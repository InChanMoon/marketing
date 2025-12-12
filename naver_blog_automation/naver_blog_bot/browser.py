"""
봇 탐지 우회를 위한 셀레니움 브라우저 설정
"""
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random


class NaverBotBrowser:
    """
    네이버 봇 탐지를 우회하는 크롬 브라우저
    """

    def __init__(self, headless=False, incognito=True):
        """
        Args:
            headless: 헤드리스 모드 사용 여부 (False 권장, 봇 탐지에 걸릴 수 있음)
            incognito: 시크릿 모드 사용 여부
        """
        self.headless = headless
        self.incognito = incognito
        self.driver = None

    def create_driver(self):
        """
        봇 탐지 우회 설정이 적용된 드라이버 생성

        Returns:
            driver: undetected_chromedriver 인스턴스
        """
        options = uc.ChromeOptions()

        # 시크릿 모드
        if self.incognito:
            options.add_argument('--incognito')

        # 봇 탐지 우회를 위한 기본 설정
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')

        # 자동화 감지 비활성화
        options.add_argument('--disable-automation')
        options.add_argument('--disable-infobars')

        # 웹 보안 관련 (선택사항, 필요시 주석 해제)
        # options.add_argument('--disable-web-security')
        # options.add_argument('--allow-running-insecure-content')

        # User-Agent 랜덤화 (선택사항)
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ]
        # options.add_argument(f'user-agent={random.choice(user_agents)}')

        # 헤드리스 모드 (비권장 - 봇 탐지에 걸릴 수 있음)
        if self.headless:
            options.add_argument('--headless=new')

        # 알림 비활성화
        prefs = {
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.media_stream_mic': 2,
            'profile.default_content_setting_values.media_stream_camera': 2,
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        }
        options.add_experimental_option('prefs', prefs)

        # 자동화 플래그 제거
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # 윈도우 크기 설정 (일반적인 해상도)
        window_sizes = [
            (1920, 1080),
            (1366, 768),
            (1440, 900),
        ]
        window_size = random.choice(window_sizes)
        options.add_argument(f'--window-size={window_size[0]},{window_size[1]}')

        # undetected_chromedriver로 드라이버 생성
        try:
            driver = uc.Chrome(options=options, version_main=None)

            # JavaScript로 webdriver 속성 숨기기
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    });

                    // Chrome 객체 위장
                    window.chrome = {
                        runtime: {}
                    };

                    // Permissions 속성 오버라이드
                    const originalQuery = window.navigator.permissions.query;
                    window.navigator.permissions.query = (parameters) => (
                        parameters.name === 'notifications' ?
                            Promise.resolve({ state: Notification.permission }) :
                            originalQuery(parameters)
                    );

                    // Plugin 배열 위장
                    Object.defineProperty(navigator, 'plugins', {
                        get: () => [1, 2, 3, 4, 5]
                    });

                    // Languages 위장
                    Object.defineProperty(navigator, 'languages', {
                        get: () => ['ko-KR', 'ko', 'en-US', 'en']
                    });
                '''
            })

            self.driver = driver
            return driver

        except Exception as e:
            print(f"드라이버 생성 중 오류 발생: {str(e)}")
            raise

    def get_driver(self):
        """
        드라이버 반환 (없으면 생성)

        Returns:
            driver: 셀레니움 드라이버
        """
        if self.driver is None:
            return self.create_driver()
        return self.driver

    def close(self):
        """
        브라우저 종료
        """
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"브라우저 종료 중 오류: {str(e)}")
            finally:
                self.driver = None

    def __enter__(self):
        """
        Context manager 진입
        """
        return self.create_driver()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager 종료
        """
        self.close()
