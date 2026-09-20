BASE_URL = "https://books.toscrape.com/"
#数据库
DB_NAME="books.db"
MAX_PAGES = 50
#时间参数
DELAY_MIN = 1.0
DELAY_MAX = 2.0
TIMEOUT_CONNECT = 5
TIMEOUT_READ = 15
#请求参数
RETRY_TOTAL = 3
RETRY_BACKOFF = 1
RETRY_STATUS = (429, 500, 502, 503, 504)
#日志参数
LOG_NAME="xun"
LOG_FILE="book.log"
LOG_LEVEL="INFO"
LOG_FMT = "%(asctime)s %(name)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
LOG_DATE_FMT="%Y-%m-%d %H:%M:%S"
#随机UA
USER_AGENTS = [
    # Chrome 148 - Windows 11
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    # Chrome 148 - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    # Chrome 148 - Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    # Edge 150 - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.4078.99",
    # Firefox 152 - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0",
    # Firefox 152 - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0",
    # Firefox 152 - Ubuntu Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0",
    # Safari 26.0 - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15",
]