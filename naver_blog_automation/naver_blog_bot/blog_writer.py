"""
네이버 블로그 글쓰기 자동화
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .utils import (
    paste_text,
    random_delay,
    human_like_delay,
    safe_click,
    check_element_exists,
    switch_to_iframe,
    switch_to_default_content
)


class NaverBlogWriter:
    """
    네이버 블로그 글쓰기 자동화 클래스
    """

    # 블로그 글쓰기 URL
    BLOG_WRITE_URL = "https://blog.naver.com/GoBlogWrite.naver"

    # iframe 및 팝업 셀렉터
    IFRAME_SELECTOR = "#mainFrame"
    POPUP_CANCEL_SELECTOR = ".se-popup-button_cancel"
    HELP_CLOSE_SELECTOR = ".se-help-panel-close-button"

    # 글쓰기 셀렉터
    TITLE_SELECTOR = ".se-section-documentTitle"
    CONTENT_SELECTOR = ".se-section-text"

    # 발행 버튼 셀렉터 (여러 버전)
    PUBLISH_BUTTON_SELECTORS = [
        "button[data-click-area='tpb.publish']",
        "button[class*='publish_btn']"
    ]

    FINAL_PUBLISH_BUTTON_SELECTOR = "button[data-testid='seOnePublishBtn']"

    def __init__(self, driver):
        """
        Args:
            driver: 셀레니움 드라이버
        """
        self.driver = driver

    def navigate_to_write_page(self):
        """
        블로그 글쓰기 페이지로 이동

        Returns:
            bool: 이동 성공 여부
        """
        try:
            print("블로그 글쓰기 페이지로 이동 중...")
            self.driver.get(self.BLOG_WRITE_URL)
            random_delay(3, 5)

            # iframe 전환
            if not switch_to_iframe(self.driver, self.IFRAME_SELECTOR, timeout=15):
                print("iframe 전환 실패")
                return False

            print("✓ iframe 전환 완료")
            random_delay(1, 2)

            # 팝업 및 도움말 닫기
            self._close_popups()

            return True

        except Exception as e:
            print(f"글쓰기 페이지 이동 중 오류: {str(e)}")
            return False

    def _close_popups(self):
        """
        팝업 및 도움말 패널 닫기
        """
        # 팝업 취소 버튼
        popup_cancel = check_element_exists(
            self.driver,
            self.POPUP_CANCEL_SELECTOR,
            timeout=3
        )
        if popup_cancel:
            try:
                popup_cancel.click()
                print("✓ 팝업 닫기 완료")
                random_delay(0.5, 1)
            except Exception as e:
                print(f"팝업 닫기 실패: {str(e)}")

        # 도움말 패널 닫기
        help_close = check_element_exists(
            self.driver,
            self.HELP_CLOSE_SELECTOR,
            timeout=3
        )
        if help_close:
            try:
                help_close.click()
                print("✓ 도움말 닫기 완료")
                random_delay(0.5, 1)
            except Exception as e:
                print(f"도움말 닫기 실패: {str(e)}")

    def write_post(self, title, content):
        """
        블로그 글 작성

        Args:
            title: 제목
            content: 내용

        Returns:
            bool: 작성 성공 여부
        """
        try:
            print(f"\n[글 작성 시작]")
            print(f"제목: {title[:30]}...")

            # 제목 입력
            print("제목 입력 중...")
            title_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE_SELECTOR))
            )
            paste_text(self.driver, title_element, title)
            random_delay(1, 2)

            # 내용 입력
            print("내용 입력 중...")
            content_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CONTENT_SELECTOR))
            )
            paste_text(self.driver, content_element, content)
            random_delay(2, 3)

            print("✓ 글 작성 완료")
            return True

        except TimeoutException as e:
            print(f"타임아웃 오류: {str(e)}")
            return False
        except Exception as e:
            print(f"글 작성 중 오류: {str(e)}")
            return False

    def publish_post(self):
        """
        작성한 글 발행

        Returns:
            bool: 발행 성공 여부
        """
        try:
            print("\n[발행 시작]")

            # iframe에서 나오기 (발행 버튼은 메인 페이지에 있음)
            switch_to_default_content(self.driver)
            random_delay(1, 2)

            # 발행 버튼 클릭 (여러 셀렉터 시도)
            publish_clicked = False
            for selector in self.PUBLISH_BUTTON_SELECTORS:
                print(f"발행 버튼 찾는 중: {selector}")
                if safe_click(self.driver, selector, by="css", timeout=5):
                    print("✓ 발행 버튼 클릭 완료")
                    publish_clicked = True
                    break

            if not publish_clicked:
                print("✗ 발행 버튼을 찾을 수 없습니다")
                return False

            random_delay(2, 3)

            # 최종 발행 버튼 클릭
            print("최종 발행 버튼 클릭 중...")
            if safe_click(
                self.driver,
                self.FINAL_PUBLISH_BUTTON_SELECTOR,
                by="css",
                timeout=10
            ):
                print("✓ 최종 발행 완료")
                random_delay(3, 5)
                return True
            else:
                print("✗ 최종 발행 버튼 클릭 실패")
                return False

        except Exception as e:
            print(f"발행 중 오류: {str(e)}")
            return False

    def write_and_publish(self, title, content):
        """
        글쓰기부터 발행까지 전체 프로세스

        Args:
            title: 제목
            content: 내용

        Returns:
            bool: 성공 여부
        """
        try:
            # 글쓰기 페이지로 이동
            if not self.navigate_to_write_page():
                return False

            # 글 작성
            if not self.write_post(title, content):
                return False

            # 발행
            if not self.publish_post():
                return False

            print("\n" + "="*50)
            print("✓ 블로그 글 작성 및 발행 성공!")
            print("="*50 + "\n")
            return True

        except Exception as e:
            print(f"\n발행 프로세스 중 오류: {str(e)}\n")
            return False

    def save_as_draft(self):
        """
        임시저장 (향후 구현)

        Returns:
            bool: 성공 여부
        """
        # TODO: 임시저장 기능 구현
        print("임시저장 기능은 아직 구현되지 않았습니다.")
        return False

    def upload_image(self, image_path):
        """
        이미지 업로드 (향후 구현)

        Args:
            image_path: 이미지 파일 경로

        Returns:
            bool: 성공 여부
        """
        # TODO: 이미지 업로드 기능 구현
        print("이미지 업로드 기능은 아직 구현되지 않았습니다.")
        return False

    def set_category(self, category_name):
        """
        카테고리 설정 (향후 구현)

        Args:
            category_name: 카테고리 이름

        Returns:
            bool: 성공 여부
        """
        # TODO: 카테고리 설정 기능 구현
        print("카테고리 설정 기능은 아직 구현되지 않았습니다.")
        return False

    def add_tags(self, tags):
        """
        태그 추가 (향후 구현)

        Args:
            tags: 태그 리스트

        Returns:
            bool: 성공 여부
        """
        # TODO: 태그 추가 기능 구현
        print("태그 추가 기능은 아직 구현되지 않았습니다.")
        return False
