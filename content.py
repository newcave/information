"""페이지에 들어가는 모든 문구·수치·출처를 한 곳에 모아 둔 파일.

문구를 고칠 때는 app.py 대신 이 파일만 수정하면 됩니다.
status 값: "정례 성과" | "공동 분석" | "적용 중" | "추진 중"
"""

UPDATED = "2026.11.20"

# ── 도메인 색 (dataviz 검증: 인접 노드 쌍 CVD ΔE ≥ 9, 모든 노드에 텍스트 라벨 병기) ──
COLORS = {
    "bio": "#1BAF7A",   # 생명·바이오
    "sec": "#6250D6",   # 정보보안
    "mat": "#E87BA4",   # 소재·분석
    "water": "#2A78D6", # 물
    "fus": "#EB6834",   # 융합연구
}

HERO = {
    "eyebrow": "Water Co-Scientist · KISTI 협력 기획 · " + UPDATED,
    "title": (
        "KISTI는 이미 도메인 연구기관과 <br>"
        "‘데이터 × AI’로 맞물려 있습니다. <br>"
        "<em>비어 있는 자리는 ‘물’입니다.</em>"
    ),
    "lead": (
        "생명·정보보안·융합연구·소재 분야 대표 기관이 KISTI의 위크시그널 분석, "
        "AI 전문가 패널, 과학기술 LLM ‘KONI(고니)’를 자기 도메인에 붙여 성과를 내고 있습니다. "
        "K-water연구원은 물 도메인으로 이 협업망에 합류해 Water Co-Scientist의 핵심 모듈을 확보합니다."
    ),
}

KPIS = [
    ("4개 기관", "KISTI와 공동 성과를 낸 도메인 연구기관<br>(생명 · 정보보안 · 융합 · 소재)"),
    ("1,753만 건", "바이오 위크시그널 탐색에 쓰인 논문<br>(SCOPUS 2019–2023 → 신호 230개)"),
    ("1,400명", "미래기술 예측에 투입된<br>AI 가상 전문가 (DATA INSIGHT 60호)"),
    ("6회", "KONI(고니) 기술이전 실적<br>(2026.8 기준)"),
]

HUB = {
    "name": "KISTI",
    "full": "한국과학기술정보연구원",
    "assets": ["KONI · AI Scientist", "K-WeSi · AI-Delphi"],
}

# 네트워크 노드 (시계방향: 좌상 → 우상 → 우하 → 하단 → 좌하)
NODES = [
    {
        "key": "bio", "pos": (255, 92), "domain": "생명·바이오",
        "org": "한국생명공학연구원", "sub": "국가생명공학정책연구센터",
        "out": "바이오 미래유망기술 공동발간", "status": "정례 성과",
    },
    {
        "key": "sec", "pos": (745, 92), "domain": "정보보안",
        "org": "국가보안기술연구소", "sub": "ETRI 부설 · NSR",
        "out": "정보보안 분야 유망기술 도출", "status": "공동 분석",
    },
    {
        "key": "mat", "pos": (855, 345), "domain": "소재·분석",
        "org": "한국기초과학지원연구원", "sub": "KBSI",
        "out": "AI사이언티스트 → 반도체 재료", "status": "적용 중",
    },
    {
        "key": "water", "pos": (500, 478), "domain": "물 · Water",
        "org": "K-water연구원 AI연구소", "sub": "Water Co-Scientist",
        "out": "KONI 자료 획득·관리 (MOU·기술이전)",
        "out2": "기술 탐지·평가 (K-WeSi·AI-Delphi)",
        "status": "추진 중", "new": True,
    },
    {
        "key": "fus", "pos": (145, 345), "domain": "융합연구",
        "org": "한국과학기술연구원", "sub": "KIST",
        "out": "융합연구 분야 유망기술 도출", "status": "공동 분석",
    },
]

STATUS_KIND = {"정례 성과": "full", "공동 분석": "half", "적용 중": "play", "추진 중": "ring"}

# ── 사례 카드 ──
CASES = [
    {
        "key": "bio", "domain": "생명·바이오", "status": "정례 성과",
        "org": "한국생명공학연구원", "org_sub": "국가생명공학정책연구센터 (KRIBB)",
        "rows": [
            ("협업", "KISTI 위크시그널 탐색 데이터로 바이오 미래유망기술 후보 발굴 — 2021년부터 매년"),
            ("방법", "SCOPUS 논문 1,753만 건(2019–2023) 키워드 추출 → 바이오 위크시그널 230개 → 혁신형 시드"),
            ("산출", "「바이오 미래유망기술」 KRIBB–KISTI 공동발간(2022–2025), 과기정통부 발표로 연결"),
        ],
        "src": [("파이낸셜뉴스 2022.2", "https://www.fnnews.com/news/202202281455392275"),
                ("뉴스서울 2024.2", "https://newsseoul.co.kr/news/view/1065610818876337")],
    },
    {
        "key": "sec", "domain": "정보보안", "status": "공동 분석",
        "org": "국가보안기술연구소", "org_sub": "ETRI 부설 (NSR)",
        "rows": [
            ("협업", "정보보안 분야 미래유망기술 후보를 KISTI 분석체계로 공동 도출"),
            ("예시", "QKD망 경로·키자원 최적화, 양자내성암호, 프라이버시 보호 기술 등"),
            ("의미", "보안 민감 도메인도 KISTI 데이터 분석과 결합 가능함을 확인"),
        ],
        "src": [("KISTI 세미나 발표자료 2026.11.19", None)],
    },
    {
        "key": "fus", "domain": "융합연구", "status": "공동 분석",
        "org": "한국과학기술연구원", "org_sub": "KIST",
        "rows": [
            ("협업", "융합연구 분야 미래유망기술 후보를 KISTI 분석체계로 공동 도출"),
            ("예시", "생성형 AI 기반 도시 예측, 재난 대응 디지털트윈, 모빌리티용 AI 센서 등"),
            ("의미", "재난·디지털트윈 등 물 분야와 맞닿은 주제가 이미 후보군에 포함"),
        ],
        "src": [("KISTI 세미나 발표자료 2026.11.19", None)],
    },
    {
        "key": "mat", "domain": "소재·분석", "status": "적용 중",
        "org": "한국기초과학지원연구원", "org_sub": "KBSI",
        "rows": [
            ("협업", "KONI 기반 ‘AI사이언티스트’(논문 분석 → 연구가설 제시)를 반도체 재료 분야에 적용"),
            ("일정", "1차 개발 완료(2026.8), KBSI 통해 2026년 말 서비스 계획"),
            ("기대", "KISTI 측 기대치 — 연구 작업 효율 10~20배"),
        ],
        "src": [("ZDNet Korea 2026.8", "https://zdnet.co.kr/view/?no=20260814113304"),
                ("ZDNet Korea 2025.7", "https://zdnet.co.kr/view/?no=20250727113433")],
    },
]

NEXT_CASE = {
    "key": "water", "domain": "물 · Water", "status": "추진 중",
    "org": "K-water연구원 AI연구소", "org_sub": "Water Co-Scientist",
    "rows": [
        ("현재", "KISTI와 MOU·기술이전 추진 — KONI 기반 <b>자료 획득·관리</b> 에이전트"),
        ("확장", "KISTI 에이전트응용연구센터(양혜영 박사)의 <b>K-WeSi · AI-Delphi</b> 연계 → 물 분야 기술 탐지·평가 에이전트"),
        ("목표", "물 분야 위크시그널·유망기술을 데이터로 도출해 연구기획·투자 우선순위의 근거로 활용"),
    ],
}

# ── 파이프라인 정렬 ──
PIPELINE = [
    {
        "step": "Bigdata", "kr": "논문 · 특허 · 웹",
        "detail": "논문 = 지식의 기본단위<br>인용관계로 기술 클러스터 구성",
        "module": "자료 획득·관리 에이전트", "module_sub": "KONI · RAG",
        "chip": "MOU·기술이전 추진", "chip_kind": "now",
    },
    {
        "step": "K-WeSi", "kr": "위크시그널 탐지",
        "detail": "활동성 높은 키워드·구문을<br>그룹핑해 미래기술 신호 포착",
        "module": "물 분야 기술 탐지 에이전트", "module_sub": "위크시그널 · 논문 클러스터",
        "chip": "협업 후보", "chip_kind": "next",
    },
    {
        "step": "AI-Delphi", "kr": "AI 전문가 패널",
        "detail": "페르소나 에이전트 40명 × 논문 590편<br>× 3라운드 반복 의견수렴",
        "module": "기술 평가 에이전트", "module_sub": "AI 전문가 패널 합의",
        "chip": "협업 후보", "chip_kind": "next",
    },
    {
        "step": "Prediction", "kr": "인사이트",
        "detail": "유망기술 선정·근거 제시<br>(예: 241선, DATA INSIGHT 60호)",
        "module": "연구기획 지원", "module_sub": "가설 · 로드맵 · 우선순위",
        "chip": "Co-Scientist 내재화", "chip_kind": "own",
    },
]

# ── 왜 지금인가 (ICLR 투고 추이, Reviewer3 / 세미나 자료 재인용) ──
ICLR = {
    "years": ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027*"],
    "values": [490, 1018, 1579, 2594, 3014, 3422, 4955, 7404, 11672, 19814, 62288],
    "note": "* 2027은 초록 등록 기준 추정치(2026.9.21). 출처: Reviewer3 (KISTI 세미나 자료 재인용)",
}

QUESTIONS = [
    "인간은 모든 <b>리뷰</b>를 할 수 있을까?",
    "인간은 모든 <b>검토</b>를 할 수 있을까?",
    "인간은 모든 <b>분석</b>을 할 수 있을까?",
]

# ── 기술기획처 검토 포인트 ──
ASKS = [
    {
        "t": "검증된 협업 모델",
        "d": "KISTI는 생명·정보보안·융합·소재 기관과 이미 공동 성과를 냈습니다. "
             "물 도메인 확장은 새 실험이 아니라 <b>검증된 패턴의 적용</b>입니다.",
    },
    {
        "t": "Co-Scientist의 구성요소",
        "d": "KONI 기반 자료 획득·관리(MOU·기술이전)와 기술 탐지·평가 에이전트(K-WeSi·AI-Delphi)는 "
             "별도 사업이 아니라 <b>Water Co-Scientist의 모듈</b>입니다.",
    },
    {
        "t": "물 분야 기술기획 근거",
        "d": "생명연 사례처럼 데이터 기반 유망기술 도출이 정례화되면, "
             "K-water 연구기획·투자 우선순위에 <b>객관적 근거</b>가 생깁니다.",
    },
]

DISCLAIMER = (
    "기관별 협업 규모(예산·인력)는 공개되지 않았습니다. "
    "이 페이지는 공개 보도·발표자료로 확인되는 협업 사실만 표기했습니다."
)

SOURCES = [
    ("파이낸셜뉴스 (2022.2.28) — 생명연 국가생명공학정책연구센터·KISTI 데이터분석본부, 위크시그널 기법으로 바이오 유망기술 발굴",
     "https://www.fnnews.com/news/202202281455392275"),
    ("머니투데이 (2023.3.6) — 생명연·KISTI, 2023년 10대 바이오 미래유망기술",
     "https://www.mt.co.kr/future/2023/03/06/2023030609270753879"),
    ("뉴스서울 (2024.2.26) — 2024년 10대 바이오 미래유망기술, 2021년부터 KISTI 위크시그널 모델 활용",
     "https://newsseoul.co.kr/news/view/1065610818876337"),
    ("디지털타임스 (2025.1.20) — 2025년 10대 바이오 미래유망기술",
     "https://www.dt.co.kr/article/11640769"),
    ("ZDNet Korea (2026.8.14) — KISTI ‘AI사이언티스트’ 1차 개발 완료, KBSI 통해 연말 서비스 / KONI 기술이전 6회",
     "https://zdnet.co.kr/view/?no=20260814113304"),
    ("ZDNet Korea (2025.7.27) — KISTI·KBSI·생명연 등 6개 출연연 AI 융합인재 업무협약",
     "https://zdnet.co.kr/view/?no=20250727113433"),
    ("기계신문 (2026.1.30) — KONI ICLR 논문 2편, ‘AI 연구동료(AI Co-Scientist)’ 개발 추진",
     "http://www.mtnews.net/news/articleView.html?idxno=23769"),
    ("쿠키뉴스 (2026.1.20) — KISTI, 인간-AI 협업으로 미래 고성장 과학기술 241선 (DATA INSIGHT 60호)",
     "https://www.kukinews.com/article/view/kuk202601200189"),
    ("대학지성 (2026) — KISTI, 1,400명 AI 가상 전문가 활용 미래유망기술 예측",
     "https://www.unipress.co.kr/news/articleView.html?idxno=13974"),
    ("헤럴드경제 (2026.8.14) — KISTI ‘AI 과학자’ 첫 공개 (KDD 2026)",
     "https://biz.heraldcorp.com/article/10841497"),
    ("KISTI 리포지터리 — 『미래기술 위크시그널』 (양혜영 외, 2024)",
     "https://repository.kisti.re.kr/handle/10580/19341"),
    ("KISTI News (2026.6.12) — AI 추론과정 평가기술 TRACE (ICML 2026, 양혜영 박사 연구팀)",
     "https://www.kisti.re.kr/eng/news/post/eng_news"),
    ("KISTI 세미나 발표자료 (2026.11.19, 양혜영 박사) — 국보연·KIST 협업 분야, AI-Delphi 구성, ICLR 투고 추이",
     None),
]
