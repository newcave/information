# information — KISTI × 도메인 연구기관 협업 지형

K-water연구원 AI연구소 **Water Co-Scientist** 기획의 일환으로, 한국과학기술정보연구원(KISTI)이
생명·정보보안·융합연구·소재 분야 대표 기관과 어떻게 협업하고 있는지, 그리고 물 도메인(K-water)이
그 협업망에 어떻게 들어가는지를 한 페이지로 보여주는 Streamlit 앱입니다. (기술기획처 설명용)

## 페이지 구성

| 섹션 | 내용 |
|---|---|
| Hero | 핵심 메시지 + 지표 4개 |
| 01 협업 지형 | KISTI 허브 ↔ 생명연·국보연·KIST·KBSI·K-water 네트워크 |
| 02 협업 사례 | 기관별 협업 내용·산출물·근거 |
| 03 정렬 | Bigdata → K-WeSi → AI-Delphi → Prediction ↔ Water Co-Scientist 모듈 |
| 04 왜 지금 | ICLR 투고 추이 (사람만으로는 다 읽을 수 없다) |
| 05 검토 포인트 | 기술기획처 검토 포인트 3가지 + 출처 |

## 수정 방법

문구·수치·출처는 모두 `content.py` 에 있습니다. `app.py` 는 레이아웃만 담당합니다.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud 배포

1. share.streamlit.io → **Create app** → 이 저장소 선택
2. Branch `main`, Main file path `app.py` → Deploy

테마는 `.streamlit/config.toml` (라이트 테마 고정), 사이드바는 사용하지 않습니다.

## 출처 표기 원칙

- 공개 보도·발표자료로 확인되는 협업 사실만 표기 (기관별 예산·인력 규모는 비공개라 미표기)
- 국보연·KIST 협업 분야, AI-Delphi 구성, ICLR 투고 추이는 KISTI 세미나 발표자료(2026.11.19) 기준
