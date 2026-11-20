"""KISTI × 도메인 연구기관 협업 지형 — Water Co-Scientist 설득 페이지 (단일 페이지).

실행: streamlit run app.py
문구·수치·출처 수정은 content.py 에서.
"""
from html import escape

import plotly.graph_objects as go
import streamlit as st

import content as C

st.set_page_config(
    page_title="KISTI × 도메인 협업 | Water Co-Scientist",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def html(s: str) -> None:
    """들여쓰기·빈 줄 때문에 마크다운 코드블록으로 오인되지 않도록 한 줄로 압축해 렌더링."""
    st.markdown(" ".join(line.strip() for line in s.splitlines() if line.strip()), unsafe_allow_html=True)


# ─────────────────────────────── 스타일 ───────────────────────────────
CSS = f"""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
:root {{
  --ink:#0B1F33; --ink2:#46566A; --muted:#7B8A9C; --line:#E2E8F0; --bg:#F5F7FB; --card:#FFFFFF;
  --navy:#0B2545; --navy2:#123A63;
  --bio:{C.COLORS['bio']}; --sec:{C.COLORS['sec']}; --mat:{C.COLORS['mat']};
  --water:{C.COLORS['water']}; --fus:{C.COLORS['fus']};
  --font:"Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR","Noto Sans CJK KR",sans-serif;
}}
html, body, .stApp, .stMarkdown, button, input {{ font-family:var(--font) !important; }}
.stApp {{ background:var(--bg); color:var(--ink); word-break:keep-all; overflow-wrap:anywhere; }}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], [data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display:none !important; }}
header[data-testid="stHeader"] {{ background:transparent; height:0; }}
.block-container {{ max-width:1180px; padding:1.4rem 1.4rem 4rem; }}
.stMarkdown p {{ margin:0; }}

/* hero */
.hero {{ position:relative; overflow:hidden; border-radius:22px; padding:42px 46px 34px; color:#fff;
  background:radial-gradient(900px 380px at 88% -15%, rgba(42,120,214,.55), transparent 62%),
             linear-gradient(135deg,var(--navy) 0%,var(--navy2) 58%,var(--navy) 100%); }}
.hero:before {{ content:""; position:absolute; inset:0; pointer-events:none;
  background-image:linear-gradient(rgba(255,255,255,.055) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.055) 1px,transparent 1px);
  background-size:34px 34px; -webkit-mask-image:linear-gradient(180deg,#000,transparent 80%); mask-image:linear-gradient(180deg,#000,transparent 80%); }}
.hero > * {{ position:relative; }}
.eyebrow {{ font-size:12px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:#9CC6F5; }}
.h1 {{ font-size:clamp(26px,3.3vw,42px); line-height:1.24; font-weight:800; letter-spacing:-.025em; margin:14px 0 14px; color:#fff; }}
.h1 em {{ font-style:normal; color:#8FD0FF; }}
.lead {{ color:#C8D5E5; font-size:15.5px; line-height:1.65; max-width:760px; }}
.kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:28px; }}
.kpi {{ background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.13); border-radius:14px; padding:14px 16px 13px; }}
.kpi b {{ display:block; font-size:28px; font-weight:800; letter-spacing:-.02em; color:#fff; line-height:1.15; }}
.kpi span {{ display:block; margin-top:6px; font-size:12.5px; line-height:1.45; color:#B5C4D6; }}

/* section heading */
.sec {{ margin:52px 0 16px; }}
.sec .no {{ font-size:12px; font-weight:800; letter-spacing:.16em; color:var(--water); }}
.sec .t {{ font-size:25px; font-weight:800; letter-spacing:-.02em; color:var(--ink); margin-top:6px; }}
.sec .d {{ font-size:14.5px; color:var(--ink2); margin-top:6px; line-height:1.6; }}
.panel {{ background:var(--card); border:1px solid var(--line); border-radius:18px; padding:14px; box-shadow:0 1px 2px rgba(16,24,40,.04); }}

/* network */
.net-wide svg {{ width:100%; height:auto; display:block; font-family:var(--font); }}
.flow {{ stroke-dasharray:7 7; animation:flow 1.2s linear infinite; }}
@keyframes flow {{ to {{ stroke-dashoffset:-28; }} }}
.legend {{ display:flex; flex-wrap:wrap; gap:16px; justify-content:center; padding:8px 4px 4px; font-size:12.5px; color:var(--ink2); }}

.net-narrow {{ display:none; }}
.hub-mini {{ background:var(--navy); color:#fff; border-radius:14px; padding:14px 16px; }}
.hub-mini b {{ font-size:20px; }} .hub-mini span {{ display:block; font-size:12.5px; color:#B5C4D6; margin-top:4px; }}
.spokes {{ margin:0 0 0 18px; border-left:2px solid var(--line); padding:6px 0 0 0; }}
.spoke {{ position:relative; margin:10px 0 0 16px; background:#fff; border:1px solid var(--line); border-left:5px solid var(--c); border-radius:12px; padding:10px 12px; }}
.spoke:before {{ content:""; position:absolute; left:-18px; top:22px; width:16px; border-top:2px solid var(--line); }}
.spoke.new {{ border-style:dashed; border-left-style:solid; background:#EEF5FD; }}
.spoke .r1 {{ display:flex; justify-content:space-between; gap:8px; font-size:12px; color:var(--ink2); }}
.spoke .o {{ font-size:15px; font-weight:700; margin-top:3px; }}
.spoke .x {{ font-size:12.5px; color:var(--ink2); margin-top:2px; }}

/* chips */
.dom {{ display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:700; color:var(--ink);
  background:color-mix(in srgb,var(--c) 13%,#fff); border:1px solid color-mix(in srgb,var(--c) 45%,#fff); border-radius:999px; padding:3px 10px; }}
.dom:before {{ content:""; width:8px; height:8px; border-radius:50%; background:var(--c); }}
.st {{ font-size:12px; font-weight:600; color:var(--ink2); background:#F1F4F8; border-radius:999px; padding:3px 10px; white-space:nowrap; }}

.si {{ display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:5px; vertical-align:0; border:1.5px solid var(--ink2); box-sizing:border-box; }}
.si-full {{ background:var(--ink2); }}
.si-half {{ background:linear-gradient(90deg,var(--ink2) 50%,transparent 50%); }}
.si-play {{ border:none; border-radius:0; width:0; height:0; border-left:8px solid var(--ink2); border-top:5px solid transparent; border-bottom:5px solid transparent; }}
.si-ring {{ border-style:dashed; }}
/* cases */
.cases {{ display:grid; grid-template-columns:repeat(2,1fr); gap:14px; }}
.case {{ background:#fff; border:1px solid var(--line); border-top:4px solid var(--c); border-radius:16px; padding:18px 20px 16px; }}
.case .r1 {{ display:flex; justify-content:space-between; align-items:center; gap:8px; }}
.case .org {{ font-size:19px; font-weight:800; letter-spacing:-.015em; margin-top:12px; }}
.case .org small {{ display:block; font-size:12.5px; font-weight:500; color:var(--muted); margin-top:2px; }}
.case dl {{ margin:12px 0 0; display:grid; grid-template-columns:44px 1fr; row-gap:7px; column-gap:8px; font-size:13.8px; line-height:1.55; }}
.case dt {{ font-weight:700; color:var(--muted); font-size:12.5px; padding-top:1px; }}
.case dd {{ margin:0; color:var(--ink); }}
.case .src {{ margin-top:12px; padding-top:10px; border-top:1px dashed var(--line); font-size:12px; color:var(--muted); }}
.case .src a {{ color:var(--ink2); text-decoration:underline; text-underline-offset:2px; }}
.case.next {{ grid-column:1/-1; border:1.5px dashed var(--water); border-top:4px solid var(--water);
  background:linear-gradient(120deg,#EEF5FD 0%,#FFFFFF 70%); }}
.case.next .org {{ font-size:21px; }}
.case.next dl {{ grid-template-columns:44px 1fr; }}

/* pipeline */
.pipe {{ display:grid; grid-template-columns:repeat(4,1fr); gap:0 2px; }}
.pcol {{ display:flex; flex-direction:column; }}
.chev {{ color:#fff; padding:16px 34px 16px 42px; min-height:92px;
  clip-path:polygon(0 0,calc(100% - 24px) 0,100% 50%,calc(100% - 24px) 100%,0 100%,24px 50%); }}
.pcol:first-child .chev {{ padding-left:22px; clip-path:polygon(0 0,calc(100% - 24px) 0,100% 50%,calc(100% - 24px) 100%,0 100%); border-radius:12px 0 0 12px; }}
.chev b {{ display:block; font-size:19px; font-weight:800; letter-spacing:-.01em; }}
.chev span {{ font-size:13px; opacity:.88; }}
.pdetail {{ font-size:12.5px; color:var(--ink2); line-height:1.5; padding:10px 14px 0 18px; min-height:52px; }}
.parrow {{ text-align:center; color:var(--muted); font-size:18px; line-height:1; padding:8px 0 6px; }}
.mod {{ margin:0 8px; background:#fff; border:1px solid var(--line); border-radius:14px; padding:12px 14px; flex:1; }}
.mod .k {{ font-size:11px; font-weight:800; letter-spacing:.12em; color:var(--water); }}
.mod .m {{ font-size:15px; font-weight:800; margin-top:4px; letter-spacing:-.01em; }}
.mod .s {{ font-size:12.5px; color:var(--ink2); margin-top:2px; }}
.chip {{ display:inline-block; margin-top:9px; font-size:11.5px; font-weight:700; border-radius:999px; padding:3px 9px; }}
.chip.now {{ background:var(--water); color:#fff; }}
.chip.next {{ background:#fff; color:var(--water); border:1.5px dashed var(--water); }}
.chip.own {{ background:#EEF2F7; color:var(--ink2); }}
.pnote {{ margin-top:14px; font-size:12.5px; color:var(--muted); }}

/* why now */
.qs {{ display:flex; flex-direction:column; gap:10px; }}
.q {{ background:#fff; border:1px solid var(--line); border-radius:14px; padding:14px 16px; font-size:17px; color:var(--ink); }}
.q b {{ color:var(--water); }}
.ans {{ margin-top:4px; background:var(--navy); color:#fff; border-radius:14px; padding:16px 18px; font-size:15px; line-height:1.6; }}
.ans b {{ color:#8FD0FF; }}
.cap {{ font-size:12px; color:var(--muted); margin-top:4px; }}
.ctitle {{ font-size:15px; font-weight:800; color:var(--ink); padding:4px 4px 0; }}
.csub {{ font-size:12.5px; color:var(--ink2); padding:2px 4px 0; }}

/* asks */
.asks {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }}
.ask {{ background:#fff; border:1px solid var(--line); border-radius:16px; padding:20px 20px 18px; }}
.ask .n {{ font-size:13px; font-weight:800; color:var(--water); letter-spacing:.1em; }}
.ask .t {{ font-size:18px; font-weight:800; margin-top:6px; letter-spacing:-.015em; }}
.ask .d {{ font-size:14px; color:var(--ink2); margin-top:8px; line-height:1.65; }}
.ask .d b {{ color:var(--ink); }}
.disc {{ margin-top:14px; font-size:12.5px; color:var(--muted); }}
.foot {{ margin-top:40px; padding-top:16px; border-top:1px solid var(--line); font-size:12px; color:var(--muted); display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px; }}
[data-testid="stExpander"] details {{ background:#fff; border:1px solid var(--line); border-radius:14px; }}
[data-testid="stExpander"] li {{ font-size:13px; }}

@media (max-width: 860px) {{
  .kpis {{ grid-template-columns:repeat(2,1fr); }}
  .kpi b {{ font-size:22px; white-space:nowrap; }}
  .h1 br {{ display:none; }} .h1 em {{ display:block; margin-top:4px; }}
  .hero {{ padding:28px 22px 24px; }}
  .net-wide {{ display:none; }} .net-narrow {{ display:block; }}
  .cases, .asks {{ grid-template-columns:1fr; }}
  .pipe {{ grid-template-columns:1fr; gap:14px; }}
  .chev, .pcol:first-child .chev {{ clip-path:none; border-radius:12px; padding:14px 18px; min-height:0; }}
  .pdetail {{ min-height:0; padding:8px 4px 0; }}
  .mod {{ margin:0; }}
}}
</style>
"""
html(CSS)


def status_html(s: str) -> str:
    return f'<span class="st"><i class="si si-{C.STATUS_KIND[s]}"></i>{s}</span>'


def status_svg(s: str, right: float, y: float) -> str:
    """상태 라벨(오른쪽 정렬)과 아이콘을 SVG 도형으로 그림."""
    kind, ink = C.STATUS_KIND[s], "#46566A"
    tw = sum(3.6 if ch == " " else 11.2 for ch in s)
    cx, cy = right - tw - 9, y - 4
    if kind == "full":
        icon = f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="{ink}"/>'
    elif kind == "half":
        icon = (f'<circle cx="{cx}" cy="{cy}" r="4" fill="none" stroke="{ink}" stroke-width="1.5"/>'
                f'<path d="M{cx},{cy - 4} A4,4 0 0,0 {cx},{cy + 4} Z" fill="{ink}"/>')
    elif kind == "play":
        icon = f'<polygon points="{cx - 3.5},{cy - 5} {cx + 4.5},{cy} {cx - 3.5},{cy + 5}" fill="{ink}"/>'
    else:
        icon = f'<circle cx="{cx}" cy="{cy}" r="4" fill="none" stroke="{ink}" stroke-width="1.5" stroke-dasharray="2 1.8"/>'
    return icon + (f'<text x="{right}" y="{y}" text-anchor="end" font-size="11.5" font-weight="600" fill="{ink}">'
                   f'{escape(s)}</text>')


# ─────────────────────────────── 네트워크 SVG ───────────────────────────────
def network_svg() -> str:
    W, H = 1000, 560
    hx, hy, hr = 500, 262, 100
    parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
             f'aria-label="KISTI를 중심으로 생명·정보보안·소재·융합 연구기관과 K-water가 연결된 협업 지형">']
    # 배경 동심 타원
    for rx, ry, op in [(420, 235, .55), (300, 170, .7), (180, 110, .9)]:
        parts.append(f'<ellipse cx="{hx}" cy="{hy}" rx="{rx}" ry="{ry}" fill="none" stroke="#E6ECF3" stroke-width="1" opacity="{op}"/>')
    # 연결선
    for n in C.NODES:
        x, y = n["pos"]
        col = C.COLORS[n["key"]]
        if n.get("new"):
            parts.append(f'<line x1="{hx}" y1="{hy}" x2="{x}" y2="{y}" stroke="{col}" stroke-width="3" class="flow"/>')
        else:
            parts.append(f'<line x1="{hx}" y1="{hy}" x2="{x}" y2="{y}" stroke="{col}" stroke-width="2.2" opacity=".75"/>')
    # 허브
    parts.append(f'<circle cx="{hx}" cy="{hy}" r="{hr + 10}" fill="#0B2545" opacity=".08"/>')
    parts.append(f'<circle cx="{hx}" cy="{hy}" r="{hr}" fill="#0B2545"/>')
    parts.append(f'<text x="{hx}" y="{hy - 22}" text-anchor="middle" font-size="34" font-weight="800" fill="#fff" letter-spacing="1">{C.HUB["name"]}</text>')
    parts.append(f'<text x="{hx}" y="{hy + 2}" text-anchor="middle" font-size="12.5" fill="#B5C4D6">{escape(C.HUB["full"])}</text>')
    for i, a in enumerate(C.HUB["assets"]):
        yy = hy + 30 + i * 22
        parts.append(f'<rect x="{hx - 74}" y="{yy - 14}" width="148" height="19" rx="9.5" fill="#1C4572"/>')
        parts.append(f'<text x="{hx}" y="{yy}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#DCE8F6">{escape(a)}</text>')
    # 노드 카드
    for n in C.NODES:
        x, y = n["pos"]
        col = C.COLORS[n["key"]]
        new = n.get("new", False)
        w, h = (312, 128) if new else (236, 104)
        x0, y0 = x - w / 2, y - h / 2
        fill = "#EEF5FD" if new else "#FFFFFF"
        stroke = f'stroke="{col}" stroke-width="2" stroke-dasharray="6 5"' if new else 'stroke="#E2E8F0" stroke-width="1"'
        parts.append(f'<rect x="{x0 + 2}" y="{y0 + 4}" width="{w}" height="{h}" rx="14" fill="#0B2545" opacity=".05"/>')
        parts.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="14" fill="{fill}" {stroke}/>')
        parts.append(f'<rect x="{x0}" y="{y0 + 14}" width="5" height="{h - 28}" rx="2.5" fill="{col}"/>')
        # 도메인 칩
        dw = 16 + len(n["domain"]) * 11.5
        parts.append(f'<rect x="{x0 + 16}" y="{y0 + 12}" width="{dw}" height="20" rx="10" fill="{col}" opacity=".16"/>')
        parts.append(f'<circle cx="{x0 + 26}" cy="{y0 + 22}" r="3.5" fill="{col}"/>')
        parts.append(f'<text x="{x0 + 34}" y="{y0 + 26.5}" font-size="11.5" font-weight="700" fill="#0B1F33">{escape(n["domain"])}</text>')
        # 상태
        parts.append(status_svg(n["status"], x0 + w - 14, y0 + 26.5))
        # 본문
        parts.append(f'<text x="{x0 + 18}" y="{y0 + 54}" font-size="{17 if new else 16}" font-weight="800" fill="#0B1F33">{escape(n["org"])}</text>')
        parts.append(f'<text x="{x0 + 18}" y="{y0 + 72}" font-size="12" fill="#7B8A9C">{escape(n["sub"])}</text>')
        parts.append(f'<text x="{x0 + 18}" y="{y0 + 92}" font-size="12.5" font-weight="600" fill="#0B1F33">{escape(n["out"])}</text>')
        if n.get("out2"):
            parts.append(f'<text x="{x0 + 18}" y="{y0 + 111}" font-size="12.5" font-weight="600" fill="#0B1F33">{escape(n["out2"])}</text>')
    # 신규 노드 라벨
    parts.append(f'<rect x="{hx + 14}" y="{hy + hr + 10}" width="118" height="22" rx="11" fill="{C.COLORS["water"]}"/>')
    parts.append(f'<text x="{hx + 73}" y="{hy + hr + 25.5}" text-anchor="middle" font-size="11.5" font-weight="800" fill="#fff">NEW · 물 도메인</text>')
    parts.append("</svg>")
    return "".join(parts)


def network_narrow() -> str:
    rows = []
    for n in C.NODES:
        col = C.COLORS[n["key"]]
        cls = "spoke new" if n.get("new") else "spoke"
        out = n["out"] + (f'<br>{n["out2"]}' if n.get("out2") else "")
        rows.append(
            f'<div class="{cls}" style="--c:{col}"><div class="r1"><span class="dom" style="--c:{col}">{n["domain"]}</span>'
            f'{status_html(n["status"])}</div>'
            f'<div class="o">{n["org"]}</div><div class="x">{out}</div></div>'
        )
    return (f'<div class="net-narrow"><div class="hub-mini"><b>KISTI</b> 한국과학기술정보연구원'
            f'<span>{" · ".join(C.HUB["assets"])}</span></div><div class="spokes">{"".join(rows)}</div></div>')


# ─────────────────────────────── 1. HERO ───────────────────────────────
kpis = "".join(f'<div class="kpi"><b>{v}</b><span>{d}</span></div>' for v, d in C.KPIS)
html(f"""
<div class="hero">
  <div class="eyebrow">{C.HERO['eyebrow']}</div>
  <div class="h1">{C.HERO['title']}</div>
  <div class="lead">{C.HERO['lead']}</div>
  <div class="kpis">{kpis}</div>
</div>
""")

# ─────────────────────────────── 2. 협업 지형 ───────────────────────────────
legend = "".join(f'<span><i class="si si-{k}"></i>{s}</span>' for s, k in C.STATUS_KIND.items())
html(f"""
<div class="sec"><div class="no">01 · LANDSCAPE</div>
<div class="t">협업 지형 — KISTI를 중심으로 도메인이 맞물려 있다</div>
<div class="d">각 분야 대표 연구기관이 KISTI의 데이터·분석·LLM 자산을 자기 도메인에 연결했습니다. 물 도메인 노드는 아직 비어 있습니다.</div></div>
<div class="panel"><div class="net-wide">{network_svg()}</div>{network_narrow()}
<div class="legend">{legend}</div></div>
""")

# ─────────────────────────────── 3. 사례 ───────────────────────────────
def case_card(c: dict, extra_cls: str = "") -> str:
    col = C.COLORS[c["key"]]
    rows = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in c["rows"])
    src = ""
    if c.get("src"):
        links = " · ".join(f'<a href="{u}" target="_blank">{t}</a>' if u else t for t, u in c["src"])
        src = f'<div class="src">근거 · {links}</div>'
    return (f'<div class="case {extra_cls}" style="--c:{col}"><div class="r1"><span class="dom" style="--c:{col}">{c["domain"]}</span>'
            f'{status_html(c["status"])}</div>'
            f'<div class="org">{c["org"]}<small>{c["org_sub"]}</small></div><dl>{rows}</dl>{src}</div>')


cards = "".join(case_card(c) for c in C.CASES) + case_card(C.NEXT_CASE, "next")
html(f"""
<div class="sec"><div class="no">02 · EVIDENCE</div>
<div class="t">확인된 협업 사례 — 도메인마다 ‘KISTI 분석 + 기관 전문성’</div>
<div class="d">규모는 공개되지 않았지만, 협업 자체는 보고서·보도자료·서비스로 확인됩니다.</div></div>
<div class="cases">{cards}</div>
""")

# ─────────────────────────────── 4. 파이프라인 정렬 ───────────────────────────────
shades = ["#5B7088", "#2A78D6", "#1D5FB0", "#0B2545"]
cols = []
for i, p in enumerate(C.PIPELINE):
    cols.append(
        f'<div class="pcol"><div class="chev" style="background:{shades[i]}"><b>{p["step"]}</b><span>{p["kr"]}</span></div>'
        f'<div class="pdetail">{p["detail"]}</div><div class="parrow">↓</div>'
        f'<div class="mod"><div class="k">WATER CO-SCIENTIST</div><div class="m">{p["module"]}</div>'
        f'<div class="s">{p["module_sub"]}</div><span class="chip {p["chip_kind"]}">{p["chip"]}</span></div></div>'
    )
html(f"""
<div class="sec"><div class="no">03 · ALIGNMENT</div>
<div class="t">KISTI 미래기술 탐지 체계 ↔ Water Co-Scientist 모듈</div>
<div class="d">KONI 기반 LLM 에이전트든, 기술 확보·평가 에이전트든 모두 Water Co-Scientist의 일부입니다.</div></div>
<div class="panel" style="padding:18px"><div class="pipe">{''.join(cols)}</div>
<div class="pnote">현재 MOU·기술이전 범위는 ‘자료 획득·관리’. K-WeSi·AI-Delphi는 KISTI 에이전트응용연구센터와의 확장 협업 후보입니다.
AI-Delphi 구성(에이전트 40명·논문 590편·3라운드)은 2026.11.19 세미나 발표 기준.</div></div>
""")

# ─────────────────────────────── 5. 왜 지금인가 ───────────────────────────────
html("""
<div class="sec"><div class="no">04 · WHY NOW</div>
<div class="t">사람만으로는 더 이상 다 읽을 수 없다</div>
<div class="d">AI 분야 최상위 학회 한 곳의 투고량만 봐도 검토 수요는 지수적으로 늘고 있습니다.</div></div>
""")
left, right = st.columns([1.45, 1], gap="large")
with left:
    html('<div class="ctitle">ICLR 연도별 투고 논문 수</div><div class="csub">단위: 편 · 막대에 마우스를 올리면 값 표시</div>')
    ys, vs = C.ICLR["years"], C.ICLR["values"]
    colors = ["#0B2545"] * (len(vs) - 1) + ["#2A78D6"]
    patterns = [""] * (len(vs) - 1) + ["/"]
    text = [""] * (len(vs) - 3) + [f"{v:,}" for v in vs[-3:]]
    fig = go.Figure(go.Bar(
        x=ys, y=vs, marker=dict(color=colors, cornerradius=4, line=dict(width=0),
                                 pattern=dict(shape=patterns, fgcolor="#FFFFFF", size=7, solidity=.25)),
        text=text, textposition="outside", textfont=dict(size=12, color="#0B1F33"),
        hovertemplate="%{x}년: %{y:,}편<extra></extra>", cliponaxis=False, width=0.62,
    ))
    fig.add_annotation(x="2027*", y=62288, text="추정", showarrow=False, yshift=34,
                       font=dict(size=11, color="#46566A"))
    fig.update_layout(
        height=340, margin=dict(l=8, r=8, t=36, b=8), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Pretendard, Apple SD Gothic Neo, Malgun Gothic, Noto Sans CJK KR, sans-serif", color="#46566A"),
        bargap=0.3, showlegend=False,
        xaxis=dict(type="category", showgrid=False, linecolor="#CBD5E1", tickfont=dict(size=12)),
        yaxis=dict(gridcolor="#EEF2F7", zeroline=False, tickformat=",", tickfont=dict(size=11), range=[0, 72000]),
        hoverlabel=dict(bgcolor="#0B2545", font_color="#FFFFFF", bordercolor="#0B2545"),
    )
    st.plotly_chart(fig, config={"displayModeBar": False}, width="stretch")
    html(f'<div class="cap">{C.ICLR["note"]}</div>')
with right:
    qs = "".join(f'<div class="q">{q}</div>' for q in C.QUESTIONS)
    html(f"""
    <div class="qs">{qs}
    <div class="ans">→ <b>AI 전문가 패널·에이전트</b>가 1차 탐지·평가를 맡고,<br>사람은 <b>판단과 결정</b>에 집중합니다.
    KISTI는 이 구조(AI-Delphi, AI사이언티스트)를 이미 도메인 기관과 운영 중입니다.</div></div>
    """)

# ─────────────────────────────── 6. 검토 포인트 ───────────────────────────────
asks = "".join(f'<div class="ask"><div class="n">POINT {i + 1:02d}</div><div class="t">{a["t"]}</div><div class="d">{a["d"]}</div></div>'
               for i, a in enumerate(C.ASKS))
html(f"""
<div class="sec"><div class="no">05 · DECISION</div>
<div class="t">기술기획처 검토 포인트</div></div>
<div class="asks">{asks}</div>
<div class="disc">※ {C.DISCLAIMER}</div>
""")

st.write("")
with st.expander("출처 · 근거 자료"):
    st.markdown("\n".join(f"- [{t}]({u})" if u else f"- {t}" for t, u in C.SOURCES))

html(f'<div class="foot"><span>K-water연구원 AI연구소 · Water Co-Scientist</span><span>업데이트 {C.UPDATED}</span></div>')
