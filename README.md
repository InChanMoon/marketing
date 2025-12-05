# Prestige Marketing - 네이버 블로그 마케팅 사이트

## 프로젝트 소개
Prestige Marketing은 네이버 블로그 마케팅 대행 서비스를 제공하는 전문 회사의 프리미엄 웹사이트입니다.
이미지 중심의 모던하고 전문적인 디자인으로 제작된 완전 반응형 웹사이트입니다.

## 주요 특징
- 🖼️ **이미지 중심 디자인** - 프리미엄한 비주얼로 전문성 강조
- 📱 **완전 반응형** - 모바일, 태블릿, 데스크톱 완벽 대응
- 🎨 **모던한 UI/UX** - 세련된 그라데이션과 부드러운 애니메이션
- 📊 **포트폴리오 섹션** - 성공 사례를 통한 신뢰도 구축
- 💼 **회사 소개 섹션** - 전문성과 경험 강조
- 📝 **자동 문의 관리** - CSV/TXT 파일로 문의 내용 저장
- ⚡ **고성능** - 최적화된 코드와 리소스

## 파일 구조
```
marketing/
├── index.php              # 메인 페이지 (이미지 기반 원페이지)
├── contact_process.php    # 문의 폼 처리 스크립트
├── README.md             # 프로젝트 가이드 (이 파일)
├── .htaccess             # Apache 설정 (보안/성능)
├── .gitignore            # Git 제외 파일
├── css/
│   └── style.css         # 이미지 기반 반응형 스타일
├── js/
│   └── script.js         # 인터랙션 및 폼 검증
├── images/               # ⚠️ 이미지 디렉토리 (아래 가이드 참조)
└── inquiries/            # 문의 내용 저장 (자동 생성)
```

## 페이지 구성

### 1. Hero Section (히어로 섹션)
- 대형 배경 이미지
- 강력한 헤드라인
- CTA 버튼 (무료 상담, 성공 사례)

### 2. Services (서비스)
- 6개의 이미지 기반 서비스 카드
- 호버 효과 (이미지 확대)
- 상세한 서비스 설명

### 3. Portfolio (성공 사례)
- 3개의 실제 프로젝트 사례
- 이미지 + 성과 통계
- 업종별 태그

### 4. Features (특징)
- 6개의 차별화 포인트
- 이미지 + 설명

### 5. About (회사 소개)
- 대형 팀/회사 이미지
- 회사 소개 및 강점
- 4개 핵심 가치

### 6. Industries (지원 업종)
- 24개 업종 표시
- 인터랙티브 태그

### 7. Stats (통계)
- 4가지 주요 지표
- 카운터 애니메이션

### 8. Contact (문의하기)
- 연락처 정보 + 이미지
- 문의 폼

---

## 📸 이미지 추가 가이드

### 필수 이미지 목록

사이트에 필요한 모든 이미지와 권장 사양입니다:

#### 1. Hero Section
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `hero-background.jpg` | 1920x1080px | 전문가 팀이 회의하는 모습, 모던한 오피스 배경 |

#### 2. Services Section (6개)
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `service-blog-optimization.jpg` | 800x550px | 블로그 최적화 작업 화면, 여러 모니터의 대시보드 |
| `service-content-creation.jpg` | 800x550px | 전문 작가가 콘텐츠 작성하는 모습, 노트북과 기획서 |
| `service-ranking.jpg` | 800x550px | 네이버 검색 순위 상승 그래프와 분석 화면 |
| `service-smartblock.jpg` | 800x550px | 네이버 모바일 스마트블록 노출 화면 |
| `service-review.jpg` | 800x550px | 고객이 후기를 작성하는 모습, 만족스러운 표정 |
| `service-all-industries.jpg` | 800x550px | 다양한 업종 이미지 콜라주 (병원, 음식점, 인테리어) |

#### 3. Portfolio Section (3개)
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `portfolio-hospital.jpg` | 800x600px | 병의원 관련 이미지 (깨끗한 병원 내부 또는 의료진) |
| `portfolio-interior.jpg` | 800x600px | 인테리어 시공 사례 (세련된 인테리어 완성 사진) |
| `portfolio-law.jpg` | 800x600px | 법률사무소 이미지 (전문적인 사무실 또는 법전) |

#### 4. Features Section (6개)
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `feature-targeting.jpg` | 600x450px | 데이터 분석 화면과 타겟 고객 분석 차트 |
| `feature-speed.jpg` | 600x450px | 빠른 업무 처리를 상징하는 이미지, 시계와 업무 화면 |
| `feature-reporting.jpg` | 600x450px | 상세한 마케팅 성과 리포트 화면 |
| `feature-quality.jpg` | 600x450px | 고품질 콘텐츠 작업 과정, 전문가의 손길 |
| `feature-security.jpg` | 600x450px | 보안을 상징하는 이미지, 자물쇠와 방패 |
| `feature-support.jpg` | 600x450px | 고객 상담 서비스, 헤드셋을 쓴 상담원 |

#### 5. About Section
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `about-company.jpg` | 900x900px | Prestige Marketing 팀 사진, 전문적인 오피스 환경 |

#### 6. Contact Section
| 파일명 | 크기 | 설명 |
|--------|------|------|
| `contact-consultation.jpg` | 600x400px | 상담사가 고객과 상담하는 모습, 친절한 분위기 |

---

## 🎨 이미지 제작 가이드

### 색상 팔레트
```css
Primary Blue:    #1e40af
Secondary Blue:  #3b82f6
Accent Cyan:     #06b6d4
Dark:            #1e293b
Light:           #f8fafc
Gray:            #64748b
```

### 이미지 스타일 가이드

#### 1. 전체적인 톤
- **프로페셔널하고 모던한 느낌**
- 깨끗하고 밝은 조명
- 블루 톤 계열 사용 권장
- 고급스러운 비즈니스 이미지

#### 2. 인물 이미지
- 전문적인 복장 (정장, 비즈니스 캐주얼)
- 자신감 있고 친근한 표정
- 다양성 고려 (성별, 연령)
- 업무에 집중하는 모습

#### 3. 배경 및 환경
- 현대적인 오피스 공간
- 깔끔하고 정돈된 환경
- 자연광 또는 밝은 조명
- 미니멀한 디자인

#### 4. 화면/UI 이미지
- 고해상도 스크린샷
- 실제 데이터처럼 보이는 차트
- 네이버 블로그 관련 화면
- 깔끔한 UI 디자인

### 이미지 최적화

#### 포맷 선택
- **JPG**: 사진, 복잡한 이미지 (80-85% 품질)
- **PNG**: 텍스트가 많은 UI, 투명도 필요시
- **WebP**: 최신 브라우저 지원 (용량 30-50% 절약)

#### 최적화 도구
- **TinyPNG** (https://tinypng.com) - 간편한 온라인 압축
- **ImageOptim** (Mac) - 로컬 일괄 처리
- **Squoosh** (https://squoosh.app) - 구글 제공 도구

#### 최적화 예시
```bash
# 원본 크기
hero-background.jpg: 3.5MB (1920x1080)

# 최적화 후
hero-background.jpg: 350KB (1920x1080, 80% quality)
→ 90% 용량 절감, 품질 저하 없음
```

---

## 🖼️ 이미지 소스 추천

### 무료 이미지 사이트

#### 1. Unsplash (https://unsplash.com)
- 가장 인기 있는 무료 고품질 이미지
- 상업적 이용 가능
- 크레딧 표기 불필요
- 검색어 추천:
  - "business meeting"
  - "modern office"
  - "digital marketing"
  - "data analysis"
  - "customer service"

#### 2. Pexels (https://pexels.com)
- 다양한 무료 스톡 사진
- 비디오도 제공
- 검색어 추천:
  - "professional team"
  - "workspace"
  - "consulting"

#### 3. Pixabay (https://pixabay.com)
- 180만 개 이상의 이미지
- 일러스트도 제공

#### 4. Freepik (https://freepik.com)
- 무료/유료 혼합
- 벡터, 일러스트 풍부
- 프리미엄 느낌의 비즈니스 이미지

### 유료 이미지 사이트 (고품질)

#### 1. Shutterstock (https://shutterstock.com)
- 최고 품질의 전문 이미지
- 월 $29부터 (10개 이미지)

#### 2. iStock (https://istockphoto.com)
- Getty Images 운영
- 다양한 가격대

#### 3. Envato Elements (https://elements.envato.com)
- 월 $16.50 (무제한 다운로드)
- 이미지 + 템플릿 + 폰트 등

### 이미지 검색 팁

#### Hero Background
```
검색어: "business team meeting modern office"
필터: 가로형 (Landscape), 고해상도
```

#### Services
```
검색어: "laptop work screen dashboard analytics"
필터: 작업 환경, 화면 중심
```

#### Portfolio
```
검색어: "hospital interior clean modern"
검색어: "luxury apartment interior design"
검색어: "law office professional"
```

#### Team/About
```
검색어: "professional business team portrait office"
필터: 그룹 사진, 자연스러운 포즈
```

---

## 📂 이미지 파일 준비 방법

### 1. 이미지 다운로드 후 이름 변경
```bash
# 다운로드한 파일을 지정된 이름으로 변경
unsplash-office-1234.jpg → hero-background.jpg
pexels-team-5678.jpg → about-company.jpg
```

### 2. 이미지 최적화
```bash
# TinyPNG에서 일괄 압축 또는
# 아래 명령어 사용 (ImageMagick 설치 필요)
convert hero-background.jpg -quality 85 -resize 1920x1080^ hero-background.jpg
```

### 3. images 폴더에 업로드
```bash
# FTP/SFTP로 업로드
/home/user/marketing/images/hero-background.jpg
/home/user/marketing/images/service-blog-optimization.jpg
...
```

### 4. 권한 설정 (서버에서)
```bash
chmod 644 images/*.jpg
chmod 644 images/*.png
```

---

## 🚀 클라우드웨이즈 배포 가이드

### 1. 파일 업로드

#### SFTP 정보 (클라우드웨이즈에서 확인)
```
호스트: your-server-ip
포트: 22
사용자명: your-username
비밀번호: your-password
```

#### FileZilla 사용
1. FileZilla 설치 및 실행
2. SFTP 정보 입력하여 연결
3. 로컬: marketing 폴더 선택
4. 원격: `/public_html/` 경로로 이동
5. 전체 파일 업로드

#### 명령줄 사용 (Linux/Mac)
```bash
# 전체 폴더 업로드
scp -r marketing/* username@server-ip:/public_html/

# 또는 rsync 사용 (추천)
rsync -avz --progress marketing/ username@server-ip:/public_html/
```

### 2. 이미지 파일 별도 업로드
```bash
# 이미지만 따로 업로드
scp images/* username@server-ip:/public_html/images/
```

### 3. 권한 설정
```bash
# SSH 접속 후
chmod 755 /public_html/images/
chmod 644 /public_html/images/*
chmod 755 /public_html/inquiries/
chmod 644 /public_html/*.php
```

### 4. PHP 설정 확인
- **PHP 버전**: 7.4 이상 (8.0 권장)
- **필요한 확장**: mbstring, json (기본 설치됨)
- **메모리 제한**: 128MB 이상
- **실행 시간**: 30초 이상

### 5. SSL 인증서 설정
1. 클라우드웨이즈 관리 패널 로그인
2. Applications > 앱 선택
3. SSL Certificate 섹션
4. Let's Encrypt 선택 및 설치
5. `.htaccess`에서 HTTPS 리다이렉트 활성화:
```apache
# .htaccess 파일에서 주석 해제
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### 6. 도메인 연결
1. 클라우드웨이즈: Applications > Domain Management
2. Primary Domain 입력: `yourdomain.com`
3. 도메인 등록 업체에서 DNS 설정:
   - A 레코드: `@` → 서버 IP
   - A 레코드: `www` → 서버 IP
4. DNS 전파 대기 (최대 24시간)

---

## 💻 로컬 테스트 방법

### MAMP/XAMPP 사용 (권장)

#### Mac - MAMP
```bash
1. MAMP 설치 (https://mamp.info)
2. MAMP 실행 > Start Servers
3. marketing 폴더를 /Applications/MAMP/htdocs/ 로 복사
4. 브라우저에서 http://localhost:8888/marketing/ 접속
```

#### Windows - XAMPP
```bash
1. XAMPP 설치 (https://apachefriends.org)
2. Apache 시작
3. marketing 폴더를 C:\xampp\htdocs\ 로 복사
4. 브라우저에서 http://localhost/marketing/ 접속
```

### PHP 내장 서버 사용
```bash
cd marketing
php -S localhost:8000

# 브라우저에서 http://localhost:8000 접속
```

---

## 🎯 커스터마이징 가이드

### 1. 색상 변경
`css/style.css` 파일의 `:root` 섹션 수정:
```css
:root {
    --primary-color: #1e40af;      /* 메인 색상 */
    --secondary-color: #3b82f6;     /* 보조 색상 */
    --accent-color: #06b6d4;        /* 강조 색상 */
}
```

### 2. 연락처 정보 변경
`index.php` 파일에서 검색 후 수정:
- 카카오톡 ID: `pres00`
- 전화번호: `010-3966-7687`
- 상담시간: `평일 09:00-18:00`

### 3. 회사명 변경
모든 파일에서 "Prestige Marketing" 검색 후 변경

### 4. 통계 수치 변경
`index.php` 파일의 Stats Section:
```html
<div class="stat-item">
    <h3>1000+</h3>  <!-- 이 부분 수정 -->
    <p>성공 프로젝트</p>
</div>
```

### 5. 서비스 내용 변경
`index.php`의 Services Section에서 각 카드 내용 수정

### 6. 포트폴리오 추가/변경
`index.php`의 Portfolio Section에서 항목 추가/수정

---

## 📧 이메일 알림 설정 (선택사항)

### 기본 PHP mail() 함수 사용
`contact_process.php` 파일에서 주석 해제 (라인 90-140):
```php
$to = "your-email@example.com"; // 실제 이메일로 변경
```

### PHPMailer 사용 (권장)
더 안정적인 이메일 전송을 위해:

#### 1. Composer 설치
```bash
cd /path/to/marketing
composer require phpmailer/phpmailer
```

#### 2. contact_process.php 수정
```php
use PHPMailer\PHPMailer\PHPMailer;
require 'vendor/autoload.php';

$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'your-email@gmail.com';
$mail->Password = 'your-app-password';
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
$mail->Port = 587;

$mail->setFrom('your-email@gmail.com', 'Prestige Marketing');
$mail->addAddress('your-email@gmail.com');
$mail->Subject = '새로운 문의: ' . $name;
$mail->Body = $email_message;

$mail->send();
```

---

## 📊 문의 데이터 관리

### 저장 위치
- `inquiries/inquiries.csv` - 전체 문의 목록 (엑셀 호환)
- `inquiries/inquiry_*.txt` - 개별 문의 파일

### CSV 파일 엑셀에서 열기
1. Excel 실행
2. 데이터 > 텍스트/CSV 가져오기
3. `inquiries.csv` 선택
4. UTF-8 인코딩 선택

### 문의 데이터 백업
```bash
# 주기적으로 백업 (서버에서)
cp -r inquiries/ inquiries_backup_$(date +%Y%m%d)/
```

---

## 🔧 문제 해결 (Troubleshooting)

### 1. 이미지가 표시되지 않을 때
```bash
# 원인 체크리스트:
☐ 이미지 파일이 images/ 폴더에 있는가?
☐ 파일명이 정확한가? (대소문자 구분)
☐ 파일 권한이 644인가?
☐ 이미지 경로가 정확한가?

# 해결 방법:
1. 파일 존재 확인: ls -la images/
2. 권한 확인: chmod 644 images/*.jpg
3. 브라우저 개발자 도구에서 404 오류 확인
```

### 2. 문의 폼이 작동하지 않을 때
```bash
# 체크리스트:
☐ PHP 버전이 7.4 이상인가?
☐ inquiries 폴더 권한이 755인가?
☐ contact_process.php 파일 권한이 644인가?

# 해결 방법:
1. PHP 버전 확인: php -v
2. 권한 설정: chmod 755 inquiries/
3. 브라우저 콘솔에서 JavaScript 오류 확인
```

### 3. 모바일에서 레이아웃이 깨질 때
```bash
# 원인:
- CSS 파일이 로드되지 않음
- 캐시 문제

# 해결 방법:
1. 캐시 삭제 (Ctrl+Shift+R 또는 Cmd+Shift+R)
2. CSS 파일 경로 확인
3. 개발자 도구에서 네트워크 탭 확인
```

### 4. Hero 배경 이미지가 느리게 로드될 때
```bash
# 해결 방법:
1. 이미지 최적화 (TinyPNG)
2. WebP 포맷으로 변환
3. 이미지 크기 조정 (1920x1080px 이하)
```

---

## 🚀 성능 최적화

### 1. 이미지 Lazy Loading
```html
<!-- index.php에 추가 -->
<img src="images/service-blog-optimization.jpg" loading="lazy" alt="...">
```

### 2. CDN 사용 (선택사항)
- Cloudflare (무료)
- Amazon CloudFront
- BunnyCDN

### 3. Gzip 압축 확인
```bash
# 서버에서 확인
curl -H "Accept-Encoding: gzip" -I https://yourdomain.com
```

### 4. 캐싱 확인
`.htaccess` 파일에 이미 설정되어 있음:
- 이미지: 1년
- CSS/JS: 1개월

---

## 📱 브라우저 지원
- ✅ Chrome (최신 버전)
- ✅ Firefox (최신 버전)
- ✅ Safari (최신 버전)
- ✅ Edge (최신 버전)
- ✅ 모바일 브라우저 (iOS Safari, Chrome Mobile, Samsung Internet)

---

## 🔐 보안 권장사항

### 1. HTTPS 사용 (필수)
- Let's Encrypt SSL 인증서 설치
- 클라우드웨이즈에서 무료 제공

### 2. 정기 백업
- 클라우드웨이즈 자동 백업 활성화
- 매일 자동 백업 권장

### 3. 파일 권한
```bash
디렉토리: 755
PHP 파일: 644
이미지 파일: 644
민감한 파일: 600
```

### 4. 보안 헤더
`.htaccess`에 이미 설정되어 있음:
- X-Frame-Options
- X-XSS-Protection
- X-Content-Type-Options

---

## 📞 지원 및 문의

### 사이트 관련 문의
- 카카오톡: pres00
- 전화: 010-3966-7687

### 기술 지원이 필요한 경우
1. 이미지 제작 및 디자인
2. 서버 설정 및 배포
3. 커스터마이징
4. 성능 최적화

---

## 📝 체크리스트

사이트 런칭 전 확인 사항:

### 이미지
- [ ] Hero 배경 이미지 (1920x1080px)
- [ ] 서비스 이미지 6개 (800x550px)
- [ ] 포트폴리오 이미지 3개 (800x600px)
- [ ] Feature 이미지 6개 (600x450px)
- [ ] About 이미지 (900x900px)
- [ ] Contact 이미지 (600x400px)
- [ ] 모든 이미지 최적화 완료

### 설정
- [ ] 연락처 정보 변경 (카카오톡, 전화번호)
- [ ] 회사명 확인
- [ ] 도메인 연결 완료
- [ ] SSL 인증서 설치
- [ ] HTTPS 리다이렉트 활성화

### 테스트
- [ ] 데스크톱에서 테스트
- [ ] 모바일에서 테스트
- [ ] 태블릿에서 테스트
- [ ] 문의 폼 작동 확인
- [ ] 모든 링크 작동 확인
- [ ] 이미지 로딩 확인
- [ ] 반응형 레이아웃 확인

### 성능
- [ ] 이미지 최적화 완료
- [ ] 페이지 로딩 속도 확인 (3초 이내)
- [ ] 모바일 로딩 속도 확인
- [ ] Gzip 압축 활성화 확인

### 보안
- [ ] SSL 인증서 설치 확인
- [ ] inquiries 폴더 접근 차단 확인
- [ ] .htaccess 보안 설정 확인
- [ ] 정기 백업 설정

---

## 라이선스
© 2024 Prestige Marketing. All rights reserved.

---

## 버전 정보
- **버전**: 2.0 (이미지 기반 리뉴얼)
- **최종 수정일**: 2024-12-05
- **제작**: Claude (Anthropic)
