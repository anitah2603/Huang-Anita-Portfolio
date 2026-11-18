[← Portfolio home](./) · **Part I** · [Part II](final-project-part-two) · [Part III](final-project-part-three)

# Final Project, Part I: Who Gets Left Out?

### How the design of the Child Tax Credit decides which children escape poverty

**One-sentence summary:** In 2021, a temporary Child Tax Credit that reached nearly every child cut U.S. child poverty to a record low. When it expired, poverty more than doubled. Who a benefit reaches matters as much as how big it is.

---

## 1. Project summary

In 2021, the percentage of American children living in poverty decreased to 5.2%, marking the lowest rate ever recorded by the Census Bureau's Supplemental Poverty Measure (SPM). However, a year later, that number had risen to 12.4%. Roughly 5 million more children were living in poverty. One major reason for this increase was the expiration of the expanded Child Tax Credit (CTC). In 2021, the credit was fully refundable, so families with little or no income received the full amount. However, in 2022, it reverted to its previous design, which phases in with earnings. Consequently, children in the lowest-income families once again received partial or no credit.

My project uses this before-and-after moment to explore a broader idea: targeted universalism, which John A. Powell and his colleagues define as "setting universal goals and achieving them through targeted processes." The universal goal here is simple: ensuring that no child grows up in poverty. Data shows that achieving this goal hinges on targeted design choices, such as ensuring the credit reaches families with the lowest incomes. Recent debates illustrate this point. The 2025 law increased the maximum credit to $2,200; however, approximately 17 million children received no increase because their families earned too little to qualify for the full amount.

I want readers to understand three things. First, the safety net already keeps millions of children out of poverty. Second, the 2021 credit demonstrated how much more can be achieved. Third, specific design choices determine which children are excluded. Rather than arguing for one party's position, I will present the evidence and trade-offs that policymakers debate, such as cost and work incentives.


## 2. Project structure

### Audience

My main audience is non-policy experts, such as students, voters, and parents, who have heard of the Child Tax Credit but don't know how it works. A second audience is policy students, such as my classmates in public policy programs, who want a clear, visual summary of the evidence.


### User stories

- As a **parent who files taxes**, I want to see how the credit changes with income, so that I understand why some families get much less than others.
- As a **student new to poverty policy**, I want to see which programs keep children out of poverty, so that I can compare them on the same scale.
- As a **voter following the debate**, I want to see what different credit designs would actually do, so that I can judge proposals on evidence rather than slogans.

### Story arc

The story follows the arc from *Good Charts*: setup, conflict, and resolution. Each section will be one scrolling section in Shorthand.

| # | Section | Story beat | Key message | Planned visualization |
| --- | --- | --- | --- | --- |
| 1 | Hook: "5 million more children" | Setup | Child poverty more than doubled in a single year | Large number plus line chart, 2009–2024 |
| 2 | The safety net works | Setup | Benefits and tax credits already cut child poverty sharply | Line chart with and without benefits, 1967–2022 |
| 3 | The 2021 experiment | Rising action | A credit that reached nearly every child produced a record low | Annotated line chart and policy timeline |
| 4 | Who fell back | Conflict | Children in single-parent, Black, and Latino families saw the largest increases | Dumbbell chart, 2021 vs. 2022 |
| 5 | Why: the design | Conflict | Today's credit phases in with earnings, so the poorest children get the least | Credit amount by family earnings, with a slider |
| 6 | What lifts children now | Falling action | Tax credits, SNAP, and Social Security do the most work today | Ranked bar chart, 2024 |
| 7 | Universal goal, targeted design | Resolution | Reaching the children left out does more than raising the maximum; trade-offs remain | Comparison of two designs, then the takeaway |

**Ending:** The story closes by asking readers which design they would choose, after showing the main arguments on each side: cost, work incentives, and poverty reduction.

## 3. Initial sketches

I drew the sketches from the real data so the shapes are accurate, but the styling is rough on purpose. Notes in [blue brackets] mark planned interactions.

### Storyboard

The storyboard shows the order of the seven sections and the story beat each one plays.

![Storyboard of the seven story sections](images/final-project/sketch-0-storyboard.png)

### Section 1: Hook

The story opens with the jump from 3.8 million to 9.0 million children in poverty. The line chart shows the record low in 2021 and the rebound when the expanded credit ended.

![Sketch 1: line chart of child poverty, 2009–2024](images/final-project/sketch-1-hook.png)

### Section 2: The safety net works

Two lines show what child poverty would be without government help (gray) and what it actually is (black). The shaded gap is the number of children kept out of poverty by policy. The gap has grown since the 1990s.

![Sketch 2: child poverty with and without benefits, 1967–2022](images/final-project/sketch-2-safety-net.png)

### Section 3: The 2021 experiment

This section reuses the line chart from Section 1, adding a timeline of what changed in 2021: a larger credit, full refundability, and monthly payments from July to December.

### Section 4: Who fell back

Each row compares a group's poverty rate in 2021 and 2022. Children in single-parent families went from 11% to 25%.

![Sketch 3: dumbbell chart of poverty rates by group, 2021 vs 2022](images/final-project/sketch-3-who-fell-back.png)

### Section 5: Why: the design

This chart explains the mechanism. Under the 2021 rules, a single parent with two school-age children received $6,000 at any income up to $112,500. Under current rules, the credit starts at zero and rises only as parents earn more, so the lowest-income children receive little or nothing.

![Sketch 4: credit amount by family earnings, 2021 vs 2025 rules](images/final-project/sketch-4-credit-design.png)

### Section 6: What lifts children now

A ranked bar chart shows how many children each program lifts above the poverty line today. Refundable tax credits lead at 3.7 million children.

![Sketch 5: children lifted out of poverty by program, 2024](images/final-project/sketch-5-what-lifts-kids.png)

### Section 7: Universal goal, targeted design

The closing comparison uses CBPP's estimates for 2024: raising the maximum credit to $2,200 would have lifted only about 66,000 more children out of poverty, while letting low-income families receive the full credit would have lifted about 1.4 million.

![Sketch 6: comparison of two credit designs](images/final-project/sketch-6-resolution.png)

## 4. The data

My main dataset is the Excel appendix of the 2024 Center on Budget and Policy Priorities (CBPP) report on poverty after pandemic relief expired. The report uses the Supplemental Poverty Measure, which counts benefits and tax credits as income and subtracts taxes and necessary expenses. This makes it the appropriate measure for addressing this issue because the official poverty measure disregards tax credits entirely. The CBPP holds the poverty line constant after inflation so that rates can be compared from 1967 to 2022. The appendix also estimates the number of children lifted above the poverty line by each program in selected years and breaks down the results by race, ethnicity, and family type.

To extend the analysis to 2024, I used the Census Bureau's report, *Poverty in the United States: 2024*. The report provides the official Supplemental Poverty Measure (SPM) child poverty rates for 2021–2024 and the effect of each benefit on child poverty in 2024. For the policy sections, I refer to the Tax Policy Center for information on the rules of the 2021 credit and to CBPP for estimates on who is excluded from the current credit and the impact of different designs.

I wrote a Python script to clean the CBPP workbook and convert it into tidy CSV files that Tableau can read directly. There is one row per year and group. When the Census Bureau changed its methods in 2017 and 2020, the CBPP reported those years twice. My files keep the updated version and note the change. Since CBPP's series and the official Census series define the poverty line differently (5.4% vs. 5.2% in 2021), every chart labels the source used.

### Data files

All cleaned files are in this repository's [data folder](data/), along with a [data dictionary](data/) and the [cleaning script](data/build_data.py).

| File | Used in sections | Source |
| --- | --- | --- |
| [child_poverty_by_race_1967_2022.csv](data/child_poverty_by_race_1967_2022.csv) | 1, 2, 4 | CBPP appendix, Table 3a |
| [child_poverty_by_family_type_1967_2022.csv](data/child_poverty_by_family_type_1967_2022.csv) | 4 | CBPP appendix, Table 5a |
| [children_lifted_by_program_selected_years.csv](data/children_lifted_by_program_selected_years.csv) | 3, 6 | CBPP appendix, Table 8a |
| [census_spm_child_poverty_2021_2024.csv](data/census_spm_child_poverty_2021_2024.csv) | 1, 3 | Census P60-287, Table B-2 |
| [census_spm_child_resource_effects_2024.csv](data/census_spm_child_resource_effects_2024.csv) | 6 | Census P60-287, Tables B-6 and B-7 |
| [ctc_policy_timeline.csv](data/ctc_policy_timeline.csv) | 3, 5 | Public laws, Tax Policy Center, CBPP, Thomson Reuters |

### Still to collect for Part II

- **Credit amounts by earnings:** I will calculate the exact credit at each earnings level for a few family types from the tax rules, replacing the rough shape in Sketch 4.
- **Arguments on each side:** I will find sources on the costs and work-incentive concerns raised about a fully refundable credit, so that the ending presents both sides.
- **State-level data (optional):** The Census publishes SPM child poverty by state as three-year averages. Adding Pennsylvania could make the story more local for my audience.

## 5. Method and medium

I will build the story in **Shorthand** as a scrolling story, with each of the seven sections as its own scene. The charts will be built in **Tableau Public** and embedded in Shorthand, so readers can hover for exact values, filter by group in Section 4, and use an earnings slider in Section 5.

I plan to use a visual design in which gray represents context, blue represents the 2021 credit, and orange represents subsequent changes. Each chart will include a source line, and I will ensure the colors are legible to color-blind readers. The finished story will be linked from Part III of this portfolio.

## Sources

- Center on Budget and Policy Priorities. ["About 16 Million Children in Low-Income Families Would Gain in First Year of Bipartisan Child Tax Credit Expansion."](https://www.cbpp.org/research/federal-tax/about-16-million-children-in-low-income-families-would-gain-in-first-year-of) January 16, 2024.
- Trisi, Danilo. ["Expiration of Pandemic Relief Led to Record Increases in Poverty and Child Poverty in 2022."](https://www.cbpp.org/research/poverty-and-inequality/expiration-of-pandemic-relief-led-to-record-increases-in-poverty) CBPP, June 10, 2024, with Excel appendix.
- Parrott, Sharon. ["Statement on 2024 Census Income, Poverty, and Health Insurance Data."](https://www.cbpp.org/sites/default/files/9-9-25pov-stmt.pdf) CBPP, September 9, 2025.
- Shrider, Emily A., and Christina Bijou. [*Poverty in the United States: 2024*.](https://cps.ipums.org/cps/resources/poverty/PovReport24.pdf) U.S. Census Bureau Report P60-287, September 2025.
- Tax Policy Center. ["How did the 2021 American Rescue Plan Act change the child tax credit?"](https://taxpolicycenter.org/briefing-book/how-did-2021-american-rescue-plan-act-change-child-tax-credit) Briefing Book.
- powell, john a., Stephen Menendian, and Wendy Ake. [*Targeted Universalism: Policy & Practice*.](https://escholarship.org/content/qt9sm8b0q8/qt9sm8b0q8.pdf) Haas Institute for a Fair and Inclusive Society, UC Berkeley, 2019.
- Thomson Reuters. ["Tax bill fails to pass Senate hurdle."](https://tax.thomsonreuters.com/news/tax-bill-fails-to-pass-senate-hurdle/) August 2, 2024.
- Berinato, Scott. *Good Charts*. Harvard Business Review Press, 2016.

---

[← Portfolio home](./) · **Part I** · [Part II](final-project-part-two) · [Part III](final-project-part-three)
