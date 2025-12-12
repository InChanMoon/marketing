"""
설정 파일 관리
"""
import json
import os
from pathlib import Path


class Config:
    """
    프로그램 설정 관리 클래스
    """

    def __init__(self, config_path="config.json"):
        """
        Args:
            config_path: 설정 파일 경로
        """
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self):
        """
        설정 파일 로드

        Returns:
            dict: 설정 딕셔너리
        """
        if not self.config_path.exists():
            print(f"설정 파일이 없습니다: {self.config_path}")
            return self._get_default_config()

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"✓ 설정 파일 로드 완료: {self.config_path}")
            return config
        except Exception as e:
            print(f"설정 파일 로드 중 오류: {str(e)}")
            return self._get_default_config()

    def _get_default_config(self):
        """
        기본 설정 반환

        Returns:
            dict: 기본 설정 딕셔너리
        """
        return {
            "browser": {
                "headless": False,
                "incognito": True,
                "window_size": "1920x1080"
            },
            "delays": {
                "min_delay": 1.0,
                "max_delay": 3.0,
                "wait_after_login": 5,
                "wait_after_publish": 10
            },
            "content_generation": {
                "mode": "manual",  # manual, ai_keyword, ai_custom
                "api_provider": None,  # openai, anthropic, etc
                "api_key": None
            },
            "ip_rotation": {
                "enabled": False,
                "method": None,  # android_phone, proxy_service
                "proxy_list": []
            },
            "logging": {
                "enabled": True,
                "log_file": "naver_blog_bot.log",
                "level": "INFO"
            }
        }

    def save_config(self, config_dict=None):
        """
        설정 파일 저장

        Args:
            config_dict: 저장할 설정 (None이면 현재 설정 저장)

        Returns:
            bool: 저장 성공 여부
        """
        try:
            config_to_save = config_dict if config_dict else self.config

            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config_to_save, f, indent=4, ensure_ascii=False)

            print(f"✓ 설정 파일 저장 완료: {self.config_path}")
            return True
        except Exception as e:
            print(f"설정 파일 저장 중 오류: {str(e)}")
            return False

    def get(self, key, default=None):
        """
        설정 값 가져오기 (점 표기법 지원)

        Args:
            key: 설정 키 (예: "browser.headless")
            default: 기본값

        Returns:
            설정 값
        """
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        """
        설정 값 설정하기 (점 표기법 지원)

        Args:
            key: 설정 키 (예: "browser.headless")
            value: 설정 값
        """
        keys = key.split('.')
        config = self.config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value


class AccountManager:
    """
    계정 관리 클래스
    """

    def __init__(self, accounts_path="accounts.json"):
        """
        Args:
            accounts_path: 계정 파일 경로
        """
        self.accounts_path = Path(accounts_path)
        self.accounts = self._load_accounts()

    def _load_accounts(self):
        """
        계정 파일 로드

        Returns:
            list: 계정 리스트
        """
        if not self.accounts_path.exists():
            print(f"계정 파일이 없습니다: {self.accounts_path}")
            return []

        try:
            with open(self.accounts_path, 'r', encoding='utf-8') as f:
                accounts = json.load(f)
            print(f"✓ 계정 파일 로드 완료: {len(accounts)}개 계정")
            return accounts
        except Exception as e:
            print(f"계정 파일 로드 중 오류: {str(e)}")
            return []

    def save_accounts(self, accounts_list=None):
        """
        계정 파일 저장

        Args:
            accounts_list: 저장할 계정 리스트 (None이면 현재 계정 저장)

        Returns:
            bool: 저장 성공 여부
        """
        try:
            accounts_to_save = accounts_list if accounts_list else self.accounts

            with open(self.accounts_path, 'w', encoding='utf-8') as f:
                json.dump(accounts_to_save, f, indent=4, ensure_ascii=False)

            print(f"✓ 계정 파일 저장 완료: {self.accounts_path}")
            return True
        except Exception as e:
            print(f"계정 파일 저장 중 오류: {str(e)}")
            return False

    def get_accounts(self):
        """
        모든 계정 가져오기

        Returns:
            list: 계정 리스트
        """
        return self.accounts

    def add_account(self, username, password):
        """
        계정 추가

        Args:
            username: 아이디
            password: 비밀번호

        Returns:
            bool: 추가 성공 여부
        """
        account = {
            "username": username,
            "password": password,
            "enabled": True
        }

        self.accounts.append(account)
        return self.save_accounts()

    def remove_account(self, username):
        """
        계정 제거

        Args:
            username: 아이디

        Returns:
            bool: 제거 성공 여부
        """
        self.accounts = [
            acc for acc in self.accounts
            if acc.get("username") != username
        ]
        return self.save_accounts()

    def get_enabled_accounts(self):
        """
        활성화된 계정만 가져오기

        Returns:
            list: 활성화된 계정 리스트
        """
        return [
            acc for acc in self.accounts
            if acc.get("enabled", True)
        ]
