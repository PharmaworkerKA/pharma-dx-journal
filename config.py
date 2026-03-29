"""製薬DXジャーナル - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "製薬DXジャーナル"
BLOG_DESCRIPTION = (
    "製薬業界のデジタルトランスフォーメーション（DX）最新動向を毎日更新。"
    "海外のAI創薬・DCT・RWD活用の最新トレンドを日本語で翻訳・要約し実践的に解説。"
)
BLOG_URL = "https://musclelove-777.github.io/pharma-dx-journal"
BLOG_TAGLINE = "製薬DXの最新トレンドを日本語で毎日発信"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/pharma-dx-journal"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "AI創薬・機械学習",
    "DCT（分散型臨床試験）",
    "RWD/RWE活用",
    "クラウド・データ基盤",
    "CSV・規制対応DX",
    "製薬DX最新ニュース",
    "デジタルバイオマーカー",
    "海外トレンド翻訳",
]

THEME = {
    "primary": "#0891b2",
    "accent": "#065f6b",
    "gradient_start": "#0891b2",
    "gradient_end": "#0e7490",
    "dark_bg": "#0c1a24",
    "dark_surface": "#1a2e3b",
    "light_bg": "#f0fdfa",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Amazon AI/DX書籍": {
        "url": "https://www.amazon.co.jp",
        "text": "AmazonでAI・DX関連書籍を探す",
        "description": "AI創薬・製薬DXの参考書",
    },
    "Udemy AI・データサイエンス講座": {
        "url": "https://www.udemy.com",
        "text": "UdemyでAI・データサイエンス講座を探す",
        "description": "動画で学ぶ製薬AI・DX実践",
    },
    "楽天 DX書籍": {
        "url": "https://www.rakuten.co.jp",
        "text": "楽天でDX関連書籍を探す",
        "description": "デジタルトランスフォーメーションの参考書",
    },
    "AWS認定": {
        "url": "https://aws.amazon.com/jp/certification/",
        "text": "AWS認定資格を取得する",
        "description": "クラウドスキルの公式認定",
    },
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)

DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 8095
