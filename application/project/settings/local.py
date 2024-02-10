"""LOCAL環境用の設定"""
from .base import *

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]


DEBUG_TOOLBAR_CONFIG = {
    # ツールバーを表示させる
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

ROOT_URLCONF = "project.urls.local"

# Djangoのメールの設定
EMAIL_HOST = "mail"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
# SMTPの1025番ポートを指定
EMAIL_PORT = 1025
# 送信中の文章の暗号化をFalseにします
EMAIL_USE_TLS = False

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://127.0.0.1"]

# メールの設定
EMAIL_HOST = "mail"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_TLS = False
