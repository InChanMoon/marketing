#!/usr/bin/env python3
"""
네이버 블로그 자동화 메인 스크립트
"""
import json
import time
import argparse
from pathlib import Path

from naver_blog_bot.browser import NaverBotBrowser
from naver_blog_bot.login import NaverLogin
from naver_blog_bot.blog_writer import NaverBlogWriter
from naver_blog_bot.config import Config, AccountManager
from naver_blog_bot.utils import random_delay


def load_posts(posts_file="posts.json"):
    """
    포스트 파일 로드

    Args:
        posts_file: 포스트 파일 경로

    Returns:
        list: 포스트 리스트
    """
    posts_path = Path(posts_file)

    if not posts_path.exists():
        print(f"포스트 파일이 없습니다: {posts_file}")
        return []

    try:
        with open(posts_path, 'r', encoding='utf-8') as f:
            posts = json.load(f)
        print(f"✓ 포스트 파일 로드 완료: {len(posts)}개 포스트")
        return posts
    except Exception as e:
        print(f"포스트 파일 로드 중 오류: {str(e)}")
        return []


def get_enabled_posts(posts):
    """
    활성화된 포스트만 필터링

    Args:
        posts: 포스트 리스트

    Returns:
        list: 활성화된 포스트 리스트
    """
    return [post for post in posts if post.get("enabled", True)]


def run_single_account(username, password, posts, config):
    """
    단일 계정으로 블로그 자동화 실행

    Args:
        username: 네이버 아이디
        password: 네이버 비밀번호
        posts: 발행할 포스트 리스트
        config: 설정 객체

    Returns:
        dict: 실행 결과
    """
    result = {
        "username": username,
        "success": False,
        "posts_published": 0,
        "posts_failed": 0,
        "error": None
    }

    browser = None
    driver = None

    try:
        print("\n" + "="*70)
        print(f"계정: {username} - 작업 시작")
        print("="*70)

        # 브라우저 생성
        headless = config.get("browser.headless", False)
        incognito = config.get("browser.incognito", True)

        browser = NaverBotBrowser(headless=headless, incognito=incognito)
        driver = browser.create_driver()

        # 로그인
        login_handler = NaverLogin(driver)
        wait_after_login = config.get("delays.wait_after_login", 5)

        if not login_handler.login(username, password, wait_after_login):
            result["error"] = "로그인 실패"
            return result

        # 블로그 글쓰기
        blog_writer = NaverBlogWriter(driver)

        for idx, post in enumerate(posts, 1):
            print(f"\n[{idx}/{len(posts)}] 포스트 작성 중...")

            title = post.get("title", "")
            content = post.get("content", "")

            if not title or not content:
                print("제목 또는 내용이 없어 건너뜁니다.")
                result["posts_failed"] += 1
                continue

            # 포스트 작성 및 발행
            if blog_writer.write_and_publish(title, content):
                result["posts_published"] += 1
                print(f"✓ 포스트 발행 성공 ({result['posts_published']}/{len(posts)})")
            else:
                result["posts_failed"] += 1
                print(f"✗ 포스트 발행 실패")

            # 다음 포스트 전 대기
            if idx < len(posts):
                wait_time = config.get("delays.wait_after_publish", 10)
                print(f"\n다음 포스트까지 {wait_time}초 대기...")
                random_delay(wait_time, wait_time + 3)

        # 로그아웃
        login_handler.logout()

        result["success"] = True
        print("\n" + "="*70)
        print(f"✓ 계정 {username} 작업 완료")
        print(f"  - 성공: {result['posts_published']}개")
        print(f"  - 실패: {result['posts_failed']}개")
        print("="*70)

    except Exception as e:
        result["error"] = str(e)
        print(f"\n✗ 오류 발생: {str(e)}")

    finally:
        # 브라우저 종료
        if browser:
            browser.close()

    return result


def run_automation(config_file="config.json", accounts_file="accounts.json", posts_file="posts.json"):
    """
    전체 자동화 프로세스 실행

    Args:
        config_file: 설정 파일 경로
        accounts_file: 계정 파일 경로
        posts_file: 포스트 파일 경로

    Returns:
        list: 각 계정별 실행 결과
    """
    print("\n" + "="*70)
    print("네이버 블로그 자동화 프로그램 시작")
    print("="*70 + "\n")

    # 설정 로드
    config = Config(config_file)

    # 계정 로드
    account_manager = AccountManager(accounts_file)
    accounts = account_manager.get_enabled_accounts()

    if not accounts:
        print("활성화된 계정이 없습니다.")
        return []

    print(f"✓ {len(accounts)}개 계정 로드 완료")

    # 포스트 로드
    posts = load_posts(posts_file)
    enabled_posts = get_enabled_posts(posts)

    if not enabled_posts:
        print("발행할 포스트가 없습니다.")
        return []

    print(f"✓ {len(enabled_posts)}개 포스트 로드 완료\n")

    # 각 계정별로 실행
    results = []

    for idx, account in enumerate(accounts, 1):
        username = account.get("username")
        password = account.get("password")

        if not username or not password:
            print(f"계정 정보가 불완전합니다: {account}")
            continue

        print(f"\n[{idx}/{len(accounts)}] 계정 처리 중...")

        # 계정별 실행
        result = run_single_account(username, password, enabled_posts, config)
        results.append(result)

        # 다음 계정 전 대기 (마지막 계정이 아닌 경우)
        if idx < len(accounts):
            wait_time = 30  # 계정 간 대기 시간
            print(f"\n다음 계정까지 {wait_time}초 대기...")
            time.sleep(wait_time)

    # 전체 결과 출력
    print("\n" + "="*70)
    print("전체 작업 완료")
    print("="*70)

    for result in results:
        status = "✓ 성공" if result["success"] else "✗ 실패"
        print(f"{status} - {result['username']}: {result['posts_published']}개 발행, {result['posts_failed']}개 실패")
        if result["error"]:
            print(f"  에러: {result['error']}")

    print("="*70 + "\n")

    return results


def main():
    """
    메인 함수
    """
    parser = argparse.ArgumentParser(description="네이버 블로그 자동화 프로그램")

    parser.add_argument(
        "--config",
        default="config.json",
        help="설정 파일 경로 (기본값: config.json)"
    )

    parser.add_argument(
        "--accounts",
        default="accounts.json",
        help="계정 파일 경로 (기본값: accounts.json)"
    )

    parser.add_argument(
        "--posts",
        default="posts.json",
        help="포스트 파일 경로 (기본값: posts.json)"
    )

    parser.add_argument(
        "--test",
        action="store_true",
        help="테스트 모드 (단일 계정, 단일 포스트만 실행)"
    )

    args = parser.parse_args()

    # 자동화 실행
    try:
        results = run_automation(
            config_file=args.config,
            accounts_file=args.accounts,
            posts_file=args.posts
        )

        # 성공/실패 통계
        total_success = sum(1 for r in results if r["success"])
        total_failed = len(results) - total_success

        print(f"\n최종 결과: {total_success}개 계정 성공, {total_failed}개 계정 실패")

    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n오류 발생: {str(e)}")


if __name__ == "__main__":
    main()
