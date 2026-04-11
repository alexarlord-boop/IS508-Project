# Magic Kitchens Meat Loaf Mix — Regression Analysis Design

**Date:** 2026-04-10  
**Course:** IS508 Big Data and Analytics  
**Role:** Sally Bunn, Brand Manager, United Food Products  
**Deliverable:** 5–7 min presentation + Excel regression output (last slide)

---

## Problem Statement

Sally Bunn needs a sales forecast and promotion/advertising budget for Magic Kitchens Meat Loaf Mix. She has 24 quarters of historical data: sales (in $K), promotion spend ($K), advertising spend ($K), and an economic conditions index. The assignment requires building the best predictive regression model and answering 3 case questions.

---

## Data

| Variable | Description |
|----------|-------------|
| `sales`  | Quarterly sales of Magic Kitchens meat loaf mix ($K) |
| `prom`   | Promotion expenditures ($K) — directed at food brokers/store managers |
| `adv`    | Advertising expenditures ($K) — directed at consumers (magazines, newspapers) |
| `index`  | Economic conditions index — higher = better economic times |

- 24 observations (quarters), policy: either promote OR advertise per quarter (not both)
- Assumption: Obs 1 = Q1 (Jan–Mar); Q4 is baseline for seasonal dummies

---

## Analytical Approach

### Model Candidates

Compare 4 OLS multiple regression models using **Adjusted R²** as the selection criterion:

| Model | Predictors |
|-------|-----------|
| M1 (Base) | `prom`, `adv`, `index` |
| M2 (Lags) | `prom`, `adv`, `index`, `prom_lag1`, `adv_lag1` |
| M3 (Seasonal) | `prom`, `adv`, `index`, `Q1_dummy`, `Q2_dummy`, `Q3_dummy` |
| M4 (Full) | All of the above |

**Variable significance criteria** (per course standards):
- |t-statistic| > 2
- p-value < 0.05
- Confidence interval does not contain zero

**Multicollinearity check:** Correlation matrix for all predictors before finalizing. Drop variables with high inter-correlation (|r| > 0.8).

### Seasonal Dummies

Three binary dummies: `Q1_dummy`, `Q2_dummy`, `Q3_dummy` (Q4 = baseline).  
Assigned cyclically from Obs 1 = Q1.

### Lagged Variables

`prom_lag1` = promotion spend in the previous quarter (tests whether broker/store stocking effects delay sales impact).  
`adv_lag1` = advertising spend in the previous quarter (tests consumer recall/delayed purchase).

Using lags reduces effective sample to 23 observations (Obs 1 is dropped).

---

## Answering the 3 Case Questions

### Q1: $1,000 on Promotion or Advertising?

- Compare the coefficient on `prom` vs `adv` (and their lags if included).
- Whichever has a larger, statistically significant coefficient per $1K of spend is the better use of funds.
- Note: if one variable is not statistically significant, that's itself an answer.

### Q2: Is the Product Counter-Cyclical?

- Inspect the coefficient on `index`.
- **Counter-cyclical** confirmed if the coefficient is **negative and statistically significant** (higher index → worse economy = higher sales).
- If positive, it's pro-cyclical. If not significant, economic conditions don't predict sales.

### Q3: Are There Significant Seasonal Effects?

- Inspect the seasonal dummy coefficients (Q1, Q2, Q3 vs Q4 baseline).
- Seasonal effects are present if at least one dummy is statistically significant.
- Interpret direction: positive dummy = that quarter sells more than Q4 baseline.

---

## Deliverables

1. **Python script** — runs OLS regression for all 4 models, outputs comparison table
2. **Excel file** — contains:
   - Raw data with engineered variables (lags, dummies)
   - Regression output for the best model (coefficients, std errors, t-stats, p-values, R², Adjusted R²)
   - 4-quarter forecast using the best model
3. **Presentation talking points** — structured around the 3 case questions + recommendation

---

## Constraints & Warnings

- Only 24 quarters (23 with lags) — small sample; use Adjusted R², not R²
- Promotion and advertising policy: only one used per quarter — this reduces multicollinearity concern but limits joint effects
- Do not extrapolate forecast beyond the range of historical predictor values
- "Stockpiling" effect: promotions may reduce near-term future sales (tested via lagged prom)
