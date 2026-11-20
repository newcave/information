"""페이지 2 — AI 과학자는 K-문샷 12대 국가 미션."""
import plotly.graph_objects as go
import streamlit as st

import content as C
from common import html

# ── HERO ──
kpis = "".join(f'<div class="kpi"><b>{v}</b><span>{d}</span></div>' for v, d in C.AI_KPIS)
html(f"""
<div class="hero">
  <div class="eyebrow">{C.AI_HERO['eyebrow']}</div>
  <div class="h1">{C.AI_HERO['title']}</div>
  <div class="lead">{C.AI_HERO['lead']}</div>
  <div class="kpis">{kpis}</div>
</div>
""")

# ── 12대 미션 ──
cells = "".join(
    f'<div class="ms{" on" if m == "AI 과학자" else ""}"><small>M{i + 1:02d}</small>{m}</div>'
    for i, m in enumerate(C.AI_MISSIONS)
)
html(f"""
<div class="sec"><div class="no">01 · MISSION</div>
<div class="t">K-문샷 12대 국가 미션 — AI 과학자는 그 자체가 미션</div>
<div class="d">다른 11개 미션(신약·핵융합·소재 등)을 가속하는 공통 엔진이기도 합니다.</div></div>
<div class="missions">{cells}</div>
""")

# ── 예산 ──
html("""
<div class="sec"><div class="no">02 · BUDGET</div>
<div class="t">예산 — 규모와 증가 속도 모두 최상위</div></div>
""")
left, right = st.columns([1, 1.6], gap="large")
with left:
    html('<div class="ctitle">과기정통부 AI 예산</div><div class="csub">단위: 조원</div>')
    t = C.AI_BUDGET_TREND
    fig = go.Figure(go.Bar(
        x=t["years"], y=t["values"], width=0.55,
        marker=dict(color=["#5B7088", "#1D5FB0", "#2A78D6"], cornerradius=4,
                    pattern=dict(shape=["", "", "/"], fgcolor="#FFFFFF", size=7, solidity=.25)),
        text=[f"{v}조" for v in t["values"]], textposition="outside", cliponaxis=False,
        textfont=dict(size=14, color="#0B1F33"),
        hovertemplate="%{x}: %{y}조원<extra></extra>",
    ))
    fig.update_layout(
        height=300, margin=dict(l=8, r=8, t=28, b=8), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Pretendard, Apple SD Gothic Neo, Malgun Gothic, Noto Sans CJK KR, sans-serif", color="#46566A"),
        showlegend=False, xaxis=dict(type="category", showgrid=False, linecolor="#CBD5E1"),
        yaxis=dict(gridcolor="#EEF2F7", zeroline=False, range=[0, 11], ticksuffix="조"),
        hoverlabel=dict(bgcolor="#0B2545", font_color="#FFFFFF", bordercolor="#0B2545"),
    )
    st.plotly_chart(fig, config={"displayModeBar": False}, width="stretch")
    html('<div class="cap">2년 만에 약 6배. 2027(안)은 국회 심의 중.</div>')
with right:
    cards = "".join(
        f'<div class="bd {b["kind"]}"><span class="tag {b["kind"]}">{C.AI_KIND_LABEL[b["kind"]]}</span>'
        f'<div class="a">{b["amt"]}</div><div class="n">{b["name"]}</div><div class="x">{b["note"]}</div></div>'
        for b in C.AI_BUDGETS
    )
    html(f'<div class="budgets">{cards}</div>')

# ── 로드맵 ──
steps = "".join(
    f'<div class="rs"><div class="y">{y}</div><div class="dot"></div><div class="t">{t}</div><div class="s">{s}</div></div>'
    for y, t, s in C.AI_ROADMAP
)
html(f"""
<div class="sec"><div class="no">03 · ROADMAP</div>
<div class="t">AI 연구동료 → 연구소장급 AI 과학자</div></div>
<div class="panel" style="padding:18px 12px 20px"><div class="road">{steps}</div></div>
""")

# ── K-water 의미 ──
asks = "".join(
    f'<div class="ask"><div class="n">POINT {i + 1:02d}</div><div class="t">{t}</div><div class="d">{d}</div></div>'
    for i, (t, d) in enumerate(C.AI_MEANING)
)
html(f"""
<div class="sec"><div class="no">04 · FOR K-WATER</div>
<div class="t">K-water에 주는 의미</div></div>
<div class="asks">{asks}</div>
<div class="disc">{C.AI_NOTE}</div>
""")

st.write("")
with st.expander("출처 · 근거 자료"):
    st.markdown("\n".join(f"- [{t}]({u})" for t, u in C.AI_SOURCES))

html(f'<div class="foot"><span>K-water연구원 AI연구소 · Water Co-Scientist</span><span>업데이트 {C.UPDATED}</span></div>')
