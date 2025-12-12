"""
네이버 로그인 자동화
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .utils import paste_text, random_delay, human_like_delay, safe_click, check_element_exists


class NaverLogin:
    """
    네이버 로그인 자동화 클래스
    """

    # 네이버 로그인 URL
    LOGIN_URL = "https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsection.blog.naver.com%2FBlogHome.naver"

    # 로그인 폼 셀렉터
    ID_INPUT_SELECTOR = "#id"
    PW_INPUT_SELECTOR = "#pw"
    LOGIN_BUTTON_SELECTOR = "#log\\.login"

    def __init__(self, driver):
        """
        Args:
            driver: 셀레니움 드라이버
        """
        self.driver = driver

    def login(self, username, password, wait_after_login=5):
        """
        네이버 로그인 수행

        Args:
            username: 네이버 아이디
            password: 네이버 비밀번호
            wait_after_login: 로그인 후 대기 시간 (초)

        Returns:
            bool: 로그인 성공 여부
        """
        try:
            print(f"[로그인 시도] 아이디: {username}")

            # 로그인 페이지 접속
            self.driver.get(self.LOGIN_URL)
            human_like_delay()

            # 페이지 로딩 대기
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.ID_INPUT_SELECTOR))
            )
            random_delay(1, 2)

            # 아이디 입력
            print("아이디 입력 중...")
            id_input = self.driver.find_element(By.CSS_SELECTOR, self.ID_INPUT_SELECTOR)
            paste_text(self.driver, id_input, username)
            random_delay(0.8, 1.5)

            # 비밀번호 입력
            print("비밀번호 입력 중...")
            pw_input = self.driver.find_element(By.CSS_SELECTOR, self.PW_INPUT_SELECTOR)
            paste_text(self.driver, pw_input, password)
            random_delay(1, 2)

            # 로그인 버튼 클릭
            print("로그인 버튼 클릭...")
            login_success = safe_click(
                self.driver,
                self.LOGIN_BUTTON_SELECTOR,
                by="css",
                timeout=10
            )

            if not login_success:
                print("로그인 버튼 클릭 실패")
                return False

            # 로그인 후 대기
            random_delay(wait_after_login, wait_after_login + 2)

            # 로그인 성공 여부 확인
            if self._check_login_success():
                print(f"✓ 로그인 성공: {username}")
                return True
            else:
                print(f"✗ 로그인 실패: {username}")
                return False

        except TimeoutException as e:
            print(f"타임아웃 오류: {str(e)}")
            return False
        except Exception as e:
            print(f"로그인 중 오류 발생: {str(e)}")
            return False

    def _check_login_success(self):
        """
        로그인 성공 여부 확인

        Returns:
            bool: 로그인 성공 여부
        """
        try:
            # 로그인 실패 시 나타나는 에러 메시지 확인
            error_selectors = [
                ".error_message",
                ".input_error",
                "#err_common"
            ]

            for selector in error_selectors:
                error_element = check_element_exists(self.driver, selector, timeout=2)
                if error_element and error_element.is_displayed():
                    error_text = error_element.text
                    print(f"로그인 오류 메시지: {error_text}")
                    return False

            # 현재 URL 확인 (로그인 성공 시 리다이렉트됨)
            current_url = self.driver.current_url
            if "nid.naver.com/nidlogin.login" not in current_url:
                # 로그인 페이지가 아니면 성공으로 간주
                return True

            # 추가 확인: 로그인 폼이 여전히 존재하는지
            id_input = check_element_exists(self.driver, self.ID_INPUT_SELECTOR, timeout=3)
            if id_input is None:
                # 로그인 폼이 없으면 성공
                return True

            # 확실하지 않은 경우
            return False

        except Exception as e:
            print(f"로그인 확인 중 오류: {str(e)}")
            # 오류 발생 시 현재 URL로 판단
            return "nid.naver.com/nidlogin.login" not in self.driver.current_url

    def handle_captcha_or_verification(self):
        """
        캡챠나 추가 인증이 필요한 경우 사용자에게 알림
        (수동으로 처리해야 함)

        Returns:
            bool: 사용자가 처리 완료했는지 여부
        """
        print("\n" + "="*50)
        print("⚠️  추가 인증이 필요할 수 있습니다.")
        print("캡챠나 본인 확인이 있다면 수동으로 처리해주세요.")
        print("="*50 + "\n")

        input("처리 완료 후 Enter를 눌러주세요...")
        return True

    def is_logged_in(self):
        """
        현재 로그인 상태인지 확인

        Returns:
            bool: 로그인 여부
        """
        try:
            # 네이버 메인 페이지로 이동
            self.driver.get("https://www.naver.com")
            random_delay(2, 3)

            # 로그인 버튼이 있는지 확인 (로그아웃 상태)
            login_button = check_element_exists(
                self.driver,
                "a[href*='nid.naver.com/nidlogin']",
                timeout=3
            )

            # 로그인 버튼이 없으면 로그인 상태
            return login_button is None

        except Exception as e:
            print(f"로그인 상태 확인 중 오류: {str(e)}")
            return False

    def logout(self):
        """
        네이버 로그아웃
        """
        try:
            print("로그아웃 중...")
            self.driver.get("https://nid.naver.com/nidlogin.logout")
            random_delay(2, 3)
            print("✓ 로그아웃 완료")
            return True
        except Exception as e:
            print(f"로그아웃 중 오류: {str(e)}")
            return False
