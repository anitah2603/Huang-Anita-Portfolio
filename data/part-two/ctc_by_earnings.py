"""Child Tax Credit by earnings: 2021 (American Rescue Plan) vs 2025 law, for three family types.

Simplifications (stated on the project page): earnings are the only income; children are ages 6-16
(eligible under both laws); standard deduction; no other credits. The CTC is applied against
income tax before other credits.
"""
import csv
import math
import sys

OUT = sys.argv[1]

# 2025 parameters (IRS / Tax Foundation, reflecting the 2025 law)
STD = {"HoH": 23625, "MFJ": 31500}
BRACKETS = {  # (upper bound of taxable income, rate)
    "HoH": [(17000, 0.10), (64850, 0.12), (103350, 0.22), (197300, 0.24), (250500, 0.32)],
    "MFJ": [(23850, 0.10), (96950, 0.12), (206700, 0.22), (394600, 0.24), (501050, 0.32)],
}
PHASEOUT_2025 = {"HoH": 200000, "MFJ": 400000}
PHASEOUT_2021_EXTRA = {"HoH": 112500, "MFJ": 150000}

FAMILIES = [
    ("Single parent, 1 child", "HoH", 1),
    ("Single parent, 2 children", "HoH", 2),
    ("Married couple, 2 children", "MFJ", 2),
]


def income_tax(filing, earnings):
    taxable = max(0, earnings - STD[filing])
    tax, lower = 0.0, 0
    for upper, rate in BRACKETS[filing]:
        if taxable <= lower:
            break
        tax += (min(taxable, upper) - lower) * rate
        lower = upper
    return tax


def reduction(agi, threshold):
    return 50 * math.ceil(max(0, agi - threshold) / 1000)


def ctc_2025(filing, kids, earnings):
    maximum = max(0, 2200 * kids - reduction(earnings, PHASEOUT_2025[filing]))
    nonref = min(maximum, income_tax(filing, earnings))
    refundable = min(maximum - nonref, 1700 * kids, 0.15 * max(0, earnings - 2500))
    return round(nonref + refundable), round(refundable)


def ctc_2021(filing, kids, earnings):
    extra = max(0, 1000 * kids - reduction(earnings, PHASEOUT_2021_EXTRA[filing]))
    base = max(0, 2000 * kids - reduction(earnings, PHASEOUT_2025[filing]))  # same $200K/$400K thresholds
    return extra + base  # fully refundable, no earnings requirement


rows = []
for name, filing, kids in FAMILIES:
    for e in range(0, 250001, 500):
        c25, ref25 = ctc_2025(filing, kids, e)
        c21 = ctc_2021(filing, kids, e)
        rows.append([name, filing, kids, e, c21, c25, ref25, 2200 * kids,
                     round(100 * c25 / (2200 * kids), 1)])

with open(f"{OUT}/ctc_credit_by_earnings.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["family_type", "filing_status", "children", "annual_earnings",
                "credit_2021_arpa", "credit_2025_law", "credit_2025_refundable_part",
                "max_credit_2025", "pct_of_max_2025"])
    w.writerows(rows)

# Quick summary for the write-up
for name, filing, kids in FAMILIES:
    full = next(e for e in range(0, 250001, 100) if ctc_2025(filing, kids, e)[0] >= 2200 * kids)
    print(f"{name}: full 2025 credit reached at ${full:,} of earnings;"
          f" at $0: 2021=${ctc_2021(filing, kids, 0):,}, 2025=${ctc_2025(filing, kids, 0)[0]:,};"
          f" at full-time federal minimum wage ($15,080): 2025=${ctc_2025(filing, kids, 15080)[0]:,}"
          f" vs 2021=${ctc_2021(filing, kids, 15080):,}")
