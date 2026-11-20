"""페이지 4 — 4인 협업 실행안 (과제 상세 · 연계 R&D · 충남 테스트베드 · 이상은·김성훈 스토리)."""
import plotly.graph_objects as go
import streamlit as st

import content as C
from common import html

P = {p["key"]: p for p in C.TEAM}
FONT = "Pretendard, Apple SD Gothic Neo, Malgun Gothic, Noto Sans CJK KR, sans-serif"
LAYOUT = dict(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(family=FONT, color="#46566A"),
              hoverlabel=dict(bgcolor="#0B2545", font_color="#FFFFFF", bordercolor="#0B2545"))
CFG = {"displayModeBar": False}

# ── HERO ──
total = sum(p["y"] * (p["e"] - p["s"]) for p in C.PLAN_PROJECTS)
kpis = [
    ("5개 과제", "4인 주관·참여<br>2027–2030"),
    (f"≈ {total:.0f}억", "총 사업비 추정<br>(연간 추정 × 기간)"),
    (f"{len(C.PLAN_PROGRAMS)}개 사업", "연계 가능한<br>R&D·공모"),
    ("3,664억", "2025.7 충남 집중호우<br>닷새 피해액"),
]
html(f"""
<div class="hero">
  <div class="eyebrow">{C.PLAN_HERO['eyebrow']}</div>
  <div class="h1">{C.PLAN_HERO['title']}</div>
  <div class="lead">{C.PLAN_HERO['lead']}</div>
  <div class="kpis">{''.join(f'<div class="kpi"><b>{v}</b><span>{d}</span></div>' for v, d in kpis)}</div>
</div>
""")
st.write("")

t1, t2, t3, t4 = st.tabs(["① 과제 상세", "② 연계 R&D·공모", "③ 충남 테스트베드", "④ 이상은·김성훈 스토리"])

# ───────────── ① 과제 상세 ─────────────
with t1:
    html('<div class="ctitle" style="margin-top:8px">추진 일정 · 연간 예산(추정)</div>'
         '<div class="csub">막대 색 = 주관자 · 막대 오른쪽 숫자 = 연간 추정 예산</div>')
    projs = list(reversed(C.PLAN_PROJECTS))
    fig = go.Figure(go.Bar(
        y=[p["t"] for p in projs], x=[p["e"] - p["s"] for p in projs], base=[p["s"] for p in projs],
        orientation="h", width=0.5,
        marker=dict(color=[P[p["lead"][0]]["color"] for p in projs], cornerradius=4),
        text=[f"연 {p['y']}억" for p in projs], textposition="outside", cliponaxis=False,
        textfont=dict(size=12, color="#0B1F33"),
        customdata=[[" · ".join(P[k]["name"] for k in p["lead"]), p["y"], p["y"] * (p["e"] - p["s"])] for p in projs],
        hovertemplate="<b>%{y}</b><br>주관 %{customdata[0]}<br>연 %{customdata[1]}억 · 총 ≈%{customdata[2]:.0f}억<extra></extra>",
    ))
    fig.update_layout(height=320, margin=dict(l=8, r=60, t=8, b=8), showlegend=False,
                      xaxis=dict(range=[2026.9, 2031.4], dtick=1, gridcolor="#EEF2F7", zeroline=False),
                      yaxis=dict(tickfont=dict(size=13, color="#0B1F33")), **LAYOUT)
    st.plotly_chart(fig, config=CFG, width="stretch")

    cards = []
    for p in C.PLAN_PROJECTS:
        lead = "".join(f'<span class="lead" style="--c:{P[k]["color"]}">{P[k]["name"]} · 주관</span>' for k in p["lead"])
        tot = p["y"] * (p["e"] - p["s"])
        cards.append(
            f'<div class="pj"><div class="t">{p["t"]}<span class="tag est" style="float:right">연 {p["y"]}억 · 총 ≈{tot:.0f}억</span></div>'
            f'<dl class="hist" style="grid-template-columns:44px 1fr"><dt>목표</dt><dd>{p["goal"]}</dd>'
            f'<dt>산출</dt><dd>{p["out"]}</dd><dt>연계</dt><dd>{p["link"]}</dd></dl>'
            f'<div class="who">{lead}</div></div>'
        )
    html(f'<div class="projects" style="margin-top:6px">{"".join(cards)}</div>'
         '<div class="disc">※ 예산은 유사 규모 R&D를 참고한 추정치(초안)입니다. 실제 공모 규모에 맞춰 조정하세요.</div>')

# ───────────── ② 연계 R&D·공모 ─────────────
with t2:
    progs = []
    for g in C.PLAN_PROGRAMS:
        progs.append(
            f'<div class="bd {"est" if g["status"] == "open" else ""}"><span class="tag {"est" if g["status"] == "open" else ""}">'
            f'{C.PLAN_STATUS[g["status"]]}</span><div class="n" style="margin-top:0;font-size:16px">{g["n"]}</div>'
            f'<div class="x">{g["who"]} · {g["when"]}</div><div class="a" style="font-size:18px;margin-top:8px">{g["amt"]}</div>'
            f'<div class="x" style="color:#0B1F33;margin-top:6px">→ {g["fit"]}</div>'
            f'<div class="x" style="margin-top:6px"><a href="{g["src"]}" target="_blank">근거 보기</a></div></div>'
        )
    html(f'<div class="budgets" style="margin-top:8px">{"".join(progs)}</div>'
         '<div class="disc">※ 점선 카드 = 공모·접수 일정이 잡힌 사업. 일정·규모는 공고문으로 재확인 필요.</div>')

# ───────────── ③ 충남 테스트베드 ─────────────
with t3:
    lk = "".join(f'<div class="lk"><b>{v}</b><span>{d}</span></div>' for v, d in C.PLAN_TB_KPIS)
    html(f'<div class="lks">{lk}</div>')
    left, right = st.columns([1.3, 1], gap="large")
    with left:
        html('<div class="ctitle">후보지 지도</div><div class="csub">개략 위치도 · 원 크기 = 2025.7 농작물 침수면적 · 사각형 = 4인 소속기관</div>')
        sites = C.PLAN_SITES
        # 외부 지도 타일 없이도 항상 보이도록 위경도 좌표평면에 개략 위치도로 표시
        m = go.Figure()
        m.add_trace(go.Scatter(
            x=[s["lon"] for s in sites], y=[s["lat"] for s in sites], mode="markers+text",
            marker=dict(size=[(s["farm"] or 900) ** 0.5 / 2.0 + 10 for s in sites], color="rgba(42,120,214,.55)",
                        line=dict(color="#2A78D6", width=2)),
            text=[s["n"] for s in sites], textposition="top center", textfont=dict(size=13, color="#0B1F33"),
            customdata=[[s["note"], f'{s["farm"]:,}ha' if s["farm"] else "—", f'{s["rain"]}mm' if s["rain"] else "—"] for s in sites],
            hovertemplate="<b>%{text}</b><br>%{customdata[0]}<br>농작물 침수 %{customdata[1]} · 강수 %{customdata[2]}<extra></extra>",
            cliponaxis=False,
        ))
        orgs = C.PLAN_ORGS
        m.add_trace(go.Scatter(
            x=[o["lon"] for o in orgs], y=[o["lat"] for o in orgs], mode="markers+text",
            marker=dict(size=13, color="#0B2545", symbol="square"),
            text=[o["n"] for o in orgs], textposition="bottom center", textfont=dict(size=12, color="#0B2545"),
            hovertemplate="%{text}<extra></extra>", cliponaxis=False,
        ))
        m.add_annotation(x=126.32, y=36.30, text="서해", showarrow=False, font=dict(size=14, color="#9AA8B8"))
        m.update_layout(height=440, margin=dict(l=8, r=8, t=8, b=8), showlegend=False,
                        xaxis=dict(range=[126.25, 127.55], showgrid=True, gridcolor="#EEF2F7", zeroline=False,
                                   ticksuffix="°E", tickfont=dict(size=10)),
                        yaxis=dict(range=[36.15, 37.0], showgrid=True, gridcolor="#EEF2F7", zeroline=False,
                                   ticksuffix="°N", tickfont=dict(size=10), scaleanchor="x", scaleratio=1.25),
                        **LAYOUT)
        st.plotly_chart(m, config=CFG, width="stretch")
    with right:
        html('<div class="ctitle">2025.7 농작물 침수면적</div><div class="csub">단위: ha · 7.16–18 호우</div>')
        farm = sorted([s for s in sites if s["farm"]], key=lambda s: s["farm"])
        b = go.Figure(go.Bar(
            y=[s["n"] for s in farm], x=[s["farm"] for s in farm], orientation="h", width=0.55,
            marker=dict(color="#2A78D6", cornerradius=4), text=[f'{s["farm"]:,}' for s in farm],
            textposition="outside", cliponaxis=False, textfont=dict(size=12, color="#0B1F33"),
            hovertemplate="%{y}: %{x:,}ha<extra></extra>",
        ))
        b.update_layout(height=230, margin=dict(l=8, r=50, t=8, b=8), showlegend=False,
                        xaxis=dict(gridcolor="#EEF2F7", zeroline=False, range=[0, 7400]),
                        yaxis=dict(tickfont=dict(size=13, color="#0B1F33")), **LAYOUT)
        st.plotly_chart(b, config=CFG, width="stretch")
        html('<div class="ans" style="font-size:14px">추천: <b>당진·서산</b> (피해 최대, 서해안 극한호우) 또는 '
             '<b>천안</b> (2026 물순환 촉진구역 지정 — 계획 수립과 바로 연동)</div>')
    html('<div class="disc">※ 지도 좌표는 시청·군청 부근 개략 위치입니다.</div>')

# ───────────── ④ 이상은·김성훈 스토리 ─────────────
with t4:
    rows = []
    for y, who, what, chk in C.PLAN_STORY:
        cls = "both" if "·" in who else ("bg" if who == "공통 배경" else "")
        rows.append(f'<div class="st-row {cls}"><div class="st-y">{y}</div><div class="st-dot"></div>'
                    f'<div class="st-c"><div class="st-w">{who}</div><div class="st-t">{what}'
                    f'{"<span class=chk>확인 필요</span>" if chk else ""}</div></div></div>')
    html(f'<div class="story">{"".join(rows)}</div>'
         f'<div class="ans" style="margin-top:16px">{C.PLAN_STORY_PUNCH}</div>'
         '<div class="disc">※ 2015 인용의 ‘김성훈’이 동일 인물인지 확인 후 표시를 정리하세요.</div>')

st.write("")
with st.expander("출처 · 근거 자료"):
    st.markdown("\n".join(f"- [{t}]({u})" for t, u in C.PLAN_SOURCES))
html(f'<div class="foot"><span>K-water연구원 AI연구소 · Water Co-Scientist</span><span>업데이트 {C.UPDATED}</span></div>')
