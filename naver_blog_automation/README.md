# 네이버 블로그 자동화 프로그램

네이버 블로그 포스트를 자동으로 작성하고 발행하는 파이썬 프로그램입니다. 셀레니움(Selenium)을 사용하며, 봇 탐지를 우회하기 위한 다양한 기능을 포함합니다.

## 주요 기능

### ✅ 구현된 기능

- **봇 탐지 우회**: undetected-chromedriver를 사용한 고급 봇 탐지 우회
- **자동 로그인**: 복사/붙여넣기 방식으로 안전한 로그인 (send_keys 미사용)
- **블로그 글쓰기**: 제목과 내용을 자동으로 입력하고 발행
- **다중 계정 지원**: 여러 계정으로 순차적으로 작업 가능
- **시크릿 모드**: 각 계정마다 독립적인 시크릿 모드 세션
- **인간적인 동작**: 랜덤 지연시간과 자연스러운 마우스 움직임
- **설정 파일 관리**: JSON 기반 설정 시스템

### 🔧 향후 구현 예정

- **AI 글 생성**: OpenAI, Anthropic 등 API를 통한 자동 글 생성
- **IP 변경**: 안드로이드 폰 또는 프록시 서비스를 통한 IP 로테이션
- **이미지 업로드**: 포스트에 이미지 자동 첨부
- **카테고리 & 태그**: 자동 카테고리 선택 및 태그 추가
- **임시저장**: 발행 전 임시저장 기능

## 설치 방법

### 1. 저장소 클론 (또는 다운로드)

```bash
cd naver_blog_automation
```

### 2. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

**필수 패키지:**
- `undetected-chromedriver`: 봇 탐지 우회
- `selenium`: 웹 자동화
- `pyperclip`: 복사/붙여넣기 기능
- `python-dotenv`: 환경 변수 관리
- `fake-useragent`: User-Agent 랜덤화

### 3. 크롬 브라우저 설치

셀레니움을 사용하므로 Chrome 브라우저가 설치되어 있어야 합니다.

## 설정 방법

### 1. 설정 파일 생성

예제 파일을 복사하여 실제 설정 파일을 만듭니다:

```bash
cp config.example.json config.json
cp accounts.example.json accounts.json
cp posts.example.json posts.json
```

### 2. 계정 정보 입력 (accounts.json)

```json
[
    {
        "username": "your_naver_id",
        "password": "your_password",
        "enabled": true
    }
]
```

- `username`: 네이버 아이디
- `password`: 네이버 비밀번호
- `enabled`: 이 계정 사용 여부 (false로 설정하면 건너뜀)

### 3. 포스트 작성 (posts.json)

```json
[
    {
        "title": "블로그 포스트 제목",
        "content": "블로그 포스트 내용\n\n여러 줄로 작성 가능합니다.",
        "enabled": true
    }
]
```

- `title`: 포스트 제목
- `content`: 포스트 내용 (`\n`으로 줄바꿈)
- `enabled`: 이 포스트 발행 여부

### 4. 설정 조정 (config.json)

```json
{
    "browser": {
        "headless": false,      // true: 화면 없이 실행 (비권장)
        "incognito": true,      // 시크릿 모드 사용
        "window_size": "1920x1080"
    },
    "delays": {
        "min_delay": 1.0,       // 최소 지연 시간 (초)
        "max_delay": 3.0,       // 최대 지연 시간 (초)
        "wait_after_login": 5,  // 로그인 후 대기 (초)
        "wait_after_publish": 10 // 발행 후 대기 (초)
    }
}
```

## 사용 방법

### 기본 실행

```bash
python main.py
```

### 커스텀 파일 경로 지정

```bash
python main.py --config my_config.json --accounts my_accounts.json --posts my_posts.json
```

### 테스트 모드

```bash
python main.py --test
```

## 프로그램 구조

```
naver_blog_automation/
├── main.py                     # 메인 실행 스크립트
├── requirements.txt            # 필수 패키지
├── config.json                 # 설정 파일
├── accounts.json              # 계정 정보
├── posts.json                 # 포스트 목록
├── naver_blog_bot/
│   ├── __init__.py
│   ├── browser.py             # 봇 탐지 우회 브라우저 설정
│   ├── login.py               # 네이버 로그인 자동화
│   ├── blog_writer.py         # 블로그 글쓰기 자동화
│   ├── config.py              # 설정 관리
│   └── utils.py               # 유틸리티 함수들
└── README.md
```

## 봇 탐지 우회 기술

이 프로그램은 다음과 같은 기술을 사용하여 봇 탐지를 우회합니다:

1. **undetected-chromedriver**: Selenium 감지를 우회하는 크롬 드라이버
2. **복사/붙여넣기 입력**: `send_keys` 대신 `Ctrl+V`로 입력 (더 자연스러움)
3. **랜덤 지연시간**: 사람처럼 불규칙한 대기 시간
4. **자연스러운 마우스 움직임**: ActionChains를 통한 실제 마우스 동작 시뮬레이션
5. **JavaScript 조작**: webdriver 속성 및 기타 자동화 감지 속성 제거
6. **시크릿 모드**: 각 세션마다 깨끗한 브라우저 환경

## 주의사항

### ⚠️ 중요

- **네이버 이용약관 준수**: 네이버의 이용약관을 반드시 확인하고 준수하세요
- **과도한 사용 금지**: 너무 많은 포스트를 짧은 시간에 발행하면 계정이 제재될 수 있습니다
- **캡챠 대응**: 캡챠가 나타나면 수동으로 처리해야 합니다
- **계정 보안**: `accounts.json` 파일은 절대 공개하지 마세요 (`.gitignore`에 포함됨)

### 권장사항

- **헤드리스 모드 비활성화**: `headless: false`로 설정 (봇 탐지 우회에 유리)
- **적절한 지연시간**: 너무 빠르게 동작하면 의심받을 수 있습니다
- **계정당 1일 포스트 제한**: 하루에 계정당 3-5개 정도만 발행하는 것을 권장
- **IP 로테이션**: 가능하면 IP를 변경하면서 사용 (향후 구현 예정)

## 문제 해결

### 로그인 실패

- 아이디/비밀번호 확인
- 캡챠 또는 본인 인증이 필요한지 확인
- 네이버 로그인 페이지가 변경되었는지 확인

### 글 발행 실패

- 네이버 블로그 에디터가 업데이트되었는지 확인
- iframe 로딩 시간이 충분한지 확인 (지연시간 증가)
- 브라우저 콘솔에서 에러 메시지 확인

### 봇으로 감지됨

- 지연시간 증가
- headless 모드 비활성화
- 최신 버전의 `undetected-chromedriver` 사용
- IP 주소 변경

## 향후 개발 계획

### AI 글 생성 (옵션)

```json
"content_generation": {
    "mode": "ai_keyword",
    "api_provider": "openai",
    "api_key": "your_api_key"
}
```

- `manual`: 수동으로 작성한 글 사용 (현재 구현됨)
- `ai_keyword`: 키워드 기반 자동 글 생성
- `ai_custom`: 커스텀 프롬프트로 글 생성

### IP 로테이션 (옵션)

```json
"ip_rotation": {
    "enabled": true,
    "method": "android_phone"  // 또는 "proxy_service"
}
```

- `android_phone`: ADB로 안드로이드 폰의 비행기 모드 제어
- `proxy_service`: 프록시 서비스 사용

## 라이선스

이 프로그램은 교육 목적으로 제공됩니다. 사용에 따른 책임은 사용자에게 있습니다.

## 기여

버그 리포트나 기능 제안은 이슈로 등록해주세요.

## 변경 이력

### v1.0.0 (2024-12-12)

- 초기 버전 릴리스
- 기본 로그인 및 글쓰기 기능 구현
- 봇 탐지 우회 기능 구현
- 다중 계정 지원
