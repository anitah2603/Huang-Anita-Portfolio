[← Portfolio home](./) · [Part I](final-project-part-one) · **Part II** · [Part III](final-project-part-three)

# Final Project, Part II: Who Gets Left Out?

### How the design of the Child Tax Credit decides which children escape poverty

**Draft Shorthand story:** [link to your Shorthand draft]

In Part I, I outlined a story about how the Child Tax Credit's design determines which children escape poverty, and sketched each section. In Part II, I revised the story based on feedback, turned the sketches into a draft Shorthand story, built the core charts in Tableau, and tested the draft with three people. This page documents that progress and the changes I plan for Part III.

---

## 1. Responding to Part I feedback

| Feedback | What I changed |
| --- | --- |
| Don't treat the Child Tax Credit as the only reason child poverty fell in 2021; there were many other COVID relief measures. | Added Section 4, "Many measures, one big lever." It shows how many children each 2021 relief measure kept out of poverty. The credit was the largest (2.9 million children), but stimulus payments (2.3 million), SNAP, Social Security, and unemployment insurance also mattered. I also use timing to separate the credit from the rest: stimulus checks went out in spring 2021, and child poverty jumped right after the monthly credit payments stopped in January 2022. |
| Address the counterpoints: why would people be against it? | Added Section 7, "The debate," covering concerns about work, cost, how to pay for it, and family structure, each paired with the evidence on both sides. |
| Look at what others have already found, and cite it. | Added Section 2 of this page, a short review of the research my story builds on. |
| Narrow the audience. | Narrowed from "parents, students, and voters" to graduate students in public policy and related programs (Section 4 of this page). |
| Briefly state what the CTC is right after the hook. | Added Section 2 of the story, "What is the Child Tax Credit?", with a short timeline. |
| See whether anyone in Congress has drafted a related bill. | Added Section 8, "What Congress has proposed," comparing the American Family Act (2025), the Family Security Act 2.0 (2022), the bipartisan H.R. 7024 (2024), and the 2025 law. |

**A data update:** In July 2026, the Bureau of Labor Statistics found coding errors in the Supplemental Poverty Measure thresholds for 2019–2024. The Census Bureau revised its estimates in August and September 2026. The changes are small (0.1 to 0.4 percentage points), but my headline numbers now use the revised rates: 5.1% in 2021 and 12.0% in 2022, instead of 5.2% and 12.4%.

## 2. What others have found

| Study | Finding | How I use it |
| --- | --- | --- |
| Census Bureau, *Poverty in the United States: 2021* (P60-277) | The Child Tax Credit kept 2.9 million children out of poverty in 2021; stimulus payments kept out 2.3 million. | Section 4: puts the credit in context with other relief |
| Burns & Fox (2022), Census working paper | The 2021 expansion alone kept 2.1 million children out of poverty; the drop was largest for children of single mothers (18.3% to 11.1%). | Section 4 |
| Parolin, Collyer & Curran (2022), Columbia | Monthly child poverty rose from 12.1% to 17% between December 2021 and January 2022, after monthly payments ended: about 3.7 million children. | Section 4: the timing evidence |
| Ananat, Glasner, Hamilton & Parolin (2022), NBER | No significant short-term change in parents' employment from the 2021 expansion. | Section 7 |
| Corinth, Meyer, Stadnicki & Wu (2021), NBER | A permanent child allowance could lead 1.5 million workers to leave the labor force. | Section 7 |
| Collyer et al. (2025), Columbia | 28% of children, and 60% of children with a single mother, can't get the full credit under the 2025 law. | Section 6 |
| McLaughlin & Rank (2018) | Child poverty costs the U.S. about $1.03 trillion a year, 5.4% of GDP. | Section 3 |

My contribution is to connect these findings in one story, focused on one design choice: whether the credit reaches families with the lowest earnings.

## 3. Storyboard and draft visualizations

The story now has nine sections. The four core charts are built for this draft; the others are planned for Part III.

| # | Section | Message | Chart | Status |
| --- | --- | --- | --- | --- |
| 1 | Hook | Child poverty more than doubled in one year | Child poverty, 2019–2025 | Part II (core) |
| 2 | What is the Child Tax Credit? | A tax credit for parents, with a catch for the lowest earners | Policy timeline | Part III |
| 3 | The safety net works | Government help already keeps millions of children out of poverty | With vs. without benefits, 1967–2022 | Part III |
| 4 | 2021: many measures, one big lever | The credit wasn't the only help in 2021, but it was the biggest for children | Children kept out of poverty by each 2021 measure | Part II (core) |
| 5 | Who fell back | When the credit expired, the poorest families fell furthest | Dumbbell, 2021 vs. 2022 | Part III |
| 6 | Why: the design | Today's credit grows only as parents earn more | Credit by earnings; children left out in 2025 | Part II (core: credit by earnings) |
| 7 | The debate | Why some lawmakers oppose a fully refundable credit | Table of arguments and evidence | Part II (text) |
| 8 | What Congress has proposed | Both parties have proposed bigger credits, with different rules for low earners | Credit for a minimum-wage parent under each plan | Part II (core) |
| 9 | Universal goal, targeted design | Reaching the children left out does more than raising the maximum | Two design changes compared | Part III |


The interactive charts appear only on the published site, not in GitHub's file preview. Sections still in progress are marked **Planned for Part III**, with a short description of the planned chart and its data.

### Section 1: Hook

**Message:** Child poverty more than doubled in one year.

This annotated line chart uses the Census Bureau's revised rates from 2019 to 2025. Readers see the pre-pandemic level, the record low in 2021, and how high poverty has stayed since.

<iframe src="https://public.tableau.com/views/ProjectII_17954870435220/Chart1?:showVizHome=no&:embed=true&:toolbar=no" width="100%" height="600" style="border:0"></iframe>


### Section 2: What is the Child Tax Credit?

**Message:** A tax credit for parents, with a catch for the lowest earners.

> **Planned for Part III.** This section is a short explainer: what the credit is, what "refundable" means, and why the credit was expanded in 2021. It also defines targeted, universal, and targeted universal policy. A timeline will mark the key changes to the credit, from its creation in 1997 through the 2021 expansion to the 2025 law.
>
> *Data:* `ctc_policy_timeline.csv` (Part I data)

### Section 3: The safety net works

**Message:** Government help already keeps millions of children out of poverty.

> **Planned for Part III.** A line chart will compare the child poverty rate with and without government benefits and taxes, from 1967 to 2022. The widening gap between the two lines shows how much the safety net does.
>
> *Data:* `safety_net_1967_2022.csv` (CBPP, anchored SPM)

### Section 4: 2021, many measures, one big lever

**Message:** The credit wasn't the only help in 2021, but it was the biggest for children.

This chart is new in Part II, added in response to feedback. It ranks the 2021 relief measures by how many children each kept out of poverty. The Child Tax Credit ranks first, and the chart shows that it worked alongside stimulus payments, SNAP, and other relief.

<iframe src="https://public.tableau.com/views/DataVisualizationProjectPartII/Chart3?:showVizHome=no&:embed=true&:toolbar=no" width="100%" height="600" style="border:0"></iframe>

### Section 5: Who fell back

**Message:** When the credit expired, the poorest families fell furthest.

> **Planned for Part III.** A dumbbell chart will compare child poverty in 2021 and 2022 by race, ethnicity, and family type. Children in single-parent, Black, and Latino families show the largest jumps.
>
> *Data:* `who_fell_back_2021_2022.csv` (CBPP) and `ctc_2021_effect_by_family.csv` (Census working paper, Burns & Fox 2022)

### Section 6: Why: the design

**Message:** Today's credit grows only as parents earn more.

This line chart is calculated from the 2021 and 2025 tax rules. Readers can switch family types with a dropdown, and a marker shows full-time minimum-wage earnings ($15,080).

<iframe src="https://public.tableau.com/views/DataVisualizationProjectPartII/Chart5?:showVizHome=no&:embed=true&:toolbar=no" width="100%" height="600" style="border:0"></iframe>

> **Planned for Part III.** A second chart will show the share of children who don't get the full credit under the 2025 law, by group. The share is highest for children with a single mother.
>
> *Data:* `left_behind_2025.csv` (Columbia Center on Poverty and Social Policy, Collyer et al. 2025)

### Section 7: The debate

**Message:** Why some lawmakers oppose a fully refundable credit.

> **Written in the Shorthand draft; to be revised in Part III.** A table sets each argument against a fully refundable credit next to the evidence on it, including the concerns about work and cost. Based on the interviews, Part III will add evidence on the wider costs of child poverty, so the debate weighs the credit's price against those costs.

### Section 8: What Congress has proposed

**Message:** Both parties have proposed bigger credits, with different rules for low earners.

This chart is new in Part II. It compares one family, a single parent with two children working full time at the federal minimum wage, across the 2021 law, three bills, and current law. Hovering over a bar shows each proposal's status, earnings rule, and estimated effect on poverty.

<iframe src="https://public.tableau.com/views/DataVisualizationProjectPartII/Chart7?:showVizHome=no&:embed=true&:toolbar=no" width="100%" height="600" style="border:0"></iframe>

### Section 9: Universal goal, targeted design

**Message:** Reaching the children left out does more than raising the maximum.

> **Planned for Part III.** A two-bar comparison will show how many more children each design change would lift out of poverty. Raising the maximum credit to $2,200 lifts about 66,000. Letting low-income families get the full credit lifts about 1.4 million. The story closes on this targeted universal approach: a credit meant for every child, designed to reach the children left out.
>
> *Data:* `design_whatif_2024.csv` (CBPP, Sept. 2025)

## 4. Audience and personas

**Target audience:** Graduate students in public policy and related programs, such as public policy, information systems, and data analytics, who will analyze or design government programs. They know basic poverty statistics but haven't compared program designs side by side. They expect sources and both sides of an argument.

I narrowed the audience from Part I for two reasons. The feedback asked for counterpoints and existing research, which this audience values most. They are also the readers I can interview, so my user research represents the people I'm writing for.

These two fictional personas represent the audience:

**Jordan, 24, public policy student.** Jordan wants to work on family policy. He knows the 2021 credit was popular but doesn't know why it ended. He is skeptical of one-sided stories and checks sources. He needs the counterarguments, consistent measures, and clear citations.

**Priya, 26, information systems student.** Priya works with data every day but has never studied tax policy. She skims text and trusts charts she can check herself. She needs a quick explanation of how the credit works and charts that make the mechanism visible without jargon.

## 5. User research protocol

### a. Target audience

Graduate students in public policy and related programs (see Section 4).

### b. How I chose interviewees

I recruited three graduate students to cover both personas:

1. A public policy student (like Jordan), to test whether the evidence feels complete and balanced
2. An information systems or data analytics student (like Priya), to test whether the charts are readable and the mechanism is clear
3. A student in another program who has never studied tax policy, to check that the story works without background

Each interview took about 15 minutes, in person or by video, using the Shorthand draft. I describe interviewees only by program and background, with no names or identifying details.

### c. Research questions

1. After the hook and explainer, can readers say what the story is about and what the credit is?
2. Does the 2021 section make clear that the credit worked alongside other relief, without overstating its role?
3. Can readers read the credit-by-earnings chart correctly?
4. Does the story feel balanced? Are the counterarguments fair and complete?
5. Can readers compare the proposals and name a trade-off?

### d. Interview script

> Thanks for helping. I'm testing a draft data story for a class. There are no wrong answers; if something is confusing, that's a problem with my design, not with you. I won't record your name. Please think out loud as you scroll. I'll try not to explain anything until the end.

0. Before we start: how familiar are you with the Child Tax Credit? (Not at all, heard of it, know how it works)
1. *(After Section 1)* In your own words, what is this story about?
2. *(After Section 2)* What is the Child Tax Credit, in one sentence?
3. *(Chart 3)* What role did the credit play in 2021, compared with the other relief?
4. *(Chart 5, task)* About how much would a single parent with two children earning $20,000 get today? *(Answer: about $2,600)*
5. *(Section 7)* Are the arguments against a refundable credit presented fairly? Is anything missing?
6. *(Chart 7)* Which proposal would help this family most, and what is the trade-off?
7. Where did you stop to think, or wish you had more information?
8. Who do you think this story is for?
9. If you could change one thing, what would it be?
10. On a scale of 1 (confusing) to 5 (very clear), how clear was the story?

## 6. Findings

### Participants

| Participant | Program and background | Familiarity with the CTC | Clarity rating (1–5) |
| --- | --- | --- | --- |
| P1 | MSPPM student | Nearly expert | 5 |
| P2 | MSPPM student | Familiar | 4 |
| P3 | MISM student | Basic | 3 |

The average clarity rating was 4.0. I had planned to interview one public policy student, one information systems student, and one student with no tax policy background. In practice I interviewed two public policy (MSPPM) students and one information systems (MISM) student. P3, who had only basic familiarity with the credit, also served as the reader without a policy background.

Quotes are lightly edited for spelling. Participants who said "CDC" meant the Child Tax Credit, so it appears here as CTC.

### Responses by question

**Q1. What is this story about?**
- P1: "Since children are independent of their parents, the socioeconomic status and financial discrimination their parents experience greatly affects their living standards."
- P2: "In order to close the child poverty gap, we need to shift from providing temporary, targeted relief to investing in a permanent, universal model."
- P3: "To help reduce child poverty, we need more policies that help low-income parents who are raising young children."

**Q2. What is the Child Tax Credit?**
- P1: "Credit that lowers federal income tax owed per child."
- P2: "Targeted tax relief that reduces your federal income tax liability."
- P3: "A tax credit that benefits children I guess?"

**Q3. The credit's role in 2021**
- P1: "The 2021 CTC relief greatly reduced the burden on parents raising children, thereby reducing the child poverty rate in the United States."
- P2: "Child poverty decreased by nearly half to a record low of 5.1%."
- P3: "It helps dropping child poverty rate to a low point."

**Q4. Chart task: credit at $20,000** (correct answer: about $2,600)
- P1: $2,550 (correct)
- P2: $15,000 (incorrect)
- P3: $2,625 (correct)

**Q5. Are the counterarguments fair?**
- P1: "I get your point, but lower federal expenses on child welfare does not mean a reduction in total federal expense."
- P2: "I would suggest to be cautious about direct money value comparison like this."
- P3: "I think it looks fair."

**Q6. Comparing proposals**
- P1: "CTC expansion in 2021, for its fair time length."
- P2: "Definitely not the 2025 current one."
- P3: "Maybe the One Family Act [the American Family Act]? It looks like the most generous one."

**Q7. Where did you get stuck?**
- P1: "Looks fine to me. But it may need more background information explanation to an audience with less policy-study backgrounds."
- P2: "It takes me some time to connect the visualizations to its policy background."
- P3: "I find it a little bit difficult navigating your 'Today's credit grows only as parents earn more' chart. It would be great if the grey cutoff line could be depicted in a more revealing way."

**Q8. Who is this for?**
- P1: "People who truly care about public welfare with policy backgrounds."
- P2: "It could be used in policy analysis if more background information and analysis are provided."
- P3: "Policy makers."

**Q9. What would you change?**
- P1: "The last chart looks a little confusing, but the topic is good."
- P2: "The color choice and annotations could be altered to convey a clearer message."
- P3: "I will look at the original data and redesign the last ('Today's credit grows only as parents earn more') chart."

### What I had to explain

After the interviews, I had to explain four things out loud:

- What targeted, universal, and targeted universal policies are
- Background on the Child Tax Credit
- Why the credit was expanded in 2021
- How yearly earnings relate to the credit a family receives

These line up with gaps in the draft. The story uses "targeted universalism" without defining it, the explainer section is too thin, and the credit-by-earnings chart does not make the relationship obvious on its own.

### Where interviewees agreed

- **The 2021 expansion clearly reduced child poverty.** All three said so in Q3. None of them mentioned the other 2021 relief measures, even after seeing the chart that ranks them. P2 answered with the overall drop in child poverty (to 5.1%), not the credit's share of it. This is the overstatement the Part I feedback warned about. Readers still take away "the credit did it," so Section 4 has to make the point more directly.
- **The credit-by-earnings chart (Chart 5) needs a redesign.** It is the chart people struggled with most. P2 answered the chart task with $15,000, which is the earnings value at the gray minimum-wage line, not a credit amount. P3 asked for the "grey cutoff line" to be "depicted in a more revealing way." P2 suggested changing the colors and annotations, and P3 wanted to redesign the chart. The main point, that low-income families get less, is not getting through.
- **The story reads as written for policy readers.** All three described the audience as policy people (Q8). P1 and P2 both said it needs more background for readers outside policy.

### Where interviewees differed

- **Background changed how fast people understood the story.** Familiarity with the credit tracked the clarity ratings: the nearly expert P1 rated it 5, and the basic-familiarity P3 rated it 3. P1 and P2 defined the credit precisely. P3 was unsure ("I guess?") and needed more explanation. Readers with policy training recognized the patterns and background quickly. Readers without it need the explainer to do more work.
- **Policy readers pushed back on the cost framing; P3 did not.** P1 argued that lower spending on child welfare does not lower total federal spending. P2 warned against comparing dollar values directly. P3 found the arguments fair. The policy students want the counterarguments to weigh wider costs, not just the price of the credit.
- **No one named a trade-off between proposals.** Each participant picked a favorite for a different reason: P1 for how long it lasted, P2 by ruling out current law, and P3 for being the most generous. None described a trade-off, so Chart 7 does not yet show what each plan gives up.

## 7. Changes planned for Part III

| What I observed | Evidence | Change for Part III |
| --- | --- | --- |
| Readers could not read the credit-by-earnings chart, and the gray line was mistaken for the answer | P2 answered $15,000; P3: "a little bit difficult navigating"; P1 and P3 called the chart confusing in Q9 | Redesign Chart 5. Label the minimum-wage line directly with both credit values. Shade the gap between the 2021 and 2025 lines as "credit lost." Add a plain-language subtitle: "A parent must earn about $33,700 to get the full credit today." Use clearer colors and fewer annotations. |
| Readers credited the 2021 drop to the CTC alone | Q3: all three described the drop as the credit's effect; none mentioned other relief | Revise Section 4's headline and annotation to say the credit was the largest of several measures. Tie Chart 1's 2021 low point to all relief, not the credit alone. |
| Readers without policy training needed more background | P1: "may need more background information"; P2: needs "more background information"; P3: "I guess?"; four topics explained out loud | Expand Section 2 into a short explainer: what the credit is, what "refundable" means, and why it was expanded in 2021. Add a short definition of targeted, universal, and targeted universal policy early in the story. |
| The cost argument looked one-sided to policy readers | P1: lower spending on child welfare "does not mean a reduction in total federal expense" | Add evidence on the wider costs of child poverty to Section 7, so the debate weighs the credit's price against those costs. |
| Raw dollar amounts were hard to compare fairly | P2: "be cautious about direct money value comparison" | In Chart 7, show each credit as a share of the family's earnings as well as in dollars (for example, $1,887 is 12.5% of $15,080, while $6,000 is about 40%). Show each plan's estimated effect on poverty next to the bar instead of only in the tooltip. |
| No one could name a trade-off between proposals | Q6: each participant chose a favorite but none named a trade-off | Add each proposal's earnings rule and status to Chart 7 as visible labels, and add a sentence on what each plan gives up (cost, work requirement, or reach). |

I will also build the remaining charts (Sections 2, 3, 5, and 9, plus the left-out chart in Section 6) and replace their placeholders in Shorthand.

## 8. Data

All Part II data files are in [data/part-two](data/part-two/). They build on the cleaned Part I files described in the [data README](data/).

| File | Used in | Source |
| --- | --- | --- |
| [poverty_trend_2019_2025.csv](data/part-two/poverty_trend_2019_2025.csv) | Section 1 | Census Bureau, revised SPM (SEHSD-WP2026-17; P60-290) |
| [safety_net_1967_2022.csv](data/part-two/safety_net_1967_2022.csv) | Section 3 | CBPP SPM appendix, Table 3a |
| [relief_2021_children_kept_out.csv](data/part-two/relief_2021_children_kept_out.csv) | Section 4 | Census P60-277, as tabulated by EPI |
| [ctc_2021_effect_by_family.csv](data/part-two/ctc_2021_effect_by_family.csv) | Section 4 (optional chart) | Burns & Fox (2022), Tables 2 and 4 |
| [who_fell_back_2021_2022.csv](data/part-two/who_fell_back_2021_2022.csv) | Section 5 | CBPP SPM appendix, Tables 3a and 5a |
| [ctc_credit_by_earnings.csv](data/part-two/ctc_credit_by_earnings.csv), [credit_by_earnings_long.csv](data/part-two/credit_by_earnings_long.csv) | Section 6 | My calculation from 2021 and 2025 tax rules ([script](data/part-two/ctc_by_earnings.py)) |
| [left_behind_2025.csv](data/part-two/left_behind_2025.csv) | Section 6 | Collyer et al. (2025) |
| [ctc_proposals_compared.csv](data/part-two/ctc_proposals_compared.csv) | Section 8 | Bill summaries; CBPP; Tax Policy Center; IRS |
| [design_whatif_2024.csv](data/part-two/design_whatif_2024.csv) | Section 9 | CBPP statement, Sept. 9, 2025 |

**How the credit amounts were calculated:** The script applies the 2025 rules ($2,200 per child, refundable portion up to $1,700 per child, phased in at 15% of earnings above $2,500, with the rest limited by income tax owed) and the 2021 rules ($3,000 per child ages 6–17, fully refundable). It assumes earnings are the family's only income, the standard deduction, and children ages 6–16, who qualify under both laws. The proposals comparison applies each bill's credit rules to the same family and ignores the bills' other tax changes, such as the Family Security Act 2.0's cuts to the EITC.

**A note on measures:** CBPP's long-run series (Sections 3 and 5) holds the 2022 poverty line constant and was published before the 2026 threshold correction, so its rates differ slightly from Census's revised rates. Each chart names its source.

## 9. Use of generative AI

I used Claude (Anthropic) as an assistant in Part II. Its contributions:

- Wrote the Python scripts that reshape the data for Tableau and calculate the credit by earnings and under each proposal, following rules I checked against IRS, Tax Foundation, and bill summaries
- Found research on the other 2021 relief measures, counterarguments, and congressional bills after the Part I feedback, and identified the Census Bureau's 2026 revisions to the poverty rates
- Checked figures from my earlier group presentation against their original sources, and flagged one that didn't match
- Drafted a Tableau build guide, the first version of the Shorthand section copy, the personas, and this research protocol


My own work: 
- Built every chart in Tableau
- Built and edited the Shorthand story
- Conducted all three interviews
- Wrote the findings, and decided on the changes for Part III

## Sources

- Ananat, Elizabeth, Benjamin Glasner, Christal Hamilton, and Zachary Parolin. ["Effects of the Expanded Child Tax Credit on Employment Outcomes."](https://www.nber.org/papers/w29823) NBER Working Paper 29823, 2022.
- Bijou, Christina, and Emily A. Shrider. [*Poverty in the United States: 2025*.](https://www.census.gov/library/publications/2026/demo/p60-290.html) U.S. Census Bureau Report P60-290, September 2026.
- Burns, Kalee, and Liana E. Fox. ["The Impact of the 2021 Expanded Child Tax Credit on Child Poverty."](https://www.census.gov/content/dam/Census/library/working-papers/2022/demo/sehsd-wp2022-24.pdf) U.S. Census Bureau Working Paper SEHSD-WP2022-24, 2022.
- Burns, Kalee, Liana Fox, and Danielle Wilson. ["Expansions to Child Tax Credit Contributed to 46% Decline in Child Poverty Since 2020."](https://www.census.gov/library/stories/2022/09/record-drop-in-child-poverty.html) U.S. Census Bureau, September 13, 2022.
- Center on Budget and Policy Priorities. ["About 16 Million Children in Low-Income Families Would Gain in First Year of Bipartisan Child Tax Credit Expansion."](https://www.cbpp.org/research/federal-tax/about-16-million-children-in-low-income-families-would-gain-in-first-year-of) January 16, 2024.
- Center on Budget and Policy Priorities. ["Romney Child Tax Credit Proposal Is Step Forward But Falls Short, Targets Low-Income Families to Pay for It."](https://www.cbpp.org/es/research/federal-tax/romney-child-tax-credit-proposal-is-step-forward-but-falls-short-targets-low) June 2022.
- Center on Budget and Policy Priorities. [Statement on 2024 Census Income, Poverty, and Health Insurance Data.](https://www.cbpp.org/sites/default/files/9-9-25pov-stmt.pdf) September 9, 2025.
- Collyer, Sophie, Christopher Yera, Megan Curran, David Harris, and Christopher Wimer. ["Children Left Behind by the H.R.1 'One Big Beautiful Bill Act' Child Tax Credit."](https://povertycenter.columbia.edu/publication/2025/children-left-behind-by-child-tax-credit-reconciliation) Columbia Center on Poverty and Social Policy, August 6, 2025.
- Corinth, Kevin, Bruce D. Meyer, Matthew Stadnicki, and Derek Wu. ["The Anti-Poverty, Targeting, and Labor Supply Effects of Replacing a Child Tax Credit with a Child Allowance."](https://www.nber.org/papers/w29366) NBER Working Paper 29366, 2021.
- Creamer, John. ["Revising Supplemental Poverty Measure Estimates from 2019 to 2024."](https://www.census.gov/library/working-papers/2026/demo/sehsd-wp2026-17.html) U.S. Census Bureau Working Paper SEHSD-WP2026-17, August 2026.
- Dante, Hugo, and Rachel Sheffield. ["Child Tax Credits Should Promote Work, Not Undermine It."](https://www.jec.senate.gov/public/index.cfm/republicans/2021/11/child-tax-credits-should-promote-work-not-undermine-it) Joint Economic Committee Republicans, November 2, 2021.
- DeLauro, Rosa, Suzan DelBene, and Ritchie Torres. ["DeLauro, DelBene, Torres Introduce Legislation to Make Permanent Expanded Child Tax Credit."](https://delauro.house.gov/media-center/press-releases/delauro-delbene-torres-introduce-legislation-make-permanent-expanded) April 9, 2025.
- Economic Policy Institute. ["Pandemic safety net programs kept millions out of poverty in 2021, new Census data show."](https://www.epi.org/blog/pandemic-safety-net-programs-kept-millions-out-of-poverty-in-2021-new-census-data-show/) September 2022.
- McLaughlin, Michael, and Mark R. Rank. "Estimating the Economic Cost of Childhood Poverty in the United States." *Social Work Research* 42, no. 2 (2018): 73–83. ([summary](https://source.washu.edu/2018/04/childhood-poverty-cost-u-s-1-03-trillion-in-a-year-study-finds/))
- Mottamal, Sita, Utami, Bidisha Kaphle, and Anita Huang. "Child Poverty in the United States." Presentation for course 90-704, Carnegie Mellon University, September 21, 2026.
- Parolin, Zachary, Sophie Collyer, and Megan A. Curran. ["Absence of Monthly Child Tax Credit Leads to 3.7 Million More Children in Poverty in January 2022."](https://www.povertycenter.columbia.edu/publication/monthly-poverty-january-2022) Columbia Center on Poverty and Social Policy, February 17, 2022.
- Tax Foundation. [2025 Tax Brackets.](https://taxfoundation.org/data/all/federal/2025-tax-brackets/)
- Tax Policy Center. ["How did the 2021 American Rescue Plan Act change the child tax credit?"](https://taxpolicycenter.org/briefing-book/how-did-2021-american-rescue-plan-act-change-child-tax-credit)
- Thomson Reuters. ["Tax bill fails to pass Senate hurdle."](https://tax.thomsonreuters.com/news/tax-bill-fails-to-pass-senate-hurdle/) August 2024.
- Trisi, Danilo. ["Expiration of Pandemic Relief Led to Record Increases in Poverty and Child Poverty in 2022."](https://www.cbpp.org/research/poverty-and-inequality/expiration-of-pandemic-relief-led-to-record-increases-in-poverty) CBPP, June 10, 2024.

---

[← Portfolio home](./) · [Part I](final-project-part-one) · **Part II** · [Part III](final-project-part-three)
