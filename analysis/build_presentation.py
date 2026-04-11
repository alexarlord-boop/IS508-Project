"""
Builds output/magic_kitchens_presentation.pptx
Run: python3 analysis/build_presentation.py
"""
import os, io, textwrap
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statsmodels.api as sm
from scipy import stats
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

# ── COLOURS ──────────────────────────────────────────────────────────────────
NAVY    = RGBColor(0x1F, 0x4E, 0x79)
BLUE    = RGBColor(0x2E, 0x75, 0xB6)
LTBLUE  = RGBColor(0xBD, 0xD7, 0xEE)
GREEN   = RGBColor(0x70, 0xAD, 0x47)
ORANGE  = RGBColor(0xED, 0x7D, 0x31)
RED     = RGBColor(0xC0, 0x00, 0x00)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
DKGREY  = RGBColor(0x40, 0x40, 0x40)
LTGREY  = RGBColor(0xF2, 0xF2, 0xF2)
YELLOW  = RGBColor(0xFF, 0xFB, 0xD5)

# ── DATA & MODELS (mirror regression.py) ─────────────────────────────────────
data = {
    'obs':   list(range(1, 25)),
    'sales': [504.72,406.59,398.55,587.76,598.92,703.62,387.24,365.67,
              388.71,372.96,603.30,614.73,484.38,227.76,329.13,308.25,
              433.86,514.98,404.70,245.43,433.20,627.24,647.61,342.81],
    'prom':  [15.6,22.2,0.0,0.0,0.0,31.8,21.3,3.9,0.0,8.4,45.3,50.1,
              39.6,4.2,0.0,0.0,0.0,13.8,17.7,0.0,17.4,37.8,42.3,11.4],
    'adv':   [30,36,45,57,39,21,12,6,6,30,30,33,6,33,6,3,45,48,0,15,9,54,36,39],
    'index': [100,102,104,104,104,100,98,96,98,103,105,107,107,107,108,105,
              103,108,110,112,113,112,113,114],
}
df = pd.DataFrame(data)
df['prom_lag1'] = df['prom'].shift(1)
df['adv_lag1']  = df['adv'].shift(1)
quarter = ((df['obs'] - 1) % 4) + 1
df['Q1'] = (quarter == 1).astype(int)
df['Q2'] = (quarter == 2).astype(int)
df['Q3'] = (quarter == 3).astype(int)

def fit(predictors):
    d = df.dropna(subset=predictors+['sales']).copy()
    return sm.OLS(d['sales'], sm.add_constant(d[predictors])).fit()

m1 = fit(['prom','adv','index'])
m2 = fit(['prom','adv','index','prom_lag1','adv_lag1'])
m3 = fit(['prom','adv','index','Q1','Q2','Q3'])
m4 = fit(['prom','adv','index','prom_lag1','adv_lag1','Q1','Q2','Q3'])
best = m4
models = {'M1\nBase':'#AEC7E8','M2\nLags':'#AEC7E8','M3\nSeasonal':'#AEC7E8','M4\nFull':'#1F4E79'}

# ── CHART HELPER ─────────────────────────────────────────────────────────────
os.makedirs('output/charts', exist_ok=True)

def save_fig(name, fig):
    path = f'output/charts/{name}.png'
    fig.savefig(path, dpi=140, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return path

# Chart 1 — Sales timeline
fig, ax = plt.subplots(figsize=(9, 3.2))
ax.plot(df['obs'], df['sales'], marker='o', linewidth=2, color='#1F4E79', markersize=5)
ax.axhline(df['sales'].mean(), color='#ED7D31', linestyle='--', linewidth=1.5,
           label=f"Mean = {df['sales'].mean():.0f}K")
ax.fill_between(df['obs'], df['sales'], df['sales'].mean(),
                where=(df['sales'] > df['sales'].mean()), alpha=0.15, color='#70AD47')
ax.fill_between(df['obs'], df['sales'], df['sales'].mean(),
                where=(df['sales'] < df['sales'].mean()), alpha=0.15, color='#C00000')
ax.set_xlabel('Quarter', fontsize=10); ax.set_ylabel('Sales ($K)', fontsize=10)
ax.set_title('24 Quarters of Sales — High Variability is the Puzzle', fontsize=11, fontweight='bold')
ax.legend(fontsize=9); ax.grid(alpha=0.3)
chart_sales = save_fig('sales_timeline', fig)

# Chart 2 — Model comparison
fig, ax = plt.subplots(figsize=(6, 3.5))
names  = ['M1 Base','M2 Lags','M3 Seasonal','M4 Full']
adj_r2 = [m1.rsquared_adj, m2.rsquared_adj, m3.rsquared_adj, m4.rsquared_adj]
colors = ['#AEC7E8','#AEC7E8','#AEC7E8','#1F4E79']
bars   = ax.bar(names, adj_r2, color=colors, edgecolor='white', width=0.55)
ax.set_ylim(0, 1.0); ax.set_ylabel('Adjusted R²', fontsize=10)
ax.set_title('Model Selection by Adjusted R²', fontsize=11, fontweight='bold')
ax.axhline(0.8, color='#70AD47', linestyle=':', linewidth=1.5, label='0.80 threshold')
ax.legend(fontsize=9)
for bar, v in zip(bars, adj_r2):
    ax.text(bar.get_x()+bar.get_width()/2, v+0.01, f'{v:.3f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.grid(alpha=0.3, axis='y')
chart_models = save_fig('model_comparison', fig)

# Chart 3 — Actual vs predicted
valid = df.dropna(subset=['prom_lag1','adv_lag1'])
actual = valid['sales'].values
fitted = best.fittedvalues.values
fig, ax = plt.subplots(figsize=(5.5, 4.5))
ax.scatter(actual, fitted, color='#1F4E79', alpha=0.75, edgecolors='white', s=70, zorder=3)
lo, hi = min(actual.min(), fitted.min())-10, max(actual.max(), fitted.max())+10
ax.plot([lo,hi],[lo,hi],'--', color='#ED7D31', linewidth=1.8, label='Perfect fit')
ax.set_xlabel('Actual Sales ($K)', fontsize=10); ax.set_ylabel('Predicted Sales ($K)', fontsize=10)
ax.set_title(f'Best Model: Actual vs Predicted\nAdj R² = {best.rsquared_adj:.3f}', fontsize=11, fontweight='bold')
ax.legend(fontsize=9); ax.grid(alpha=0.3)
chart_fit = save_fig('actual_vs_predicted', fig)

# Chart 4 — Two-quarter spend effect
bp, bpv = best.params, best.pvalues
prom_c, prom_l = bp['prom'], bp['prom_lag1']
adv_c,  adv_l  = bp['adv'],  bp['adv_lag1']
fig, axes = plt.subplots(1, 2, figsize=(8, 3.8), sharey=False)
for ax, label, vals, color in [
    (axes[0], 'Promotion ($1K spent)', [prom_c, prom_l], '#ED7D31'),
    (axes[1], 'Advertising ($1K spent)', [adv_c, adv_l], '#1F4E79'),
]:
    bar_colors = [color if v >= 0 else '#C00000' for v in vals]
    bars = ax.bar(['Q0\n(immediate)','Q1\n(next qtr)'], vals, color=bar_colors,
                  edgecolor='white', width=0.45)
    ax.axhline(0, color='black', linewidth=1.1)
    ax.set_title(label, fontsize=10, fontweight='bold')
    ax.set_ylabel('Δ Sales per $1K ($K)', fontsize=9)
    total = sum(vals)
    ax.text(0.5, 0.93, f'Net: {total:+.2f}K', transform=ax.transAxes,
            ha='center', fontsize=11, fontweight='bold', color='black',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#FFFBD5', alpha=0.95))
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x()+bar.get_width()/2, v+(0.1 if v>=0 else -0.35),
                f'{v:+.2f}', ha='center', va='bottom', fontsize=10)
    ax.grid(alpha=0.25, axis='y')
plt.suptitle('Two-Quarter Sales Impact per $1K Spent', fontsize=11, fontweight='bold')
plt.tight_layout()
chart_q1 = save_fig('q1_spend_effect', fig)

# Chart 5 — Forecast
mean_p, mean_a, mean_i = df['prom'].mean(), df['adv'].mean(), df['index'].mean()
lp, la = df['prom'].iloc[-1], df['adv'].iloc[-1]
fc_rows = [{'prom':mean_p,'adv':mean_a,'index':mean_i,
            'prom_lag1': lp if i==1 else mean_p,
            'adv_lag1':  la if i==1 else mean_a,
            'Q1':int(q==1),'Q2':int(q==2),'Q3':int(q==3)}
           for i,q in enumerate([1,2,3,4],1)]
fc_df = pd.DataFrame(fc_rows)
best_pred = [v for v in best.params.index if v!='const']
fc_X = sm.add_constant(fc_df[best_pred], has_constant='add')
fc_sales = best.predict(fc_X).values
fc_obs   = [25,26,27,28]

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.plot(df['obs'], df['sales'], marker='o', linewidth=1.8, color='#1F4E79',
        markersize=4, label='Historical')
ax.plot(fc_obs, fc_sales, marker='D', linewidth=2.2, linestyle='--',
        color='#ED7D31', markersize=7, label='Forecast (mean spend)')
ax.fill_between(fc_obs, fc_sales*0.85, fc_sales*1.15, alpha=0.15, color='#ED7D31')
ax.axvline(24.5, color='grey', linestyle=':', linewidth=1.2)
ax.set_xlabel('Quarter', fontsize=10); ax.set_ylabel('Sales ($K)', fontsize=10)
ax.set_title('4-Quarter Sales Forecast — Mean Spend Baseline', fontsize=11, fontweight='bold')
ax.legend(fontsize=9); ax.grid(alpha=0.3)
chart_fc = save_fig('forecast', fig)

print("✓ Charts saved")

# ── PPTX HELPERS ─────────────────────────────────────────────────────────────
W, H = Inches(13.33), Inches(7.5)   # 16:9 widescreen

def new_prs():
    prs = Presentation()
    prs.slide_width  = W
    prs.slide_height = H
    return prs

def blank_slide(prs):
    layout = prs.slide_layouts[6]   # completely blank
    return prs.slides.add_slide(layout)

def add_rect(slide, x, y, w, h, fill=None, line=None):
    shape = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.line.fill.background()
    if fill:
        shape.fill.solid(); shape.fill.fore_color.rgb = fill
    else:
        shape.fill.background()
    if line:
        shape.line.color.rgb = line; shape.line.width = Pt(0.75)
    else:
        shape.line.fill.background()
    return shape

def add_text(slide, text, x, y, w, h, size=18, bold=False, color=DKGREY,
             align=PP_ALIGN.LEFT, wrap=True, italic=False):
    txb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    txb.word_wrap = wrap
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = Pt(size)
    run.font.bold  = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txb

def add_bullets(slide, items, x, y, w, h, size=16, color=DKGREY, indent=False):
    txb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    txb.word_wrap = True
    tf  = txb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        if indent and item.startswith('  '):
            p.level = 1
            item = item.strip()
        run = p.add_run()
        run.text = ('• ' if not indent else ('  – ' if p.level else '• ')) + item
        run.font.size  = Pt(size)
        run.font.color.rgb = color
        run.font.bold  = item.isupper() or item.startswith('★')

def add_image(slide, path, x, y, w, h=None):
    if h:
        slide.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    else:
        slide.shapes.add_picture(path, Inches(x), Inches(y), width=Inches(w))

def section_bar(slide, label):
    """Dark left-edge accent bar + section label."""
    add_rect(slide, 0, 0, 0.18, 7.5, fill=NAVY)
    add_text(slide, label, 0.35, 0.18, 4, 0.5, size=11, color=BLUE, bold=True)

def slide_title(slide, title, subtitle=None):
    add_text(slide, title, 0.35, 0.55, 12.6, 0.75, size=28, bold=True, color=NAVY)
    if subtitle:
        add_text(slide, subtitle, 0.35, 1.22, 12.6, 0.4, size=15, color=DKGREY, italic=True)
    add_rect(slide, 0.35, 1.18, 12.6, 0.04, fill=LTBLUE)

# ── BUILD SLIDES ─────────────────────────────────────────────────────────────
prs = new_prs()

# ─── SLIDE 1: Title ───────────────────────────────────────────────────────────
sl = blank_slide(prs)
add_rect(sl, 0, 0, 13.33, 7.5, fill=NAVY)
add_rect(sl, 0.5, 1.5, 12.33, 4.5, fill=RGBColor(0x17, 0x3A, 0x5C))
add_text(sl, 'Magic Kitchens Meat Loaf Mix',
         0.8, 1.8, 11.7, 1.1, size=34, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_text(sl, 'Sales Forecast & Marketing Budget Recommendation',
         0.8, 2.8, 11.7, 0.6, size=20, color=LTBLUE, align=PP_ALIGN.CENTER)
add_rect(sl, 4.0, 3.55, 5.33, 0.05, fill=ORANGE)
add_text(sl, 'Presented by Sally Bunn · Brand Manager',
         0.8, 3.75, 11.7, 0.45, size=15, color=WHITE, align=PP_ALIGN.CENTER, italic=True)
add_text(sl, 'Group Members: Matvey Firsov  ·  Gennady Petrishchev  ·  Aleksandr Petrunin  ·  Manuel Wills',
         0.8, 4.2, 11.7, 0.4, size=13, color=LTBLUE, align=PP_ALIGN.CENTER)
add_text(sl, 'IS508 · Big Data and Analytics · April 2026',
         0.8, 5.2, 11.7, 0.4, size=13, color=RGBColor(0x8E, 0xA9, 0xC8),
         align=PP_ALIGN.CENTER)


# ─── SLIDE 2: Agenda ─────────────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, 'OVERVIEW')
slide_title(sl, 'Agenda')

items = [
    ('01', 'The Business Challenge', 'Why Sally needs a model — and why past data is confusing'),
    ('02', 'Data & Exploration',     '24 quarters, 4 variables, hidden patterns'),
    ('03', 'Methodology',            '4 regression models built, 1 selected by Adjusted R²'),
    ('04', 'Key Findings',           'What actually drives sales — and what doesn\'t'),
    ('05', 'Recommendation',         'Where to spend $1K, what to forecast, what to watch'),
]
for i, (num, heading, sub) in enumerate(items):
    y_base = 1.7 + i * 0.98
    add_rect(sl, 0.55, y_base, 0.55, 0.55, fill=NAVY)
    add_text(sl, num, 0.55, y_base+0.04, 0.55, 0.5, size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(sl, heading, 1.25, y_base+0.02, 5.5, 0.32, size=16, bold=True, color=NAVY)
    add_text(sl, sub, 1.25, y_base+0.3, 11.5, 0.32, size=12, color=DKGREY, italic=True)

# ─── SLIDE 3: The Business Challenge ─────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '01 · THE CHALLENGE')
slide_title(sl, 'The Business Challenge', 'What Sally inherited on Day 1')

add_bullets(sl, [
    'Meat loaf mix sales swing from $227K to $703K per quarter — a nearly 3× gap',
    'Company policy: EITHER promote OR advertise each quarter (never both)',
    'Long-standing internal debate: does promotion actually work, or just steal future sales?',
    'Advertising effect unclear — two similar ad spends ($36K vs $39K) produced $648K and $343K',
    'Economist claims product is counter-cyclical — sells better in recessions',
    'Possible seasonal effect — cold months may drive more purchases',
], 0.35, 1.55, 8.2, 4.5, size=16)

# Key numbers callout
for val, label, y in [
    ('$227K–$703K', 'Sales range', 1.6),
    ('85%', 'Variance explained\nby our model', 2.95),
    ('24 qtrs', 'Historical data', 4.35),
]:
    add_rect(sl, 9.0, y, 3.9, 1.0, fill=LTBLUE, line=BLUE)
    add_text(sl, val, 9.0, y+0.05, 3.9, 0.55, size=22, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_text(sl, label, 9.0, y+0.55, 3.9, 0.38, size=11, color=DKGREY, align=PP_ALIGN.CENTER)

# ─── SLIDE 4: Data Overview ───────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '02 · DATA & EXPLORATION')
slide_title(sl, 'The Data — 24 Quarters of History')

# Variable table
headers = ['Variable', 'Description', 'Mean', 'Min', 'Max']
rows = [
    ['sales',  'Quarterly sales ($K)',                f"{df['sales'].mean():.0f}K",  f"{df['sales'].min():.0f}K",  f"{df['sales'].max():.0f}K"],
    ['prom',   'Promotion spend — to brokers ($K)',   f"{df['prom'].mean():.1f}K",   '0K',                         f"{df['prom'].max():.1f}K"],
    ['adv',    'Advertising spend — to consumers ($K)',f"{df['adv'].mean():.1f}K",   '0K',                         f"{df['adv'].max():.0f}K"],
    ['index',  'Economic conditions index',           f"{df['index'].mean():.1f}",   f"{df['index'].min():.0f}",   f"{df['index'].max():.0f}"],
]

table_shape = sl.shapes.add_table(5, 5, Inches(0.35), Inches(1.55), Inches(5.8), Inches(2.2))
tbl = table_shape.table
col_widths = [1.0, 2.8, 0.7, 0.65, 0.65]
for ci, cw in enumerate(col_widths):
    tbl.columns[ci].width = Inches(cw)

for ci, h in enumerate(headers):
    cell = tbl.cell(0, ci)
    cell.text = h
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    p = cell.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.runs[0]; run.font.bold=True; run.font.size=Pt(12); run.font.color.rgb=WHITE

for ri, row in enumerate(rows, 1):
    bg = LTGREY if ri % 2 == 0 else WHITE
    for ci, val in enumerate(row):
        cell = tbl.cell(ri, ci)
        cell.text = val
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER if ci > 1 else PP_ALIGN.LEFT
        run = p.runs[0]; run.font.size = Pt(11); run.font.color.rgb = DKGREY

add_image(sl, chart_sales, x=2.35, y=3.95, w=10.6, h=3.5)

# ─── SLIDE 5: Exploratory Insight — Stockpiling ───────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '02 · DATA & EXPLORATION')
slide_title(sl, 'Key Insight: Promotion Creates a Hangover',
            'What the raw data tells us before we even run a model')

add_bullets(sl, [
    'Promotion boosts sales THIS quarter — but suppresses NEXT quarter',
    'When prior-quarter promo > $20K → next quarter median sales DROP ~$80K',
    'Brokers stockpile inventory during deals, then don\'t reorder until stock clears',
    '→ This is why we must test lagged (delayed) effects in the model',
], 0.35, 1.55, 12.6, 2.2, size=16)

# Inline mini chart — prom vs prom_lag1 effect
fig2, axes2 = plt.subplots(1, 2, figsize=(9, 2.8))
high = df[df['prom_lag1'] > 20]['sales'].dropna()
low  = df[df['prom_lag1'] <= 20]['sales'].dropna()
axes2[0].boxplot([low, high], labels=['Low prior\npromo ≤$20K', 'High prior\npromo >$20K'],
                  patch_artist=True,
                  boxprops=dict(facecolor='#BDD7EE'),
                  medianprops=dict(color='#1F4E79', linewidth=2))
axes2[0].set_ylabel('Sales this quarter ($K)', fontsize=9)
axes2[0].set_title('Sales after High vs Low Promo Quarter', fontsize=9, fontweight='bold')
axes2[0].grid(alpha=0.3)

valid = df.dropna(subset=['prom_lag1'])
m_s, b_s, r_s, p_s, _ = stats.linregress(valid['prom_lag1'], valid['sales'])
xline = np.linspace(valid['prom_lag1'].min(), valid['prom_lag1'].max(), 100)
axes2[1].scatter(valid['prom_lag1'], valid['sales'], color='#ED7D31', alpha=0.7,
                 edgecolors='white', s=50)
axes2[1].plot(xline, m_s*xline+b_s, 'k--', linewidth=1.5)
axes2[1].set_xlabel('Prior-Qtr Promo ($K)', fontsize=9)
axes2[1].set_ylabel('Current Sales ($K)', fontsize=9)
axes2[1].set_title(f'Lag-1 Promo → Sales (r={r_s:.2f})', fontsize=9, fontweight='bold')
axes2[1].grid(alpha=0.3)
plt.tight_layout()
chart_stock = save_fig('stockpiling', fig2)
add_image(sl, chart_stock, x=0.35, y=3.75, w=12.6, h=3.5)

# ─── SLIDE 6: Methodology ────────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '03 · METHODOLOGY')
slide_title(sl, 'Model Building — Progressive Complexity',
            'We built 4 OLS regression models, selecting by Adjusted R²')

model_info = [
    ('M1', 'Base',     'prom + adv + index',                    m1.rsquared_adj, '✗ Missing lag effects'),
    ('M2', 'Lags',     '+ prom_lag₁ + adv_lag₁',               m2.rsquared_adj, '✗ Missing seasons'),
    ('M3', 'Seasonal', '+ Q1/Q2/Q3 dummies',                    m3.rsquared_adj, '✗ Missing lags'),
    ('M4', 'Full ★',   'All of the above  ← BEST',              m4.rsquared_adj, '✓ All effects tested'),
]
for i, (code_, name, vars_, adj, note) in enumerate(model_info):
    y = 1.6 + i * 1.18
    is_best = code_ == 'M4'
    bg = LTBLUE if is_best else LTGREY
    border = BLUE if is_best else RGBColor(0xCC, 0xCC, 0xCC)
    add_rect(sl, 0.35, y, 12.5, 1.02, fill=bg, line=border)
    add_text(sl, code_, 0.45, y+0.07, 0.7, 0.5, size=20, bold=True, color=NAVY)
    add_text(sl, name,  1.15, y+0.07, 1.8, 0.4, size=15, bold=is_best, color=NAVY)
    add_text(sl, vars_, 2.95, y+0.07, 6.0, 0.4, size=13, color=DKGREY, italic=True)
    add_text(sl, f'Adj R² = {adj:.3f}', 9.1, y+0.07, 2.0, 0.4, size=14, bold=True,
             color=NAVY if is_best else DKGREY)
    add_text(sl, note, 2.95, y+0.52, 9.1, 0.38, size=11, color=DKGREY)

add_text(sl, '★ Winner: M4 Full — Adj R² = 0.850  (explains 85% of sales variance)',
         0.35, 6.45, 12.6, 0.4, size=13, bold=True, color=NAVY)

# ─── SLIDE 7: Model Fit ───────────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '03 · METHODOLOGY')
slide_title(sl, 'Best Model Performance — M4 Full',
            f'Adj R² = {best.rsquared_adj:.3f} · n = {int(best.nobs)} quarters · AIC = {best.aic:.0f}')

add_image(sl, chart_models, x=0.35, y=1.5, w=6.1, h=3.6)
add_image(sl, chart_fit,    x=6.8,  y=1.4, w=6.2, h=4.4)

add_bullets(sl, [
    f'RMSE: ${np.sqrt(np.mean(best.resid**2)):.1f}K  (avg forecast error)',
    'Residuals are well-behaved — no systematic pattern',
    'No multicollinearity detected (max |r| = 0.46 between predictors)',
], 0.35, 5.35, 12.6, 1.6, size=14)

# ─── SLIDE 8: Q1 — Advertising vs Promotion ──────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '04 · KEY FINDINGS')
slide_title(sl, 'Q1: Where Should Sally Spend $1,000?',
            'Answer: Advertising yields a higher net sales return')

add_image(sl, chart_q1, x=0.35, y=1.5, w=7.8, h=4.4)

add_rect(sl, 8.5, 1.55, 4.5, 1.15, fill=LTGREY, line=RGBColor(0xCC,0xCC,0xCC))
add_text(sl, 'Promotion — Net Effect',  8.6, 1.6,  4.2, 0.32, size=12, color=DKGREY, bold=True)
add_text(sl, f'+{bp["prom"]:.2f}K  −{abs(bp["prom_lag1"]):.2f}K  =  +{bp["prom"]+bp["prom_lag1"]:.2f}K net',
         8.6, 1.9, 4.2, 0.32, size=12, color=ORANGE, bold=True)

add_rect(sl, 8.5, 2.9, 4.5, 1.15, fill=LTBLUE, line=BLUE)
add_text(sl, 'Advertising — Net Effect', 8.6, 2.95, 4.2, 0.32, size=12, color=DKGREY, bold=True)
add_text(sl, f'+{bp["adv"]:.2f}K  +{bp["adv_lag1"]:.2f}K  =  +{bp["adv"]+bp["adv_lag1"]:.2f}K net',
         8.6, 3.25, 4.2, 0.32, size=12, color=NAVY, bold=True)

add_bullets(sl, [
    'Promotion boosts sales NOW (+$6.51K) but creates a hangover',
    'Lagged promo is negative (−$3.41K): brokers stockpile, then go quiet',
    'Advertising compounds: +$2.64K now AND +$2.78K next quarter',
    '★ Sally should ADVERTISE — net return is $5.41K vs $3.10K',
], 8.5, 4.3, 4.6, 2.8, size=12)

# ─── SLIDE 9: Q2 — Counter-cyclical ──────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '04 · KEY FINDINGS')
slide_title(sl, 'Q2: Is Meat Loaf Counter-Cyclical?',
            'The economist\'s theory is plausible — but just misses statistical confirmation')

idx_c  = best.params['index']
idx_p  = best.pvalues['index']
idx_t  = best.tvalues['index']
idx_ci = best.conf_int().loc['index']

# Inline chart
fig3, ax3 = plt.subplots(figsize=(6, 3.6))
ax3.scatter(df['index'], df['sales'], color='#1F4E79', alpha=0.7, edgecolors='white', s=60)
m3_, b3_, r3_, p3_, _ = stats.linregress(df['index'], df['sales'])
xline3 = np.linspace(df['index'].min(), df['index'].max(), 100)
ax3.plot(xline3, m3_*xline3+b3_, 'k--', linewidth=1.5, label=f'Slope={m3_:.1f}  r={r3_:.2f}')
ax3.set_xlabel('Economic Index (higher = better times)', fontsize=10)
ax3.set_ylabel('Sales ($K)', fontsize=10)
ax3.set_title('Sales vs Economic Conditions Index', fontsize=10, fontweight='bold')
ax3.legend(fontsize=9); ax3.grid(alpha=0.3)
plt.tight_layout()
chart_idx = save_fig('index_scatter', fig3)
add_image(sl, chart_idx, x=0.35, y=1.55, w=6.8, h=4.0)

# Stats box
for label, val, y_pos in [
    ('Coefficient (index)', f'{idx_c:.3f}', 1.65),
    ('t-statistic',          f'{idx_t:.2f}',  2.45),
    ('p-value',              f'{idx_p:.4f}',  3.25),
    ('95% CI',               f'[{idx_ci[0]:.2f}, {idx_ci[1]:.2f}]', 4.05),
]:
    add_rect(sl, 7.5, y_pos, 5.4, 0.65, fill=LTGREY, line=RGBColor(0xCC,0xCC,0xCC))
    add_text(sl, label, 7.6, y_pos+0.06, 2.8, 0.32, size=12, color=DKGREY)
    add_text(sl, val, 10.3, y_pos+0.06, 2.5, 0.32, size=14, bold=True, color=NAVY, align=PP_ALIGN.RIGHT)

add_rect(sl, 7.5, 5.1, 5.4, 1.1, fill=YELLOW, line=ORANGE)
add_bullets(sl, [
    'Coefficient is NEGATIVE (−4.92): ✓ correct direction',
    'p = 0.053 — misses 5% threshold by a whisker',
    'Verdict: Suggestive, not conclusive',
    'Watch economic conditions; cold winters may help',
], 7.6, 5.1, 5.2, 1.1, size=11)

# ─── SLIDE 10: Q3 — Seasonal Effects ─────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '04 · KEY FINDINGS')
slide_title(sl, 'Q3: Are There Seasonal Effects?',
            'No season significantly outperforms another — after controlling for spend')

# Seasonal bar chart (inline)
q_names  = ['Q1\n(Winter)','Q2\n(Spring)','Q3\n(Summer)','Q4\n(Autumn)\n[baseline]']
q_coefs  = [best.params.get('Q1',0), best.params.get('Q2',0), best.params.get('Q3',0), 0]
q_pvals  = [best.pvalues.get('Q1',1), best.pvalues.get('Q2',1), best.pvalues.get('Q3',1), 1]
q_colors = ['#1F4E79' if pp<0.05 else ('#AEC7E8' if pp<0.10 else '#D9D9D9') for pp in q_pvals]

fig4, ax4 = plt.subplots(figsize=(6.5, 3.8))
bars4 = ax4.bar(q_names, q_coefs, color=q_colors, edgecolor='white', width=0.5)
ax4.axhline(0, color='black', linewidth=1.2)
ax4.set_ylabel('Sales vs Q4 baseline ($K)', fontsize=10)
ax4.set_title('Seasonal Dummy Coefficients (vs Q4 Autumn baseline)', fontsize=10, fontweight='bold')
for bar, v, pp in zip(bars4, q_coefs, q_pvals):
    ax4.text(bar.get_x()+bar.get_width()/2, v+(3 if v>=0 else -12),
             f'{v:+.0f}K\np={pp:.2f}', ha='center', fontsize=8)
ax4.grid(alpha=0.3, axis='y')
plt.tight_layout()
chart_seas = save_fig('seasonal', fig4)
add_image(sl, chart_seas, x=0.35, y=1.55, w=7.0, h=4.2)

add_bullets(sl, [
    'Q1 (Winter): +20K vs Q4 — not significant (p=0.54)',
    'Q2 (Spring): −61K vs Q4 — marginal (p=0.09)',
    'Q3 (Summer): −53K vs Q4 — not significant (p=0.14)',
    '',
    'After controlling for spend & economy,',
    'seasons cannot be confirmed statistically',
    '(24 quarters may be too few to isolate)',
    '',
    '→ Do NOT plan seasonal budget shifts yet',
    '→ Re-evaluate with more data',
], 7.6, 1.55, 5.4, 5.5, size=13)

# ─── SLIDE 11: Forecast ───────────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '04 · KEY FINDINGS')
slide_title(sl, '4-Quarter Sales Forecast',
            'Based on M4 Full model — historical mean spend as baseline')

add_image(sl, chart_fc, x=0.35, y=1.5, w=8.5, h=3.5)

# Forecast table
fc_labels = ['Q1 (Year 7)','Q2 (Year 7)','Q3 (Year 7)','Q4 (Year 7)','Annual Total']
fc_vals   = list(np.round(fc_sales, 1)) + [round(fc_sales.sum(), 1)]

table2 = sl.shapes.add_table(6, 2, Inches(9.2), Inches(1.55), Inches(3.9), Inches(2.6))
t2 = table2.table
t2.columns[0].width = Inches(2.3)
t2.columns[1].width = Inches(1.6)

for ci, h in enumerate(['Quarter', 'Forecast ($K)']):
    cell = t2.cell(0, ci)
    cell.text = h
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    run = p.runs[0]; run.font.bold=True; run.font.size=Pt(11); run.font.color.rgb=WHITE

for ri, (lbl, val) in enumerate(zip(fc_labels, fc_vals), 1):
    is_total = ri == 5
    bg = LTBLUE if is_total else (LTGREY if ri%2==0 else WHITE)
    for ci, txt in enumerate([lbl, f'${val:.1f}K']):
        cell = t2.cell(ri, ci)
        cell.text = txt
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        run = p.runs[0]; run.font.size=Pt(11); run.font.bold=is_total
        run.font.color.rgb = NAVY if is_total else DKGREY

add_bullets(sl, [
    f'Annual forecast: ${fc_sales.sum():.0f}K  (mean-spend baseline)',
    'To maximise: shift spend toward advertising',
    'Monitor economic index — weak economy may boost sales',
], 0.35, 5.2, 12.6, 1.8, size=14)

# ─── SLIDE 12: Recommendation ────────────────────────────────────────────────
sl = blank_slide(prs)
section_bar(sl, '05 · RECOMMENDATION')
slide_title(sl, 'Sally\'s Action Plan',
            'Three evidence-based decisions for the coming year')

recs = [
    ('', 'Shift budget toward Advertising',
     ['Advertising net effect: +$5.41K per $1K — nearly 2× promotion',
      'Eliminate or reduce promotion-heavy quarters',
      'Use promotion sparingly (max 1–2 quarters) to avoid stockpiling hangover']),
    ('', 'Monitor economic conditions',
     ['Index coefficient is negative: bad times → more meat loaf sold',
      'Keep a recession-ready plan; this product may be a safe harbour',
      'Re-test counter-cyclicality as more data accumulates']),
    ('', 'Do not yet plan by season',
     ['Seasonal patterns are unconfirmed at 5% significance',
      'Collect 2 more years of data before allocating seasonal budgets',
      'Track Q2 (spring) — shows the largest (if marginal) negative effect']),
]
for i, (icon, heading, bullets) in enumerate(recs):
    y = 1.7 + i * 1.65
    add_rect(sl, 0.35, y, 12.5, 1.5, fill=LTBLUE if i==0 else LTGREY,
             line=BLUE if i==0 else RGBColor(0xCC,0xCC,0xCC))
    add_text(sl, icon,    0.45, y+0.25, 0.7, 0.7, size=22, align=PP_ALIGN.CENTER)
    add_text(sl, heading, 1.2, y+0.1,  4.5, 0.45, size=15, bold=True, color=NAVY)
    for j, b in enumerate(bullets):
        add_text(sl, '→ ' + b, 1.2, y + 0.52 + j*0.3, 11.3, 0.3, size=11, color=DKGREY)

# ─── SLIDE 13 (LAST): Excel Model Output ─────────────────────────────────────
sl = blank_slide(prs)
add_rect(sl, 0, 0, 13.33, 0.6, fill=NAVY)
add_text(sl, 'OLS Regression Output — Best Model: M4 Full (Adj R² = 0.850)',
         0.2, 0.07, 12.9, 0.45, size=14, bold=True, color=WHITE)

# Model-level stats row
stats_items = [
    ('Dependent Variable', 'Sales ($K)'),
    ('Observations', str(int(best.nobs))),
    ('R-squared', f'{best.rsquared:.4f}'),
    ('Adjusted R-squared', f'{best.rsquared_adj:.4f}'),
    ('F-stat p-value', f'{best.f_pvalue:.4f}'),
    ('AIC', f'{best.aic:.2f}'),
    ('RMSE', f'${np.sqrt(np.mean(best.resid**2)):.1f}K'),
]
x_step = 13.0 / len(stats_items)
for i, (lbl, val) in enumerate(stats_items):
    x = 0.18 + i * x_step
    add_rect(sl, x, 0.62, x_step-0.05, 0.52, fill=LTBLUE, line=BLUE)
    add_text(sl, lbl, x+0.02, 0.64, x_step-0.07, 0.2, size=8, color=DKGREY, align=PP_ALIGN.CENTER)
    add_text(sl, val, x+0.02, 0.82, x_step-0.07, 0.24, size=11, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

# Full coefficient table
conf = best.conf_int()
col_labels = ['Variable','Coefficient','Std Error','t-Stat','P-value','[95% CI Low','95% CI High]','Significant?']
col_w      = [1.6, 1.35, 1.1, 1.0, 0.95, 1.2, 1.25, 1.2]
table3 = sl.shapes.add_table(
    len(best.params)+1, len(col_labels),
    Inches(0.18), Inches(1.2),
    Inches(sum(col_w)), Inches(5.9)
)
t3 = table3.table
for ci, cw in enumerate(col_w):
    t3.columns[ci].width = Inches(cw)

for ci, h in enumerate(col_labels):
    cell = t3.cell(0, ci)
    cell.text = h
    cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
    p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    run = p.runs[0]; run.font.bold=True; run.font.size=Pt(11); run.font.color.rgb=WHITE

for ri, var in enumerate(best.params.index, 1):
    pval = best.pvalues[var]
    sig  = pval < 0.05
    bg   = RGBColor(0xE2,0xEF,0xDA) if sig else (LTGREY if ri%2==0 else WHITE)
    row_data = [
        var,
        f'{best.params[var]:.4f}',
        f'{best.bse[var]:.4f}',
        f'{best.tvalues[var]:.3f}',
        f'{pval:.4f}',
        f'{conf.loc[var,0]:.4f}',
        f'{conf.loc[var,1]:.4f}',
        '✓ Yes' if sig else 'No',
    ]
    for ci, val in enumerate(row_data):
        cell = t3.cell(ri, ci)
        cell.text = val
        cell.fill.solid(); cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT
        run = p.runs[0]
        run.font.size  = Pt(11)
        run.font.bold  = sig
        run.font.color.rgb = RGBColor(0x37,0x5E,0x23) if (sig and ci>0) else DKGREY

add_text(sl, 'Note: Green = statistically significant (p < 0.05). '
             'Lagged variables use n=23 (one observation lost to lag).',
         0.18, 7.12, 12.9, 0.28, size=9, color=DKGREY, italic=True)

# ── SAVE ────────────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)
out = 'output/magic_kitchens_presentation.pptx'
prs.save(out)
print(f"\n✓ Presentation saved → {out}")
print(f"  Slides: {len(prs.slides)}  (last slide = Excel regression output)")
