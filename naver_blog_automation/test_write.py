#!/usr/bin/env python3
"""
네이버 블로그 글쓰기 테스트 스크립트
실제 계정으로 로그인 후 테스트 글을 작성합니다. (발행은 하지 않음)
"""
import sys
from getpass import getpass

from naver_blog_bot.browser import NaverBotBrowser
from naver_blog_bot.login import NaverLogin
from naver_blog_bot.blog_writer import NaverBlogWriter


def test_write():
    """
    블로그 글쓰기 테스트
    """
    print("\n" + "="*70)
    print("네이버 블로그 글쓰기 테스트")
    print("="*70 + "\n")

    # 계정 정보 입력
    username = input("네이버 아이디: ")
    password = getpass("비밀번호 (입력 시 보이지 않음): ")

    if not username or not password:
        print("아이디와 비밀번호를 모두 입력해주세요.")
        return False

    # 테스트 포스트 내용
    test_title = "[테스트] 자동화 테스트 포스트"
    test_content = """이것은 자동화 테스트 포스트입니다.

실제로 발행되지는 않으니 안심하세요.

테스트가 끝나면 브라우저를 닫아주세요."""

    browser = None

    try:
        print("\n브라우저 시작 중...")
        browser = NaverBotBrowser(headless=False, incognito=True)
        driver = browser.create_driver()

        # 로그인
        print("로그인 시도 중...")
        login_handler = NaverLogin(driver)

        if not login_handler.login(username, password, wait_after_login=5):
            print("로그인 실패")
            return False

        print("✓ 로그인 성공")

        # 블로그 글쓰기 페이지로 이동
        print("\n블로그 글쓰기 페이지로 이동 중...")
        blog_writer = NaverBlogWriter(driver)

        if not blog_writer.navigate_to_write_page():
            print("글쓰기 페이지 이동 실패")
            return False

        print("✓ 글쓰기 페이지 이동 성공")

        # 글 작성 (발행은 안 함)
        print("\n테스트 글 작성 중...")
        if blog_writer.write_post(test_title, test_content):
            print("\n" + "="*70)
            print("✓ 글쓰기 테스트 성공!")
            print("="*70)
            print("\n주의: 발행 버튼을 누르지 않았으므로 실제로 발행되지 않았습니다.")
            print("브라우저에서 작성된 내용을 확인하세요.")

            input("\n확인 후 Enter를 누르면 종료됩니다...")
            return True
        else:
            print("✗ 글쓰기 실패")
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
    success = test_write()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
