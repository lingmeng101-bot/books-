import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup

import config

log=logging.getLogger(config.LOG_NAME)
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def parse_book(html: str, url: str) -> list[dict]:
    try:
        soup = BeautifulSoup(html, 'lxml')
        log.debug("解析正常 url=%s", url)
        items=soup.select("article.product_pod")
        if not items:
            log.warning("未匹配到 article.product_pod, url=%s", url)
            return []
        data=[]
        for item in items:
            href_tag=item.select_one("div.image_container a")
            if not href_tag:
                href_tag=item.select_one("a[href*='/index.html']")

            img_tag=item.select_one("div.image_container a img")
            if not img_tag:
                img_tag=item.select_one("img[src*='.jpg']")

            book_name = item.select_one("h3 a")
            name=book_name.get("title") if book_name else ""
            if not name:
                name = img_tag.get("alt") if img_tag else ""

            price_tag=item.select_one("p.price_color")
            price=price_tag.text.strip() if price_tag else ""

            stock_tag = item.select_one("p.instock.availability")
            stock_status = stock_tag.get_text(strip=True) if stock_tag else ""

            rating_tag = item.select_one("p.star-rating")
            if rating_tag:
                class_num = rating_tag.get("class", [])
                rating_num = rating_map.get(class_num[1], 0) if len(class_num) > 1 else 0
            else:
                rating_num = 0

            href=href_tag.get("href") if href_tag else ""
            img=img_tag.get("src") if img_tag else ""
            href_url=urljoin(url,href)
            img_url=urljoin(url, img)
            out_dict={
                "book_name":name,
                "price":price,
                "stock":stock_status,
                "href":href_url,
                "img":img_url,
                "star":rating_num
            }
            data.append(out_dict)
        return data
    except Exception:
        log.exception("解析异常 url=%s", url)
        raise
def next_page_url(html:str,path_url:str) -> str | None:
    soup = BeautifulSoup(html, 'lxml')
    next_tag = soup.select_one("li.next a")
    if not next_tag:
        return None
    return urljoin(path_url, next_tag.get("href"))
