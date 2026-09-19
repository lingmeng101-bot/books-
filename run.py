import config
import sqlite3
import requests
import logging
from fetcher import  fetch
from parser import parse_book, next_page_url
from storage import  link_exists, save_xia_xun, commit_db

log=logging.getLogger(config.LOG_NAME)

def crawl_and_save(session:requests.Session, start_url: str, max_pages: int,conn: sqlite3.Connection) -> tuple[int,int]:
    url = start_url
    added_count = 0
    page_count=0
    seen=set()
    malformed_count = 0
    while url and page_count<max_pages:
        log.info("[list %d/%d] %s", page_count + 1, max_pages, url)
        try:
            html=fetch(session, url)
        except requests.RequestException as e:
            log.error("列表页请求失败，本轮结束: %s (%s)", url, e)
            break
        items=parse_book(html,url)
        if not items:
            log.warning("列表页没解析出任何条目，页面结构可能变了: %s", url)

        for item in items:
            href=item["href"]
            if href in seen or link_exists(conn, href):
                continue
            seen.add(href)

            if not item['stock'] or not item['book_name']:
                access_status="malformed"

                save_xia_xun(
                    conn,
                    book_name=item['book_name'],
                    price=item['price'],
                    stock=item['stock'],
                    href= href,
                    img=item['img'],
                    star=item['star'],
                    access_status=access_status,
                )

                malformed_count += 1
                log.warning("[!] malformed 记录: %s", href)

                continue

            access_status = "normal"
            save_xia_xun(
                conn,
                book_name=item['book_name'],
                price=item['price'],
                stock=item['stock'],
                href=href,
                img=item['img'],
                star=item['star'],
                access_status=access_status,
            )
            added_count += 1
            log.info("  [+] %s 【%s】%s", access_status, item["book_name"], item["price"])
        commit_db(conn)
        url=next_page_url(html, url)
        page_count += 1
    if malformed_count > 0:
        log.warning("今日发现 %d 条解析异常（malformed），请检查解析器！", malformed_count)
    return added_count, malformed_count








