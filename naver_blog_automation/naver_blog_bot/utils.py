"""
유틸리티 함수 모음
"""
import time
import random
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def random_delay(min_sec=1.0, max_sec=3.0):
    """
    사람처럼 보이기 위한 랜덤 지연시간

    Args:
        min_sec: 최소 지연 시간 (초)
        max_sec: 최대 지연 시간 (초)
    """
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)


def human_like_delay():
    """
    더욱 인간적인 지연 패턴 (0.5 ~ 2.5초)
    """
    random_delay(0.5, 2.5)


def paste_text(driver, element, text):
    """
    send_keys 대신 복사/붙여넣기로 텍스트 입력
    봇 탐지를 우회하기 위한 방법

    Args:
        driver: 셀레니움 드라이버
        element: 입력할 웹 엘리먼트
        text: 입력할 텍스트
    """
    # 클립보드에 텍스트 복사
    pyperclip.copy(text)

    # 엘리먼트 클릭
    element.click()
    human_like_delay()

    # ActionChains를 사용한 붙여넣기
    actions = ActionChains(driver)

    # Ctrl+A로 기존 텍스트 선택 (있을 경우를 대비)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(0.3)

    # Ctrl+V로 붙여넣기
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(0.5)


def safe_click(driver, selector, by="css", timeout=10, click_delay=True):
    """
    안전한 클릭 (요소가 클릭 가능할 때까지 대기)

    Args:
        driver: 셀레니움 드라이버
        selector: CSS 선택자 또는 XPath
        by: 선택자 타입 ("css" 또는 "xpath")
        timeout: 대기 시간 (초)
        click_delay: 클릭 후 지연 여부

    Returns:
        bool: 클릭 성공 여부
    """
    try:
        from selenium.webdriver.common.by import By

        by_type = By.CSS_SELECTOR if by == "css" else By.XPATH

        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by_type, selector))
        )

        # 사람처럼 마우스를 움직여서 클릭
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(random.uniform(0.1, 0.3)).click().perform()

        if click_delay:
            human_like_delay()

        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"클릭 실패 - {selector}: {str(e)}")
        return False


def check_element_exists(driver, selector, by="css", timeout=5):
    """
    요소 존재 여부 확인

    Args:
        driver: 셀레니움 드라이버
        selector: CSS 선택자 또는 XPath
        by: 선택자 타입
        timeout: 대기 시간 (초)

    Returns:
        element or None: 요소가 있으면 반환, 없으면 None
    """
    try:
        from selenium.webdriver.common.by import By

        by_type = By.CSS_SELECTOR if by == "css" else By.XPATH

        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by_type, selector))
        )
        return element
    except TimeoutException:
        return None


def switch_to_iframe(driver, iframe_selector, timeout=10):
    """
    iframe으로 전환

    Args:
        driver: 셀레니움 드라이버
        iframe_selector: iframe 선택자
        timeout: 대기 시간 (초)

    Returns:
        bool: 전환 성공 여부
    """
    try:
        from selenium.webdriver.common.by import By

        iframe = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
        )
        driver.switch_to.frame(iframe)
        return True
    except TimeoutException:
        print(f"iframe 전환 실패: {iframe_selector}")
        return False


def switch_to_default_content(driver):
    """
    메인 컨텐츠로 전환 (iframe에서 나오기)
    """
    driver.switch_to.default_content()


def scroll_slowly(driver, scroll_pause_time=0.5):
    """
    페이지를 천천히 스크롤 (사람처럼 보이기 위해)

    Args:
        driver: 셀레니움 드라이버
        scroll_pause_time: 스크롤 간 대기 시간
    """
    # 현재 스크롤 높이 가져오기
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 천천히 스크롤
    scroll_step = random.randint(300, 500)
    current_position = 0

    while current_position < last_height:
        current_position += scroll_step
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(scroll_pause_time)

        # 새로운 높이 확인 (동적 컨텐츠 로딩 대비)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height > last_height:
            last_height = new_height


def mouse_move_to_element(driver, element):
    """
    요소로 마우스를 자연스럽게 이동

    Args:
        driver: 셀레니움 드라이버
        element: 대상 엘리먼트
    """
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(random.uniform(0.1, 0.4)).perform()
