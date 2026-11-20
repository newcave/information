"""페이지 3 — 4인 협업 구상 (초안). 문구·점수·이력은 content.py 의 TEAM_* 에서 수정."""
from html import escape

import plotly.graph_objects as go
import streamlit as st

import content as C
from common import html

P = {p["key"]: p for p in C.TEAM}
FONT = "Pretendard, Apple SD Gothic Neo, Malgun Gothic, Noto Sans CJK KR, sans-serif"

# ── HERO ──
kpis = "".join(f'<div class="kpi"><b>{v}</b><span>{d}</span></div>' for v, d in C.TEAM_KPIS)
html(f"""
<div class="hero">
  <div class="eyebrow">{C.TEAM_HERO['eyebrow']}</div>
  <div class="h1">{C.TEAM_HERO['title']}</div>
  <div class="lead">{C.TEAM_HERO['lead']}</div>
  <div class="kpis">{kpis}</div>
</div>
""")


# ── 01 협업 그림 ──
def team_svg() -> str:
    W, H = 1000, 490
    hx, hy = 500, 245
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="네 사람과 공동 테스트베드를 잇는 협업 구조">']
    # 허브 연결
    for p in C.TEAM:
        x, y = p["pos"]
        out.append(f'<line x1="{hx}" y1="{hy}" x2="{x}" y2="{y}" stroke="{p["color"]}" stroke-width="2" stroke-dasharray="5 6" opacity=".7"/>')
    # 사람 간 연결 + 라벨
    for a, b, label in C.TEAM_LINKS:
        (x1, y1), (x2, y2) = P[a]["pos"], P[b]["pos"]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#C9D3DF" stroke-width="2.5"/>')
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        w = 22 + len(label) * 12.2
        out.append(f'<rect x="{mx - w / 2}" y="{my - 14}" width="{w}" height="28" rx="14" fill="#fff" stroke="#E2E8F0"/>')
        out.append(f'<text x="{mx}" y="{my + 4.5}" text-anchor="middle" font-size="13" font-weight="700" fill="#0B1F33">{escape(label)}</text>')
    # 허브
    out.append(f'<circle cx="{hx}" cy="{hy}" r="78" fill="#0B2545"/>')
    out.append(f'<text x="{hx}" y="{hy - 4}" text-anchor="middle" font-size="16" font-weight="800" fill="#fff">{C.TEAM_HUB[0]}</text>')
    out.append(f'<text x="{hx}" y="{hy + 18}" text-anchor="middle" font-size="16" font-weight="800" fill="#8FD0FF">{C.TEAM_HUB[1]}</text>')
    out.append(f'<text x="{hx}" y="{hy + 40}" text-anchor="middle" font-size="11" fill="#B5C4D6">공동 테스트베드 (안)</text>')
    # 사람 노드
    for p in C.TEAM:
        x, y = p["pos"]
        w, h = 250, 84
        x0, y0 = x - w / 2, y - h / 2
        out.append(f'<rect x="{x0 + 2}" y="{y0 + 4}" width="{w}" height="{h}" rx="16" fill="#0B2545" opacity=".05"/>')
        out.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="16" fill="#fff" stroke="{p["color"]}" stroke-width="2"/>')
        out.append(f'<circle cx="{x0 + 40}" cy="{y}" r="24" fill="{p["color"]}"/>')
        out.append(f'<text x="{x0 + 40}" y="{y + 6}" text-anchor="middle" font-size="17" font-weight="800" fill="#fff">{p["name"][0]}</text>')
        out.append(f'<text x="{x0 + 76}" y="{y - 8}" font-size="18" font-weight="800" fill="#0B1F33">{p["name"]}'
                   f'<tspan font-size="12.5" font-weight="600" fill="#7B8A9C"> {p["role"]}</tspan></text>')
        out.append(f'<text x="{x0 + 76}" y="{y + 15}" font-size="12" fill="#46566A">{escape(p["org"].split(" (")[0])}</text>')
        out.append(f'<text x="{x0 + 76}" y="{y + 32}" font-size="11.5" font-weight="600" fill="#0B1F33">{escape(" · ".join(p["tags"][:2]))}</text>')
    out.append("</svg>")
    return "".join(out)


html(f"""
<div class="sec"><div class="no">01 · TEAM</div>
<div class="t">네 사람, 네 개의 연결</div>
<div class="d">둘레의 선은 두 사람이 바로 함께할 수 있는 주제, 가운데는 넷이 같이 만드는 공동 테스트베드입니다.</div></div>
<div class="panel"><div class="net-team">{team_svg()}</div></div>
""")

# ── 02 사람별 이력 ──
cards = []
for p in C.TEAM:
    tags = "".join(f'<span class="tg">{t}</span>' for t in p["tags"])
    hist = "".join(f'<dt>{k}</dt><dd>{v}{"<span class=chk>확인 필요</span>" if chk else ""}</dd>' for k, v, chk in p["history"])
    cards.append(
        f'<div class="pc" style="--c:{p["color"]}"><div class="hd"><div class="av">{p["name"][0]}</div>'
        f'<div><div class="nm">{p["name"]}<small>{p["role"]}</small></div><div class="og">{p["org"]}</div></div></div>'
        f'<div class="tags" style="--c:{p["color"]}">{tags}</div><dl class="hist">{hist}</dl></div>'
    )
html(f"""
<div class="sec"><div class="no">02 · PROFILE</div>
<div class="t">이력 — 각자 쌓아 온 것</div></div>
<div class="people">{''.join(cards)}</div>
""")

# ── 03 타임라인 + 역량 매트릭스 ──
html("""
<div class="sec"><div class="no">03 · DATA</div>
<div class="t">스토리와 역량 — 겹치는 곳이 협업 지점</div>
<div class="d">점은 이력상의 주요 연구·경력(마우스를 올리면 상세), 색이 진할수록 해당 역량이 강합니다.</div></div>
""")
left, right = st.columns([1.25, 1], gap="large")
with left:
    html('<div class="ctitle">이력 타임라인</div><div class="csub">2015 – 2026</div>')
    order = ["ksh", "pgy", "lse", "lgy"]  # 아래 → 위

    def _positions(pts):
        """라벨 있는 점만 위/아래 번갈아 배치해 겹침을 줄임."""
        out, n = [], 0
        for t in pts:
            out.append("top center" if n % 2 == 0 else "bottom center")
            n += 1 if t[2] else 0
        return out

    fig = go.Figure()
    for key in order:
        p = P[key]
        pts = sorted([t for t in C.TEAM_TIMELINE if t[1] == key], key=lambda t: t[0])
        fig.add_trace(go.Scatter(
            x=[t[0] for t in pts], y=[p["name"]] * len(pts), mode="markers+text",
            marker=dict(size=13, color=p["color"], line=dict(color="#FFFFFF", width=2)),
            text=[t[2] for t in pts],
            textposition=_positions(pts),
            textfont=dict(size=10.5, color="#46566A"),
            customdata=[t[3] for t in pts],
            hovertemplate="<b>%{y}</b> · %{x:.0f}<br>%{customdata}<extra></extra>",
            name=p["name"], showlegend=False, cliponaxis=False,
        ))
    fig.update_layout(
        height=360, margin=dict(l=8, r=16, t=16, b=8), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, color="#46566A"),
        xaxis=dict(range=[2014.5, 2027.2], dtick=1, showgrid=True, gridcolor="#EEF2F7", zeroline=False, tickfont=dict(size=11)),
        yaxis=dict(type="category", categoryorder="array", categoryarray=[P[k]["name"] for k in order],
                   tickfont=dict(size=13, color="#0B1F33"), showgrid=False),
        hoverlabel=dict(bgcolor="#0B2545", font_color="#FFFFFF", bordercolor="#0B2545"),
    )
    st.plotly_chart(fig, config={"displayModeBar": False}, width="stretch")
with right:
    html('<div class="ctitle">역량 매트릭스</div><div class="csub">0–3 초안 점수 · 당사자 확인 후 수정</div>')
    keys = ["lgy", "lse", "pgy", "ksh"]
    z = [[C.TEAM_SCORES[k][i] for k in keys] for i in range(len(C.TEAM_SKILLS))]
    hm = go.Figure(go.Heatmap(
        z=z, x=[P[k]["name"] for k in keys], y=C.TEAM_SKILLS, zmin=0, zmax=3,
        colorscale=[[0, "#F3F6FA"], [0.34, "#CFE1F6"], [0.67, "#6FA6E6"], [1, "#1D5FB0"]],
        xgap=3, ygap=3, showscale=False, text=z, texttemplate="%{text}",
        textfont=dict(size=12), hovertemplate="%{x} · %{y}: %{z}<extra></extra>",
    ))
    hm.update_layout(
        height=360, margin=dict(l=8, r=8, t=8, b=8), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, color="#46566A"),
        xaxis=dict(side="top", tickfont=dict(size=13, color="#0B1F33")),
        yaxis=dict(autorange="reversed", tickfont=dict(size=12)),
        hoverlabel=dict(bgcolor="#0B2545", font_color="#FFFFFF", bordercolor="#0B2545"),
    )
    st.plotly_chart(hm, config={"displayModeBar": False}, width="stretch")

# ── 04 협업 과제(안) ──
pjs = []
for t, d, roles in C.TEAM_PROJECTS:
    who = "".join(
        f'<span class="{"lead" if r == "주관" else ""}" style="--c:{P[k]["color"]}">{P[k]["name"]} · {r}</span>'
        for k, r in sorted(roles.items(), key=lambda kv: kv[1] != "주관")
    )
    pjs.append(f'<div class="pj"><div class="t">{t}</div><div class="d">{d}</div><div class="who">{who}</div></div>')
steps = "".join(
    f'<div class="rs"><div class="y">{y}</div><div class="dot"></div><div class="t">{t}</div><div class="s">{s}</div></div>'
    for y, t, s in C.TEAM_NEXT
)
html(f"""
<div class="sec"><div class="no">04 · PROJECTS</div>
<div class="t">협업 과제 (안)</div></div>
<div class="projects">{''.join(pjs)}</div>
<div class="sec" style="margin-top:36px"><div class="no">05 · NEXT</div>
<div class="t">다음 단계</div></div>
<div class="panel" style="padding:18px 12px 20px"><div class="road r3">{steps}</div></div>
<div class="disc">{C.TEAM_NOTE}</div>
""")

st.write("")
with st.expander("출처 · 근거 자료"):
    st.markdown("\n".join(f"- [{t}]({u})" for t, u in C.TEAM_SOURCES))

html(f'<div class="foot"><span>K-water연구원 AI연구소 · Water Co-Scientist</span><span>업데이트 {C.UPDATED}</span></div>')
