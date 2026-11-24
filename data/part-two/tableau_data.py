"""Chart-ready (long-format) CSVs for building the Part II charts in Tableau."""
import csv
import sys

PART1, OUT = sys.argv[1], sys.argv[2]


def read(name, folder=PART1):
    with open(f"{folder}/{name}") as fh:
        return list(csv.DictReader(fh))


def write(name, header, rows):
    with open(f"{OUT}/{name}", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


race = read("child_poverty_by_race_1967_2022.csv")
fam = read("child_poverty_by_family_type_1967_2022.csv")
census = read("census_spm_child_poverty_2021_2024.csv")

# Chart 1: trend, 2019-2025.
# Census SPM child rates use the corrected thresholds BLS re-released in July 2026:
# 2019-2023 from Creamer, Census working paper SEHSD-WP2026-17 (corrected series);
# 2024-2025 from Census P60-290 (Sept. 2026) news-conference slides. Verify against P60-290 Table 8.
census_revised = {2019: 12.4, 2020: 9.6, 2021: 5.1, 2022: 12.0, 2023: 13.5, 2024: 13.5, 2025: 13.4}
write("poverty_trend_2019_2025.csv", ["year", "child_spm_poverty_rate_pct", "source"],
      [[y, v, "Census SPM, revised 2026"] for y, v in census_revised.items()])

# Chart 3: 2021 relief measures, children kept out of poverty (Census P60-277, as tabulated by EPI)
write("relief_2021_children_kept_out.csv", ["measure", "children_kept_out_of_poverty", "is_child_tax_credit"], [
    ["Child Tax Credit", 2919000, "yes"],
    ["Stimulus payments (third round)", 2270000, "no"],
    ["SNAP and school lunch", 1188000, "no"],
    ["Social Security", 1065000, "no"],
    ["Housing subsidies", 595000, "no"],
    ["Unemployment insurance", 525000, "no"],
    ["SSI", 288000, "no"],
])

# Chart 7: congressional proposals compared, for a single parent of two children (ages 6-16)
# earning $15,080 (full time at the federal minimum wage). Amounts calculated from each bill's rules.
write("ctc_proposals_compared.csv",
      ["proposal", "year", "sponsors", "status", "max_credit_per_child_age_6_16", "fully_refundable",
       "earnings_rule", "payments", "credit_single_parent_2_kids_at_15080", "credit_at_zero_earnings",
       "estimated_poverty_effect", "source"], [
    ["2021 expanded credit (American Rescue Plan)", 2021, "Democratic majority", "Law for 2021 only; expired",
     3000, "yes", "None", "Half paid monthly, July-Dec 2021", 6000, 6000,
     "2.1 million children kept out of poverty by the expansion (Census)", "Tax Policy Center; Burns & Fox 2022"],
    ["Family Security Act 2.0", 2022, "Sens. Romney, Daines, Burr (R)", "Introduced; not passed",
     3000, "partly", "Full credit with $10,000+ prior-year earnings; proportional below", "Monthly", 6000, 0,
     "About 1.3 million children lifted, net of offsets (CBPP)", "CBPP, June 2022"],
    ["Tax Relief for American Families and Workers Act (H.R. 7024)", 2024, "Bipartisan (Wyden, Smith)",
     "Passed House 357-70; stalled in Senate", 2100, "no", "15% of earnings above $2,500, per child",
     "Annual", 3774, 0, "Up to 400,000 children lifted in year one; 500,000+ when fully in effect (CBPP)",
     "CBPP, Jan. 2024"],
    ["2025 law (One Big Beautiful Bill Act)", 2025, "Republican majority", "Law", 2200, "no",
     "15% of family earnings above $2,500; refundable part capped at $1,700 per child", "Annual", 1887, 0,
     "About 66,000 more children lifted vs. prior law (CBPP)", "IRS; CBPP, Sept. 2025"],
    ["American Family Act (H.R. 2763)", 2025, "Reps. DeLauro, DelBene, Torres; Sen. Bennet (D)",
     "Introduced; not passed", 3600, "yes", "None", "Monthly", 7200, 7200, "No estimate found",
     "DeLauro press release, Apr. 9, 2025"],
])

# Chart 2: with vs without benefits, all children, long format
rows = []
for r in race:
    if r["group"] != "All children":
        continue
    rows.append([int(r["year"]), "Without benefits and taxes", float(r["poverty_rate_without_assistance_pct"])])
    rows.append([int(r["year"]), "With benefits and taxes", float(r["poverty_rate_with_assistance_pct"])])
write("safety_net_1967_2022.csv", ["year", "measure", "child_poverty_rate_pct"], rows)

# Chart 3: dumbbell, 2021 vs 2022
groups = [("Children in single-parent families", "Family type", fam, "family_type", "Not a married-couple family"),
          ("Latino children", "Race/ethnicity", race, "group", "Latino (any race)"),
          ("Black children", "Race/ethnicity", race, "group", "Black, not Latino"),
          ("All children", "All", race, "group", "All children"),
          ("Asian children", "Race/ethnicity", race, "group", "Asian, not Latino"),
          ("White children", "Race/ethnicity", race, "group", "White, not Latino"),
          ("Children in married-couple families", "Family type", fam, "family_type", "Married-couple family")]
rows = []
for order, (label, gtype, src, key, val) in enumerate(groups, 1):
    for y in (2021, 2022):
        r = next(x for x in src if x[key] == val and int(x["year"]) == y)
        rows.append([label, gtype, order, y, float(r["poverty_rate_with_assistance_pct"])])
write("who_fell_back_2021_2022.csv", ["group", "group_type", "sort_order", "year", "child_poverty_rate_pct"], rows)

# Chart 4: credit by earnings, long format
credit = read("ctc_credit_by_earnings.csv", OUT)
rows = []
for r in credit:
    rows.append([r["family_type"], int(r["annual_earnings"]), "2021 (American Rescue Plan)", int(r["credit_2021_arpa"])])
    rows.append([r["family_type"], int(r["annual_earnings"]), "2025 law", int(r["credit_2025_law"])])
write("credit_by_earnings_long.csv", ["family_type", "annual_earnings", "law", "credit"], rows)

# Chart 6: what-if comparison
write("design_whatif_2024.csv", ["design_change", "additional_children_lifted", "source"], [
    ["Raise the maximum credit to $2,200", 66000, "CBPP statement, Sept. 9, 2025"],
    ["Let low-income families get the full credit", 1400000, "CBPP statement, Sept. 9, 2025"],
])
# 2021 credit's effect by family type (Burns & Fox 2022, Census working paper, Tables 2 and 4)
rows = []
for fam_t, vals in [("Married-couple families", (5.0, 4.1, 2.8)),
                    ("Mother, no spouse or partner", (19.9, 18.3, 11.1)),
                    ("Father, no spouse or partner", (14.0, 12.5, 8.9)),
                    ("Cohabiting-partner families", (13.4, 12.9, 7.5))]:
    for scen, v in zip(["No Child Tax Credit", "Pre-2021 credit rules", "2021 expanded credit"], vals):
        rows.append([fam_t, scen, v])
write("ctc_2021_effect_by_family.csv", ["family_type", "scenario", "child_spm_poverty_rate_2021_pct"], rows)

# Children left behind by the 2025 credit (Collyer et al. 2025, Columbia CPSP)
write("left_behind_2025.csv", ["group", "pct_of_children_not_getting_full_credit", "is_overall"], [
    ["Children with a single mother", 60, "no"], ["American Indian or Alaska Native children", 48, "no"],
    ["Black children", 45, "no"], ["Latino children", 39, "no"], ["Children in large families", 36, "no"],
    ["Rural children", 35, "no"], ["Children under 6", 30, "no"], ["All children under 17", 28, "yes"]])
print("ok")
