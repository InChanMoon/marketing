#!/usr/bin/env python3
"""
네이버 로그인 테스트 스크립트
실제 계정으로 로그인이 되는지 간단히 테스트합니다.
"""
import sys
from getpass import getpass

from naver_blog_bot.browser import NaverBotBrowser
from naver_blog_bot.login import NaverLogin


def test_login():
    """
    로그인 테스트
    """
    print("\n" + "="*70)
    print("네이버 로그인 테스트")
    print("="*70 + "\n")

    # 계정 정보 입력
    username = input("네이버 아이디: ")
    password = getpass("비밀번호 (입력 시 보이지 않음): ")

    if not username or not password:
        print("아이디와 비밀번호를 모두 입력해주세요.")
        return False

    browser = None

    try:
        print("\n브라우저 시작 중...")
        browser = NaverBotBrowser(headless=False, incognito=True)
        driver = browser.create_driver()

        print("로그인 시도 중...")
        login_handler = NaverLogin(driver)

        if login_handler.login(username, password, wait_after_login=5):
            print("\n" + "="*70)
            print("✓ 로그인 테스트 성공!")
            print("="*70)

            # 사용자가 확인할 수 있도록 대기
            input("\n브라우저를 확인하세요. 종료하려면 Enter를 누르세요...")

            return True
        else:
            print("\n" + "="*70)
            print("✗ 로그인 테스트 실패")
            print("="*70)

            # 브라우저를 열어둬서 사용자가 문제를 확인할 수 있게 함
            input("\n브라우저를 확인하세요. 종료하려면 Enter를 누르세요...")

            return False

    except KeyboardInterrupt:
        print("\n\n테스트가 중단되었습니다.")
        return False

    except Exception as e:
        print(f"\n오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        if browser:
            print("\n브라우저 종료 중...")
            browser.close()


def main():
    """
    메인 함수
    """
    success = test_login()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
