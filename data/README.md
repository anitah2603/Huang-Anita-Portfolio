[← Back to Final Project Part I](../final-project-part-one)

# Data for "Who Gets Left Out?"

All files are CSVs derived from public sources. Rates are percentages (for example, `12.4` means 12.4%). The original CBPP workbook is saved here as [`cbpp_spm_appendix_2024.xlsx`](cbpp_spm_appendix_2024.xlsx), and the Python script that built the CSVs from it is [`build_data.py`](build_data.py) (run: `python build_data.py cbpp_spm_appendix_2024.xlsx .`).

| File | What it holds | Source |
| --- | --- | --- |
| `child_poverty_by_race_1967_2022.csv` | Child poverty rate with and without government assistance and taxes, by race/ethnicity, 1967–2022 | CBPP SPM appendix, Table 3a |
| `child_poverty_by_family_type_1967_2022.csv` | Same measure for children in married-couple vs. other families | CBPP SPM appendix, Table 5a |
| `children_lifted_by_program_selected_years.csv` | Children lifted above the poverty line by each program, selected years 1967–2022 | CBPP SPM appendix, Table 8a |
| `census_spm_child_poverty_2021_2024.csv` | Official Census SPM child poverty rate and count, 2021–2024 | Census P60-287, Table B-2 |
| `census_spm_child_resource_effects_2024.csv` | How much each benefit or expense changed the child SPM rate in 2024 | Census P60-287, Tables B-6 and B-7 |
| `ctc_policy_timeline.csv` | Key dates in Child Tax Credit policy, 1997–2025 | Public laws, Tax Policy Center, CBPP, Thomson Reuters (see Part I sources) |

## Notes on the CBPP files

- **Poverty measure:** The Supplemental Poverty Measure (SPM) counts cash and non-cash benefits and tax credits, and subtracts taxes and necessary expenses. CBPP holds the 2022 poverty line constant in real terms (adjusted for inflation with the CPI-U-RS), so rates are comparable across years.
- **"Without assistance":** The rate if government assistance and taxes were not counted.
- **Duplicate years:** Census changed its processing system in 2017 and population weights in 2020, so the source reports some years twice. These files keep the updated version and record it in `series_note`.
- **Units:** Counts in the program file are numbers of children. The workbook labels them "in thousands," but the values are whole-person counts.
- **Small samples:** Estimates for American Indian and Alaska Native children rest on small samples and change a lot from year to year.

## Combining the series

CBPP's 2021 rate (5.4%) differs slightly from Census's official 2021 SPM rate (5.2%) because the thresholds are set differently. The project uses the CBPP series for long-term trends through 2022 and the Census series for 2021–2024, and labels which is which on every chart.

## Sources

- Danilo Trisi, ["Expiration of Pandemic Relief Led to Record Increases in Poverty and Child Poverty in 2022,"](https://www.cbpp.org/research/poverty-and-inequality/expiration-of-pandemic-relief-led-to-record-increases-in-poverty) Center on Budget and Policy Priorities, June 10, 2024, Excel appendix.
- Emily A. Shrider and Christina Bijou, *Poverty in the United States: 2024*, U.S. Census Bureau Report P60-287, September 2025 ([PDF via IPUMS](https://cps.ipums.org/cps/resources/poverty/PovReport24.pdf)).
