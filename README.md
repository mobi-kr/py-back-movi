# py-back-movi

MOVI 중고차 통합검색·AI 분석 플랫폼의 Python 백엔드입니다.

메인 백엔드는 Spring Boot이며, 이 서비스는 **데이터 수집**과 향후 **Python 기반 AI 분석**을 담당합니다.

> 현재 운영 서버와 PostgreSQL은 아직 구축되지 않았습니다. 이 단계의 서비스는 외부 의존성 없이 단독으로 실행됩니다.

## 기술 스택

| 구분 | 사용 기술 |
| --- | --- |
| 언어 | Python 3.14 |
| 웹 프레임워크 | FastAPI, Uvicorn |
| 설정 | Pydantic v2, pydantic-settings |
| 패키지 관리 | uv |
| 테스트 | pytest |
| Lint / Format | Ruff |

## 사전 준비

- [uv](https://docs.astral.sh/uv/) 설치
- Python 3.14 (없으면 `uv python install 3.14`로 설치)

## 시작하기

```bash
# 의존성 설치 (uv.lock 기준)
uv sync --frozen

# 환경변수 파일 생성
cp .env.example .env

# 개발 서버 실행
uv run uvicorn app.main:app --reload
```

서버 실행 후 확인:

```bash
curl http://127.0.0.1:8000/health/live
# {"status":"ok"}
```

API 문서: http://127.0.0.1:8000/docs

## 환경변수

| 이름 | 기본값 | 설명 |
| --- | --- | --- |
| `APP_NAME` | `py-back-movi` | 애플리케이션 이름 |
| `APP_ENV` | `local` | 실행 환경 (`local`, `dev`, `prod`, `test`) |
| `DEBUG` | `false` | FastAPI 디버그 모드 |
| `LOG_LEVEL` | `INFO` | 로그 레벨 (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) |

환경변수가 `.env` 파일보다 우선합니다.

## 테스트 및 코드 품질

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## 프로젝트 구조

```
app/
├── main.py          # FastAPI 엔트리포인트
├── api/
│   └── health.py    # GET /health/live
└── core/
    ├── config.py    # 환경변수 설정 (pydantic-settings)
    └── logging.py   # 기본 로깅 설정
tests/               # pytest 테스트
```

## API

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| `GET` | `/health/live` | 프로세스 생존 확인 (항상 `200 {"status":"ok"}`) |
