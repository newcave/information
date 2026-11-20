"""공통 스타일·헬퍼."""
import streamlit as st

import content as C


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
#MainMenu, footer, [data-testid="stDecoration"], [data-testid="stStatusWidget"], [data-testid="stAppDeployButton"] {{ display:none !important; }}
header[data-testid="stHeader"] {{ background:rgba(245,247,251,.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line); }}
.block-container {{ max-width:1180px; padding:4.6rem 1.4rem 4rem; }}
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

/* AI scientist page */
.missions {{ display:grid; grid-template-columns:repeat(6,1fr); gap:8px; }}
.ms {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:12px 8px; text-align:center; font-size:14px; font-weight:600; color:var(--ink2); }}
.ms small {{ display:block; font-size:11px; color:var(--muted); font-weight:700; letter-spacing:.08em; }}
.ms.on {{ background:var(--navy); color:#fff; border-color:var(--navy); box-shadow:0 0 0 3px rgba(42,120,214,.35); }}
.ms.on small {{ color:#8FD0FF; }}
.budgets {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }}
.bd {{ background:#fff; border:1px solid var(--line); border-radius:14px; padding:16px 18px; }}
.bd.est {{ border:1.5px dashed var(--water); background:#EEF5FD; }}
.bd .a {{ font-size:26px; font-weight:800; letter-spacing:-.02em; color:var(--ink); }}
.bd .n {{ font-size:14px; font-weight:700; margin-top:4px; }}
.bd .x {{ font-size:12.5px; color:var(--muted); margin-top:3px; }}
.tag {{ float:right; font-size:11px; font-weight:700; border-radius:999px; padding:2px 8px; background:#F1F4F8; color:var(--ink2); }}
.tag.est {{ background:var(--water); color:#fff; }}
.road {{ display:grid; grid-template-columns:repeat(5,1fr); position:relative; }}
.road:before {{ content:""; position:absolute; left:6%; right:6%; top:17px; border-top:2px solid var(--line); }}
.rs {{ position:relative; text-align:center; padding:0 6px; }}
.rs .dot {{ width:14px; height:14px; border-radius:50%; background:var(--water); margin:10px auto 10px; box-shadow:0 0 0 4px #fff; }}
.rs:last-child .dot {{ background:var(--navy); }}
.rs .y {{ font-size:13px; font-weight:800; color:var(--water); letter-spacing:.06em; }}
.rs .t {{ font-size:15px; font-weight:800; margin-top:2px; }}
.rs .s {{ font-size:12.5px; color:var(--ink2); margin-top:2px; }}

/* plan page */
.lks {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:10px 0 18px; }}
.lk {{ background:#fff; border:1px solid var(--line); border-radius:14px; padding:14px 16px; }}
.lk b {{ display:block; font-size:24px; font-weight:800; letter-spacing:-.02em; color:var(--ink); }}
.lk span {{ display:block; font-size:12.5px; color:var(--ink2); margin-top:4px; line-height:1.45; }}
.story {{ position:relative; margin-top:10px; }}
.st-row {{ display:grid; grid-template-columns:84px 22px 1fr; align-items:start; }}
.st-y {{ font-size:13px; font-weight:800; color:var(--water); text-align:right; padding:12px 8px 0 0; }}
.st-dot {{ position:relative; height:100%; }}
.st-dot:before {{ content:""; position:absolute; left:10px; top:0; bottom:0; border-left:2px solid var(--line); }}
.st-dot:after {{ content:""; position:absolute; left:4px; top:14px; width:14px; height:14px; border-radius:50%; background:#fff; border:3px solid #9AA8B8; box-sizing:border-box; }}
.st-row.both .st-dot:after {{ background:var(--water); border-color:var(--water); }}
.st-row.bg .st-dot:after {{ border-style:dashed; }}
.st-c {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:10px 14px; margin:6px 0; }}
.st-row.both .st-c {{ border:1.5px solid var(--water); background:#EEF5FD; }}
.st-row.bg .st-c {{ background:#F5F7FB; }}
.st-w {{ font-size:12px; font-weight:700; color:var(--muted); }}
.st-t {{ font-size:14.5px; font-weight:700; color:var(--ink); margin-top:2px; }}
[data-testid="stTabs"] button p {{ font-size:15px; font-weight:700; }}

/* team page */
.net-team svg {{ width:100%; height:auto; display:block; font-family:var(--font); }}
.road.r3 {{ grid-template-columns:repeat(3,1fr); }}
.people {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; }}
.pc {{ background:#fff; border:1px solid var(--line); border-top:4px solid var(--c); border-radius:16px; padding:16px 16px 14px; }}
.pc .hd {{ display:flex; align-items:center; gap:10px; }}
.av {{ width:42px; height:42px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:17px; color:#fff; background:var(--c); flex:none; }}
.pc .nm {{ font-size:18px; font-weight:800; letter-spacing:-.01em; }}
.pc .nm small {{ font-size:12.5px; font-weight:600; color:var(--muted); margin-left:4px; }}
.pc .og {{ font-size:12.5px; color:var(--ink2); margin-top:1px; }}
.tags {{ display:flex; flex-wrap:wrap; gap:5px; margin-top:12px; }}
.tg {{ font-size:11.5px; font-weight:600; color:var(--ink); background:color-mix(in srgb,var(--c) 12%,#fff); border:1px solid color-mix(in srgb,var(--c) 40%,#fff); border-radius:999px; padding:2px 8px; }}
.hist {{ margin-top:12px; border-top:1px dashed var(--line); padding-top:10px; display:grid; grid-template-columns:38px 1fr; row-gap:6px; column-gap:6px; font-size:12.8px; line-height:1.45; }}
.hist dt {{ font-weight:700; color:var(--muted); font-size:11.5px; padding-top:1px; }}
.hist dd {{ margin:0; }}
.chk {{ display:inline-block; font-size:10.5px; font-weight:700; color:#9A5B00; background:#FFF4DE; border-radius:6px; padding:0 5px; margin-left:4px; }}
.projects {{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; }}
.pj {{ background:#fff; border:1px solid var(--line); border-radius:14px; padding:14px 16px; }}
.pj .t {{ font-size:16px; font-weight:800; }}
.pj .d {{ font-size:13px; color:var(--ink2); margin-top:4px; line-height:1.5; }}
.pj .who {{ display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }}
.who span {{ font-size:12px; font-weight:700; border-radius:999px; padding:2px 9px; border:1.5px solid var(--c); color:var(--ink); background:#fff; }}
.who span.lead {{ background:var(--c); color:#fff; }}

@media (max-width: 860px) {{
  .people, .projects {{ grid-template-columns:1fr; }}
  .lks {{ grid-template-columns:repeat(2,1fr); }}
  .st-row {{ grid-template-columns:62px 22px 1fr; }}
  .road.r3 {{ grid-template-columns:1fr; }}
  .missions {{ grid-template-columns:repeat(3,1fr); }}
  .budgets {{ grid-template-columns:1fr; }}
  .road {{ grid-template-columns:1fr; gap:10px; }} .road:before {{ display:none; }}
  .rs {{ text-align:left; display:grid; grid-template-columns:60px 1fr; align-items:baseline; background:#fff; border:1px solid var(--line); border-radius:12px; padding:10px 12px; }}
  .rs .dot {{ display:none; }}
  .rs .s {{ grid-column:2; }}
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


def inject_css() -> None:
    html(CSS)
