# Prestige Marketing - 네이버 블로그 마케팅 사이트

## 프로젝트 소개
Prestige Marketing은 네이버 블로그 마케팅 대행 서비스를 제공하는 전문 회사의 웹사이트입니다.
모던하고 전문적인 디자인으로 제작된 반응형 웹사이트입니다.

## 주요 기능
- 📱 **모바일 반응형 디자인** - 모든 디바이스에서 최적화된 화면
- 🎨 **모던한 UI/UX** - 그라데이션과 애니메이션을 활용한 세련된 디자인
- 📝 **문의 폼 시스템** - 고객 문의를 자동으로 저장하는 시스템
- ⚡ **빠른 로딩** - 최적화된 코드와 리소스
- 🔒 **보안** - XSS 방지 및 입력값 검증

## 파일 구조
```
marketing/
├── index.php              # 메인 페이지
├── contact_process.php    # 문의 폼 처리 스크립트
├── README.md             # 프로젝트 설명서
├── css/
│   └── style.css         # 스타일시트
├── js/
│   └── script.js         # JavaScript 인터랙션
├── images/               # 이미지 디렉토리 (수동으로 추가 필요)
└── inquiries/            # 문의 내용 저장 디렉토리 (자동 생성)
```

## 이미지 추가 가이드

### 필요한 이미지 목록
사이트에서 사용하는 이미지들을 다음 경로에 추가해주세요:

#### 1. 서비스 아이콘 (각 60x60px, PNG 또는 SVG 권장)
- `images/blog-icon.png` - 블로그 배포 아이콘 (노트북과 블로그 화면 심볼)
- `images/content-icon.png` - 콘텐츠 제작 아이콘 (문서와 펜 심볼)
- `images/ranking-icon.png` - 상위 노출 아이콘 (상승 그래프와 1위 메달)
- `images/smartblock-icon.png` - 스마트블록 아이콘 (큐브와 체크마크)
- `images/review-icon.png` - 후기 콘텐츠 아이콘 (별점과 말풍선)
- `images/all-industries-icon.png` - 전업종 가능 아이콘 (다양한 업종 심볼 조합)

#### 2. 배너 이미지
- `images/consultation-banner.png` - 상담 안내 배너 (300x200px)
  - 전문 상담사와 고객이 대화하는 모습
  - 따뜻하고 신뢰감 있는 분위기

### 이미지 제작 가이드라인

#### 색상 팔레트
- **Primary Blue**: #1e40af
- **Secondary Blue**: #3b82f6
- **Accent Color**: #06b6d4
- **Dark**: #1e293b
- **Light**: #f8fafc

#### 스타일 가이드
- 아이콘: 심플하고 모던한 라인 스타일
- 색상: 위의 색상 팔레트 사용 권장
- 포맷: PNG (투명 배경) 또는 SVG
- 최적화: 웹 최적화된 이미지 사용

### 이미지가 없을 때
이미지가 준비되지 않았다면, 다음과 같이 처리할 수 있습니다:

1. **임시로 이모지 사용** (현재 설정됨)
   - CSS의 `.service-icon`이 이모지를 표시하도록 설정되어 있습니다.

2. **아이콘 폰트 사용**
   - Font Awesome이나 Material Icons를 추가하여 사용 가능

3. **온라인 에셋 활용**
   - Unsplash, Pexels 등에서 무료 이미지 다운로드
   - Flaticon에서 아이콘 다운로드

## 클라우드웨이즈 배포 가이드

### 1. 파일 업로드
클라우드웨이즈 서버에 FTP 또는 SFTP로 접속하여 모든 파일을 업로드합니다.

```bash
# SFTP 접속 (클라우드웨이즈에서 제공하는 정보 사용)
sftp username@server-ip

# 파일 업로드
put -r * /public_html/
```

### 2. 권한 설정
```bash
# 문의 저장 디렉토리 권한 설정
chmod 755 inquiries/
chmod 644 inquiries/*.csv
chmod 644 inquiries/*.txt
```

### 3. PHP 설정 확인
- PHP 버전: 7.4 이상 권장
- 필요한 확장: mbstring, json (기본 설치됨)

### 4. 도메인 연결
클라우드웨이즈 관리 패널에서:
1. Applications > 앱 선택
2. Domain Management
3. Primary Domain 설정

## 문의 폼 이메일 알림 설정 (선택사항)

`contact_process.php` 파일에서 이메일 알림 기능을 활성화할 수 있습니다:

1. 파일 열기: `contact_process.php`
2. 주석 처리된 이메일 코드 찾기 (라인 90-140)
3. 주석 해제하고 이메일 주소 수정:
```php
$to = "your-email@example.com"; // 실제 이메일 주소로 변경
```

### SMTP 설정 (권장)
더 안정적인 이메일 전송을 위해 PHPMailer 사용을 권장합니다:

```bash
# Composer로 PHPMailer 설치
composer require phpmailer/phpmailer
```

## 커스터마이징

### 색상 변경
`css/style.css` 파일의 `:root` 섹션에서 색상 변수를 수정하세요:

```css
:root {
    --primary-color: #1e40af;      /* 메인 색상 */
    --secondary-color: #3b82f6;     /* 보조 색상 */
    --accent-color: #06b6d4;        /* 강조 색상 */
}
```

### 연락처 정보 변경
`index.php` 파일에서 다음 정보를 수정하세요:
- 카카오톡 ID: pres00
- 전화번호: 010-3966-7687

### 통계 수치 변경
`index.php` 파일의 Stats Section에서 수정:
```html
<div class="stat-item">
    <h3>1000+</h3>
    <p>성공 프로젝트</p>
</div>
```

## 문의 데이터 확인

문의가 접수되면 다음 위치에 저장됩니다:
- `inquiries/inquiries.csv` - 모든 문의 내역 (CSV 형식)
- `inquiries/inquiry_YYYYMMDD_HHMMSS_*.txt` - 개별 문의 파일

## 브라우저 지원
- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome Mobile)

## 성능 최적화 팁

1. **이미지 최적화**
   - TinyPNG나 ImageOptim으로 이미지 압축
   - WebP 포맷 사용 고려

2. **캐싱 활성화**
   - .htaccess 파일에 브라우저 캐싱 설정 추가

3. **CDN 사용**
   - 정적 파일을 CDN에 호스팅

4. **Gzip 압축**
   - 클라우드웨이즈 설정에서 활성화

## 보안 권장사항

1. **HTTPS 사용**
   - 클라우드웨이즈에서 Let's Encrypt SSL 인증서 설치

2. **정기적인 백업**
   - 클라우드웨이즈 자동 백업 기능 활성화

3. **파일 권한 관리**
   ```bash
   # 디렉토리: 755
   # PHP 파일: 644
   # 민감한 설정 파일: 600
   ```

4. **보안 헤더 추가**
   - .htaccess에 보안 헤더 설정

## 문제 해결

### 문의 폼이 작동하지 않을 때
1. PHP 버전 확인 (7.4 이상)
2. inquiries 디렉토리 권한 확인 (755)
3. 브라우저 콘솔에서 JavaScript 오류 확인

### 모바일에서 레이아웃이 깨질 때
1. 캐시 클리어
2. viewport meta 태그 확인
3. CSS 파일이 제대로 로드되는지 확인

### 이미지가 표시되지 않을 때
1. 이미지 경로 확인
2. 파일명 대소문자 확인 (Linux는 대소문자 구분)
3. 이미지 파일 권한 확인 (644)

## 연락처
- 카카오톡: pres00
- 전화: 010-3966-7687

## 라이선스
© 2024 Prestige Marketing. All rights reserved.
