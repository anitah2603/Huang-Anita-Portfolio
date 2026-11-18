"""Build tidy CSVs for Anita's final project from CBPP's SPM appendix plus Census P60-287 figures."""
import csv
import os
import sys

import openpyxl

SRC = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
wb = openpyxl.load_workbook(SRC, data_only=True)

GROUPS = ["All children", "White, not Latino", "Black, not Latino", "Latino (any race)",
          "Asian, not Latino", "Another race or multiracial, not Latino",
          "Asian American and Pacific Islander, not Latino", "American Indian and Alaska Native"]


def num(v):
    return v if isinstance(v, (int, float)) else None


def year_info(label):
    s = str(label)
    note = ""
    if s.endswith("**"):
        note = "Census updated processing system and 2020 population weights"
    elif s.endswith("*"):
        note = "Census updated processing system"
    return int(s.rstrip("*")), note


# 1. Child poverty with and without government assistance, by race/ethnicity (table_3a)
ws = wb["table_3a"]
rows = []
for r in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True):
    if r[1] is None or not str(r[1]).rstrip("*").isdigit():
        continue
    year, note = year_info(r[1])
    for i, g in enumerate(GROUPS):
        before, after = num(r[2 + i]), num(r[10 + i])
        if before is None and after is None:
            continue
        rows.append([year, str(r[1]), note, g,
                     None if before is None else round(before * 100, 2),
                     None if after is None else round(after * 100, 2)])
# When a year appears twice (old and updated processing), keep the most recent version as primary.
latest = {}
for row in rows:
    key = (row[0], row[3])
    latest[key] = row  # later rows in the sheet are the updated versions
with open(f"{OUT}/child_poverty_by_race_1967_2022.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "year_label_in_source", "series_note", "group",
                "poverty_rate_without_assistance_pct", "poverty_rate_with_assistance_pct"])
    for key in sorted(latest):
        w.writerow(latest[key])

# 2. Children by family structure (table_5a)
ws = wb["table_5a"]
fam = {"Married-couple family": (3, 9), "Not a married-couple family": (4, 10)}
latest = {}
for r in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True):
    if r[1] is None or not str(r[1]).rstrip("*").isdigit():
        continue
    year, note = year_info(r[1])
    for g, (b, a) in fam.items():
        latest[(year, g)] = [year, str(r[1]), note, g, round(r[b] * 100, 2), round(r[a] * 100, 2)]
with open(f"{OUT}/child_poverty_by_family_type_1967_2022.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "year_label_in_source", "series_note", "family_type",
                "poverty_rate_without_assistance_pct", "poverty_rate_with_assistance_pct"])
    for key in sorted(latest):
        w.writerow(latest[key])

# 3. Children lifted out of poverty by program, selected years (table_8a, all races)
ws = wb["table_8a"]
grid = [list(r) for r in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True)]
hdr = next(i for i, r in enumerate(grid) if r[2] == 1967)
years = [str(v) for v in grid[hdr][2:13]]
programs = ["All public benefits", "Social Security", "Unemployment Insurance", "AFDC/TANF",
            "Supplemental Security Income (SSI)", "SNAP (formerly food stamps)", "Rental assistance",
            "Earned Income Tax Credit (EITC)", "Child Tax Credit", "EITC and Child Tax Credit"]


def find_block(title):
    return next(i for i, r in enumerate(grid) if r[1] and str(r[1]).startswith(title))


poor_total = next(r for r in grid if r[1] == "Number in poverty")[2:13]
b_without = find_block("Would be living in poverty")
b_lifted = find_block("Lifted above the poverty line")
out = []
fixes = []
for j, yl in enumerate(years):
    year, note = year_info(yl)
    for k, p in enumerate(programs):
        without = grid[b_without + 2 + k][2 + j]
        lifted = grid[b_lifted + 2 + k][2 + j]
        # Two cells in the source are stored 1,000x too large; check against
        # (actual number in poverty + number lifted) and rescale.
        expected = poor_total[j] + lifted
        if without and abs(without / 1000 - expected) < abs(without - expected):
            fixes.append(f"{p} {yl}: {without} -> {without / 1000}")
            without = without / 1000
        out.append([year, yl, note, p, round(without), round(lifted),
                    round(100 * lifted / without, 1) if without else None])
with open(f"{OUT}/children_lifted_by_program_selected_years.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "year_label_in_source", "series_note", "program",
                "children_in_poverty_without_program", "children_lifted_above_poverty_by_program",
                "pct_of_otherwise_poor_children_lifted"])
    w.writerows(out)
print("Rescaled cells:", *fixes, sep="\n  ")

# 4. Census official SPM child poverty, 2021-2024 (P60-287, Table B-2)
with open(f"{OUT}/census_spm_child_poverty_2021_2024.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "children_under18_thousands", "children_in_spm_poverty_thousands",
                "spm_child_poverty_rate_pct"])
    w.writerows([[2021, 73470, 3829, 5.2], [2022, 72500, 8983, 12.4],
                 [2023, 72770, 9962, 13.7], [2024, 72980, 9744, 13.4]])

# 5. Census effect of each resource on child SPM poverty, 2024 (P60-287, Tables B-6 and B-7)
effects = [
    ("Refundable tax credits (EITC + refundable CTC)", "benefit", -5.08, -3704),
    ("SNAP", "benefit", -1.94, -1417),
    ("Refundable Child Tax Credit", "benefit", -2.01, -1464),
    ("Social Security", "benefit", -1.86, -1358),
    ("School lunch", "benefit", -0.91, -666),
    ("Housing subsidies", "benefit", -0.87, -634),
    ("SSI", "benefit", -0.46, -337),
    ("WIC", "benefit", -0.28, -207),
    ("TANF/general assistance", "benefit", -0.25, -181),
    ("Unemployment insurance", "benefit", -0.17, -124),
    ("Energy assistance", "benefit", -0.08, -57),
    ("Medical expenses", "expense", 2.09, 1524),
    ("FICA (payroll taxes)", "expense", 1.98, 1448),
    ("Work expenses", "expense", 1.79, 1310),
    ("Federal income tax", "expense", 0.30, 222),
]
with open(f"{OUT}/census_spm_child_resource_effects_2024.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["element", "type", "effect_on_child_spm_rate_pct_points", "children_affected_thousands"])
    w.writerows(effects)

# 6. Child Tax Credit policy timeline
timeline = [
    ("1997-08-05", "CTC created", "Taxpayer Relief Act of 1997 creates a $400-per-child credit (1998), later $500."),
    ("2017-12-22", "CTC raised to $2,000", "Tax Cuts and Jobs Act raises the maximum to $2,000 per child, with up to $1,400 refundable."),
    ("2021-03-11", "Expanded CTC enacted", "American Rescue Plan: up to $3,600 (under 6) / $3,000 (6-17), fully refundable, for tax year 2021 only."),
    ("2021-07-15", "Monthly payments begin", "Half of the 2021 credit paid in advance monthly, July-December 2021."),
    ("2022-01-01", "Expansion expires", "Prior-law credit returns for tax year 2022."),
    ("2024-01-31", "Bipartisan expansion passes House", "H.R. 7024, Tax Relief for American Families and Workers Act, passes 357-70."),
    ("2024-08-01", "Expansion stalls in Senate", "Cloture vote on H.R. 7024 fails 48-44."),
    ("2025-07-04", "CTC raised to $2,200", "2025 reconciliation law raises the maximum to $2,200; refundability rules unchanged."),
]
with open(f"{OUT}/ctc_policy_timeline.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date", "event", "detail"])
    w.writerows(timeline)
print("done")
