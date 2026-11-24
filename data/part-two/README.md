[← Back to Final Project Part II](../../final-project-part-two)

# Part II chart data

Chart-ready CSVs for the Tableau charts in Part II. Rates are percentages (12.4 means 12.4%).

- `ctc_by_earnings.py` calculates the Child Tax Credit at every $500 of earnings for three family types under the 2021 and 2025 rules (run: `python ctc_by_earnings.py .`).
- `tableau_data.py` reshapes the Part I files in `../` plus the published figures below into these CSVs (run: `python tableau_data.py .. .` after running the credit script).

Figures typed in from publications (not from the CBPP workbook):

- `poverty_trend_2019_2025.csv`: Census Bureau SPM child poverty rates as revised in 2026 after BLS corrected the thresholds. 2019–2023 from Creamer, Census Working Paper SEHSD-WP2026-17 (corrected series); 2024–2025 from P60-290 (September 2026). Check against P60-290 Table 8 when you can.
- `relief_2021_children_kept_out.csv`: Census P60-277 (2021 data), children kept out of poverty by each resource, as tabulated by the Economic Policy Institute.
- `ctc_proposals_compared.csv`: Credit for a single parent with two children (ages 6–16) earning $15,080, calculated from each bill's credit rules (sources in the `source` column).
- `ctc_2021_effect_by_family.csv`: Burns & Fox, U.S. Census Bureau Working Paper SEHSD-WP2022-24, Tables 2 and 4.
- `left_behind_2025.csv`: Collyer et al., Columbia Center on Poverty and Social Policy, August 6, 2025.
- `design_whatif_2024.csv`: CBPP statement on 2024 Census data, September 9, 2025.
