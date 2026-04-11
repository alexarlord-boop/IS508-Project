# Magic Kitchens Regression Analysis — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the best OLS multiple regression model to forecast Magic Kitchens meat loaf mix sales, and answer 3 case questions for Sally Bunn's IS508 presentation.

**Architecture:** Single Python analysis script (`analysis/regression.py`) that loads hardcoded data, engineers features (lags, seasonal dummies), runs 4 candidate models, selects the best by Adjusted R², interprets results against the 3 case questions, and writes a formatted Excel output file.

**Tech Stack:** Python 3, pandas, numpy, statsmodels (OLS), openpyxl (Excel output)

---

## File Structure

| File | Purpose |
|------|---------|
| `analysis/regression.py` | Main analysis script — data, features, models, questions, Excel export |
| `output/magic_kitchens_output.xlsx` | Generated Excel file for presentation last slide |

---

## Task 1: Load Data and Verify Shape

**Files:**
- Create: `analysis/regression.py`

- [ ] **Step 1.1: Create the script with the 24-observation dataset**

```python
# analysis/regression.py
import pandas as pd
import numpy as np
import statsmodels.api as sm
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import os

# ── 1. DATA ──────────────────────────────────────────────────────────────────
data = {
    'obs':   list(range(1, 25)),
    'sales': [504.72, 406.59, 398.55, 587.76, 598.92, 703.62, 387.24, 365.67,
              388.71, 372.96, 603.30, 614.73, 484.38, 227.76, 329.13, 308.25,
              433.86, 514.98, 404.70, 245.43, 433.20, 627.24, 647.61, 342.81],
    'prom':  [15.6, 22.2, 0.0, 0.0, 0.0, 31.8, 21.3, 3.9,
              0.0, 8.4, 45.3, 50.1, 39.6, 4.2, 0.0, 0.0,
              0.0, 13.8, 17.7, 0.0, 17.4, 37.8, 42.3, 11.4],
    'adv':   [30, 36, 45, 57, 39, 21, 12, 6,
              6, 30, 30, 33, 6, 33, 6, 3,
              45, 48, 0, 15, 9, 54, 36, 39],
    'index': [100, 102, 104, 104, 104, 100, 98, 96,
              98, 103, 105, 107, 107, 107, 108, 105,
              103, 108, 110, 112, 113, 112, 113, 114],
}
df = pd.DataFrame(data)
```

- [ ] **Step 1.2: Verify data shape**

```python
assert df.shape == (24, 5), f"Expected (24, 5), got {df.shape}"
assert df['sales'].mean().round(2) == 455.51, f"Mean mismatch: {df['sales'].mean()}"
print("✓ Data loaded: 24 rows × 5 columns")
print(df.describe().round(2))
```

Run: `python3 analysis/regression.py`  
Expected: prints "✓ Data loaded: 24 rows × 5 columns" and a summary table.

---

## Task 2: Feature Engineering (Lags + Seasonal Dummies)

**Files:**
- Modify: `analysis/regression.py` — append after Task 1 code

- [ ] **Step 2.1: Create lagged variables**

```python
# ── 2. FEATURE ENGINEERING ───────────────────────────────────────────────────
# Lagged variables (1-quarter delay)
df['prom_lag1'] = df['prom'].shift(1)
df['adv_lag1']  = df['adv'].shift(1)
```

- [ ] **Step 2.2: Create seasonal dummies (Obs 1 = Q1)**

```python
# Seasonal dummies — assumption: Obs 1 = Q1 (Jan–Mar)
# Q4 is baseline (winter/cold) — omitted to avoid dummy trap
quarter = ((df['obs'] - 1) % 4) + 1   # cycles 1,2,3,4,1,2,3,...
df['Q1'] = (quarter == 1).astype(int)
df['Q2'] = (quarter == 2).astype(int)
df['Q3'] = (quarter == 3).astype(int)
# Q4 = 1 when Q1=Q2=Q3=0 (baseline)
```

- [ ] **Step 2.3: Verify dummies — each quarter should appear exactly 6 times**

```python
print("\n── Quarter distribution ──")
print(f"Q1 obs: {df['Q1'].sum()} (expect 6)")
print(f"Q2 obs: {df['Q2'].sum()} (expect 6)")
print(f"Q3 obs: {df['Q3'].sum()} (expect 6)")
print(f"Q4 obs: {(24 - df['Q1'].sum() - df['Q2'].sum() - df['Q3'].sum())} (expect 6)")
assert df['Q1'].sum() == df['Q2'].sum() == df['Q3'].sum() == 6
print("✓ Seasonal dummies correct")
```

- [ ] **Step 2.4: Correlation matrix — check for multicollinearity**

```python
print("\n── Correlation matrix (predictors) ──")
cols = ['prom', 'adv', 'index', 'prom_lag1', 'adv_lag1']
corr = df[cols].corr().round(2)
print(corr)
# Flag pairs with |r| > 0.7
high_corr = [(c1, c2, corr.loc[c1, c2])
             for i, c1 in enumerate(cols)
             for j, c2 in enumerate(cols)
             if i < j and abs(corr.loc[c1, c2]) > 0.7]
if high_corr:
    print(f"\n⚠ High correlation pairs: {high_corr}")
else:
    print("\n✓ No severe multicollinearity detected")
```

Run: `python3 analysis/regression.py`  
Expected: all assertions pass, correlation matrix prints, note any flagged pairs.

---

## Task 3: Build and Compare 4 Regression Models

**Files:**
- Modify: `analysis/regression.py` — append after Task 2 code

- [ ] **Step 3.1: Define a helper function to run OLS and print summary**

```python
# ── 3. MODELS ─────────────────────────────────────────────────────────────────
def run_ols(df_in, predictors, label):
    """Run OLS regression; returns fitted model."""
    d = df_in.dropna(subset=predictors + ['sales']).copy()
    X = sm.add_constant(d[predictors])
    y = d['sales']
    model = sm.OLS(y, X).fit()
    n = len(d)
    print(f"\n{'─'*60}")
    print(f"  {label}  (n={n})")
    print(f"{'─'*60}")
    print(f"  Adj. R²: {model.rsquared_adj:.4f}   R²: {model.rsquared:.4f}   AIC: {model.aic:.1f}")
    for var in model.params.index:
        sig = "***" if model.pvalues[var] < 0.01 else ("**" if model.pvalues[var] < 0.05 else ("*" if model.pvalues[var] < 0.10 else ""))
        print(f"  {var:15s}  coef={model.params[var]:8.3f}  t={model.tvalues[var]:6.2f}  p={model.pvalues[var]:.3f}  {sig}")
    return model
```

- [ ] **Step 3.2: Run M1 — Base model**

```python
m1 = run_ols(df, ['prom', 'adv', 'index'], "M1: Base (prom + adv + index)")
```

- [ ] **Step 3.3: Run M2 — With lags**

```python
m2 = run_ols(df, ['prom', 'adv', 'index', 'prom_lag1', 'adv_lag1'],
             "M2: Lags (+ prom_lag1 + adv_lag1)")
```

- [ ] **Step 3.4: Run M3 — With seasonal dummies**

```python
m3 = run_ols(df, ['prom', 'adv', 'index', 'Q1', 'Q2', 'Q3'],
             "M3: Seasonal (+ Q1 Q2 Q3 dummies)")
```

- [ ] **Step 3.5: Run M4 — Full model**

```python
m4 = run_ols(df, ['prom', 'adv', 'index', 'prom_lag1', 'adv_lag1', 'Q1', 'Q2', 'Q3'],
             "M4: Full (lags + seasonal)")
```

- [ ] **Step 3.6: Print comparison table and select best model**

```python
print("\n── Model Comparison ──")
models = {'M1 Base': m1, 'M2 Lags': m2, 'M3 Seasonal': m3, 'M4 Full': m4}
comp = pd.DataFrame({
    name: {'Adj R²': m.rsquared_adj, 'R²': m.rsquared, 'AIC': m.aic, 'n': int(m.nobs)}
    for name, m in models.items()
}).T.round(4)
print(comp)

best_name = comp['Adj R²'].idxmax()
best_model = models[best_name]
print(f"\n★ Best model: {best_name} (Adj R² = {comp.loc[best_name, 'Adj R²']:.4f})")
```

Run: `python3 analysis/regression.py`  
Expected: 4 model summaries with coefficients, then a comparison table and best model identified.

---

## Task 4: Answer the 3 Case Questions

**Files:**
- Modify: `analysis/regression.py` — append after Task 3 code

- [ ] **Step 4.1: Q1 — Advertising vs Promotion ($1K decision)**

```python
# ── 4. CASE QUESTIONS ─────────────────────────────────────────────────────────
print("\n" + "═"*60)
print("CASE QUESTION ANSWERS")
print("═"*60)

print("\n── Q1: $1,000 on Advertising or Promotion? ──")
params = best_model.params
pvals  = best_model.pvalues

prom_coef      = params.get('prom', None)
adv_coef       = params.get('adv', None)
prom_lag_coef  = params.get('prom_lag1', None)
adv_lag_coef   = params.get('adv_lag1', None)

prom_sig = pvals.get('prom', 1) < 0.05
adv_sig  = pvals.get('adv', 1)  < 0.05
prom_lag_sig = pvals.get('prom_lag1', 1) < 0.05
adv_lag_sig  = pvals.get('adv_lag1', 1)  < 0.05

print(f"  prom coefficient    : {prom_coef:.3f}  {'(significant)' if prom_sig else '(NOT significant)'}")
print(f"  adv  coefficient    : {adv_coef:.3f}  {'(significant)' if adv_sig else '(NOT significant)'}")
if prom_lag_coef is not None:
    print(f"  prom_lag1 coefficient: {prom_lag_coef:.3f}  {'(significant)' if prom_lag_sig else '(NOT significant)'}")
if adv_lag_coef is not None:
    print(f"  adv_lag1  coefficient: {adv_lag_coef:.3f}  {'(significant)' if adv_lag_sig else '(NOT significant)'}")

# Total prom effect (current + lag)
total_prom = (prom_coef or 0) + (prom_lag_coef or 0)
total_adv  = (adv_coef  or 0) + (adv_lag_coef  or 0)
print(f"\n  Total prom effect per $1K (current + lag): ${total_prom:.2f}K in sales")
print(f"  Total adv  effect per $1K (current + lag): ${total_adv:.2f}K in sales")

if total_prom > total_adv:
    print("\n  → RECOMMENDATION: Spend on PROMOTION")
else:
    print("\n  → RECOMMENDATION: Spend on ADVERTISING")
```

- [ ] **Step 4.2: Q2 — Counter-cyclical?**

```python
print("\n── Q2: Is Meat Loaf Mix Counter-Cyclical? ──")
index_coef = params.get('index', None)
index_sig  = pvals.get('index', 1) < 0.05
print(f"  index coefficient: {index_coef:.3f}  {'(significant p<0.05)' if index_sig else '(NOT significant)'}")
if index_coef is not None:
    if index_coef < 0 and index_sig:
        print("  → CONFIRMED counter-cyclical: higher index (better economy) → lower sales")
    elif index_coef > 0 and index_sig:
        print("  → NOT counter-cyclical (pro-cyclical): higher index → higher sales")
    else:
        print("  → INCONCLUSIVE: economic index not a significant predictor in this model")
```

- [ ] **Step 4.3: Q3 — Seasonal effects?**

```python
print("\n── Q3: Significant Seasonal Effects? ──")
seasonal_results = {}
for q in ['Q1', 'Q2', 'Q3']:
    if q in params:
        coef = params[q]
        pval = pvals[q]
        sig  = pval < 0.05
        seasonal_results[q] = {'coef': coef, 'pval': pval, 'sig': sig}
        print(f"  {q} vs Q4: coef={coef:.2f}  p={pval:.3f}  {'★ significant' if sig else 'not significant'}")

if any(v['sig'] for v in seasonal_results.values()):
    print("\n  → CONFIRMED: Significant seasonal effects exist")
    best_q = max(seasonal_results, key=lambda k: seasonal_results[k]['coef'])
    worst_q = min(seasonal_results, key=lambda k: seasonal_results[k]['coef'])
    print(f"  Highest sales quarter vs Q4 baseline: {best_q} (+{seasonal_results[best_q]['coef']:.1f}K)")
    print(f"  Lowest  sales quarter vs Q4 baseline: {worst_q} ({seasonal_results[worst_q]['coef']:.1f}K)")
else:
    print("\n  → NOT CONFIRMED: No seasonal dummies are statistically significant")
```

Run: `python3 analysis/regression.py`  
Expected: 3 blocks of output answering each case question with direction and interpretation.

---

## Task 5: Generate Excel Output

**Files:**
- Modify: `analysis/regression.py` — append after Task 4 code
- Create (auto-generated): `output/magic_kitchens_output.xlsx`

- [ ] **Step 5.1: Set up Excel workbook structure**

```python
# ── 5. EXCEL OUTPUT ────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)
wb = Workbook()

# Styles
header_font   = Font(bold=True, color="FFFFFF")
header_fill   = PatternFill("solid", fgColor="1F4E79")
subhead_fill  = PatternFill("solid", fgColor="BDD7EE")
sig_fill      = PatternFill("solid", fgColor="E2EFDA")  # green — significant
center        = Alignment(horizontal='center')
left          = Alignment(horizontal='left')
thin          = Side(style='thin')
border        = Border(left=thin, right=thin, top=thin, bottom=thin)

def style_header(cell, width=None):
    cell.font      = header_font
    cell.fill      = header_fill
    cell.alignment = center
    cell.border    = border

def style_subheader(cell):
    cell.fill      = subhead_fill
    cell.font      = Font(bold=True)
    cell.alignment = center
    cell.border    = border
```

- [ ] **Step 5.2: Sheet 1 — Raw data with engineered features**

```python
ws_data = wb.active
ws_data.title = "Data"

# Header row
headers = ['Obs', 'Sales ($K)', 'Prom ($K)', 'Adv ($K)', 'Index',
           'Prom Lag1', 'Adv Lag1', 'Q1', 'Q2', 'Q3']
for col, h in enumerate(headers, 1):
    c = ws_data.cell(row=1, column=col, value=h)
    style_header(c)
    ws_data.column_dimensions[get_column_letter(col)].width = 12

# Data rows
display_cols = ['obs', 'sales', 'prom', 'adv', 'index', 'prom_lag1', 'adv_lag1', 'Q1', 'Q2', 'Q3']
for r_idx, (_, row) in enumerate(df.iterrows(), 2):
    for c_idx, col in enumerate(display_cols, 1):
        val = row[col]
        ws_data.cell(row=r_idx, column=c_idx, value=round(float(val), 2) if pd.notna(val) else '')
        ws_data.cell(row=r_idx, column=c_idx).border = border

# Means row
ws_data.cell(row=27, column=1, value='Mean')
ws_data.cell(row=27, column=1).font = Font(bold=True)
for c_idx, col in enumerate(['sales', 'prom', 'adv', 'index'], 2):
    ws_data.cell(row=27, column=c_idx, value=round(df[col].mean(), 2))
    ws_data.cell(row=27, column=c_idx).font = Font(bold=True)
print("✓ Data sheet written")
```

- [ ] **Step 5.3: Sheet 2 — Regression output for the best model**

```python
ws_reg = wb.create_sheet("Best Model Regression")

# Title
ws_reg.merge_cells('A1:G1')
title_cell = ws_reg['A1']
title_cell.value = f"OLS Regression Results — {best_name}"
title_cell.font = Font(bold=True, size=14, color="FFFFFF")
title_cell.fill = header_fill
title_cell.alignment = center

# Model stats
ws_reg['A3'] = 'Dependent Variable:'
ws_reg['B3'] = 'Sales ($K)'
ws_reg['A4'] = 'Observations:'
ws_reg['B4'] = int(best_model.nobs)
ws_reg['A5'] = 'R-squared:'
ws_reg['B5'] = round(best_model.rsquared, 4)
ws_reg['A6'] = 'Adjusted R-squared:'
ws_reg['B6'] = round(best_model.rsquared_adj, 4)
ws_reg['A7'] = 'F-statistic p-value:'
ws_reg['B7'] = round(best_model.f_pvalue, 4)
ws_reg['A8'] = 'AIC:'
ws_reg['B8'] = round(best_model.aic, 2)
for r in range(3, 9):
    ws_reg.cell(row=r, column=1).font = Font(bold=True)

# Coefficient table header
coef_headers = ['Variable', 'Coefficient', 'Std Error', 't-Statistic', 'P-value', '95% CI Low', '95% CI High']
for col, h in enumerate(coef_headers, 1):
    c = ws_reg.cell(row=10, column=col, value=h)
    style_header(c)
    ws_reg.column_dimensions[get_column_letter(col)].width = 16

# Coefficient rows
conf = best_model.conf_int()
for r_idx, var in enumerate(best_model.params.index, 11):
    p = best_model.pvalues[var]
    row_data = [
        var,
        round(best_model.params[var], 4),
        round(best_model.bse[var], 4),
        round(best_model.tvalues[var], 4),
        round(p, 4),
        round(conf.loc[var, 0], 4),
        round(conf.loc[var, 1], 4),
    ]
    for c_idx, val in enumerate(row_data, 1):
        cell = ws_reg.cell(row=r_idx, column=c_idx, value=val)
        cell.border = border
        if p < 0.05 and c_idx > 1:
            cell.fill = sig_fill   # highlight significant rows
    ws_reg.cell(row=r_idx, column=1).font = Font(bold=(p < 0.05))

# Legend
legend_row = 11 + len(best_model.params)
ws_reg.cell(row=legend_row + 1, column=1, value='Note: Green shading = statistically significant (p < 0.05)')
ws_reg.cell(row=legend_row + 1, column=1).font = Font(italic=True)
print("✓ Regression output sheet written")
```

- [ ] **Step 5.4: Sheet 3 — Model comparison table**

```python
ws_comp = wb.create_sheet("Model Comparison")

ws_comp.merge_cells('A1:E1')
ws_comp['A1'] = 'Model Comparison — Selection by Adjusted R²'
ws_comp['A1'].font = Font(bold=True, size=13, color="FFFFFF")
ws_comp['A1'].fill = header_fill
ws_comp['A1'].alignment = center

comp_headers = ['Model', 'Adj R²', 'R²', 'AIC', 'n']
for col, h in enumerate(comp_headers, 1):
    c = ws_comp.cell(row=3, column=col, value=h)
    style_header(c)
    ws_comp.column_dimensions[get_column_letter(col)].width = 16

for r_idx, (name, row) in enumerate(comp.iterrows(), 4):
    vals = [name, row['Adj R²'], row['R²'], row['AIC'], int(row['n'])]
    for c_idx, val in enumerate(vals, 1):
        cell = ws_comp.cell(row=r_idx, column=c_idx, value=val)
        cell.border = border
    if name == best_name:
        for c_idx in range(1, 6):
            ws_comp.cell(row=r_idx, column=c_idx).fill = sig_fill
            ws_comp.cell(row=r_idx, column=c_idx).font = Font(bold=True)

ws_comp.cell(row=r_idx + 2, column=1, value=f'★ Best model: {best_name}')
ws_comp.cell(row=r_idx + 2, column=1).font = Font(bold=True)
print("✓ Model comparison sheet written")
```

- [ ] **Step 5.5: Sheet 4 — Case question answers summary**

```python
ws_qa = wb.create_sheet("Case Question Answers")

ws_qa.merge_cells('A1:D1')
ws_qa['A1'] = 'Magic Kitchens — Case Question Answers'
ws_qa['A1'].font = Font(bold=True, size=13, color="FFFFFF")
ws_qa['A1'].fill = header_fill
ws_qa['A1'].alignment = center
ws_qa.column_dimensions['A'].width = 30
ws_qa.column_dimensions['B'].width = 20
ws_qa.column_dimensions['C'].width = 50

def qa_row(ws, row, question, value, interpretation):
    ws.cell(row=row, column=1, value=question).font = Font(bold=True)
    ws.cell(row=row, column=2, value=value)
    ws.cell(row=row, column=3, value=interpretation).alignment = Alignment(wrap_text=True)

# Q1
prom_total = (params.get('prom', 0) or 0) + (params.get('prom_lag1', 0) or 0)
adv_total  = (params.get('adv',  0) or 0) + (params.get('adv_lag1',  0) or 0)
q1_rec = "PROMOTION" if prom_total > adv_total else "ADVERTISING"
ws_qa.cell(row=3, column=1, value='Q1 Header').value  # placeholder — filled below
qa_row(ws_qa, 3,
       'Q1: Prom or Adv ($1K)?',
       f"Recommend: {q1_rec}",
       f"$1K on promotion yields ~${prom_total:.1f}K in sales (current + lag). "
       f"$1K on advertising yields ~${adv_total:.1f}K in sales (current + lag).")

qa_row(ws_qa, 5,
       'Q2: Counter-cyclical?',
       f"index coef = {params.get('index', 0):.3f} ({'sig' if pvals.get('index',1)<0.05 else 'not sig'})",
       ("CONFIRMED. Negative and significant coefficient on index: as economic conditions improve, "
        "sales DECLINE. Meat loaf is indeed a counter-cyclical product.")
       if (params.get('index', 0) < 0 and pvals.get('index', 1) < 0.05)
       else ("INCONCLUSIVE or NOT CONFIRMED. The index coefficient is not statistically significant, "
             "meaning we cannot confirm the counter-cyclical hypothesis from this data."))

any_seas_sig = any(pvals.get(q, 1) < 0.05 for q in ['Q1', 'Q2', 'Q3'])
qa_row(ws_qa, 7,
       'Q3: Seasonal effects?',
       'YES' if any_seas_sig else 'NOT CONFIRMED',
       ("Seasonal dummy variables are statistically significant, confirming seasonal patterns in sales. "
        "See regression sheet for quarter-by-quarter effects vs Q4 baseline.")
       if any_seas_sig
       else "No seasonal dummies reached significance (p < 0.05). Seasonal effects are not confirmed.")

print("✓ Case Q&A sheet written")
```

- [ ] **Step 5.6: Save the workbook**

```python
output_path = 'output/magic_kitchens_output.xlsx'
wb.save(output_path)
print(f"\n✓ Excel output saved → {output_path}")
print("  Sheets: Data | Best Model Regression | Model Comparison | Case Question Answers")
```

Run: `python3 analysis/regression.py`  
Expected: "✓ Excel output saved → output/magic_kitchens_output.xlsx" with 4 sheets.

---

## Task 6: 4-Quarter Sales Forecast

**Files:**
- Modify: `analysis/regression.py` — append after Task 5 code AND add a "Forecast" sheet to the workbook (insert before `wb.save()`)

- [ ] **Step 6.1: Build forecast inputs for next 4 quarters**

Insert this block BEFORE `wb.save()` in Task 5:

```python
# ── 6. FORECAST ───────────────────────────────────────────────────────────────
# Next 4 quarters = obs 25–28 (Q1–Q4 of next year)
# Use mean prom/adv (from historical) and mean index as baseline
mean_prom  = df['prom'].mean()
mean_adv   = df['adv'].mean()
mean_index = df['index'].mean()

# Last known prom/adv values (for lags)
last_prom = df['prom'].iloc[-1]
last_adv  = df['adv'].iloc[-1]

forecast_rows = []
for i, q_num in enumerate([1, 2, 3, 4], start=1):
    row = {
        'obs':       24 + i,
        'quarter':   f'Q{q_num} (Forecast)',
        'prom':      mean_prom,
        'adv':       mean_adv,
        'index':     mean_index,
        'prom_lag1': last_prom if i == 1 else mean_prom,
        'adv_lag1':  last_adv  if i == 1 else mean_adv,
        'Q1': int(q_num == 1),
        'Q2': int(q_num == 2),
        'Q3': int(q_num == 3),
    }
    forecast_rows.append(row)

fc_df = pd.DataFrame(forecast_rows)
```

- [ ] **Step 6.2: Generate predictions**

```python
# Build predictor matrix matching the best model
best_predictors = [v for v in best_model.params.index if v != 'const']
fc_X = sm.add_constant(fc_df[best_predictors], has_constant='add')
fc_df['forecast_sales'] = best_model.predict(fc_X)

print("\n── 4-Quarter Sales Forecast ──")
print(fc_df[['quarter', 'forecast_sales']].to_string(index=False))
```

- [ ] **Step 6.3: Write forecast sheet to workbook**

```python
ws_fc = wb.create_sheet("4-Quarter Forecast")
ws_fc.merge_cells('A1:D1')
ws_fc['A1'] = '4-Quarter Sales Forecast (Mean Spend Baseline)'
ws_fc['A1'].font  = Font(bold=True, size=13, color="FFFFFF")
ws_fc['A1'].fill  = header_fill
ws_fc['A1'].alignment = center

fc_headers = ['Quarter', 'Forecast Sales ($K)', 'Prom Used ($K)', 'Adv Used ($K)']
for col, h in enumerate(fc_headers, 1):
    c = ws_fc.cell(row=3, column=col, value=h)
    style_header(c)
    ws_fc.column_dimensions[get_column_letter(col)].width = 22

for r_idx, (_, row) in enumerate(fc_df.iterrows(), 4):
    ws_fc.cell(row=r_idx, column=1, value=row['quarter'])
    ws_fc.cell(row=r_idx, column=2, value=round(row['forecast_sales'], 2))
    ws_fc.cell(row=r_idx, column=3, value=round(row['prom'], 2))
    ws_fc.cell(row=r_idx, column=4, value=round(row['adv'], 2))
    for c_idx in range(1, 5):
        ws_fc.cell(row=r_idx, column=c_idx).border = border

ws_fc.cell(row=9, column=1, value='Note: Forecast uses historical mean spend and index as baseline.')
ws_fc.cell(row=9, column=1).font = Font(italic=True)
print("✓ Forecast sheet written")
```

Run: `python3 analysis/regression.py`  
Expected: forecast table printed to console, "✓ Forecast sheet written", final Excel has 5 sheets.

---

## Self-Review Checklist

- [x] **Spec coverage:** All 3 case questions answered (Tasks 4.1–4.3). 4 candidate models built (Task 3). Excel output generated (Task 5). 4-quarter forecast included (Task 6).
- [x] **No placeholders:** All steps contain actual Python code, no TBDs or "implement later".
- [x] **Type consistency:** `best_model`, `best_name`, `params`, `pvals`, `best_predictors` defined in Task 3 and reused correctly in Tasks 4, 5, 6.
- [x] **Data constant:** 24 observations hard-coded in Task 1 match the case study data.
- [x] **Excel save order:** `wb.save()` comes AFTER all sheet creation including forecast (Task 6 inserts before save).
