import logging

import config
from fetcher import make_session
from log import setup_logger
from run import crawl_and_save
from storage import commit_db, get_unpushed, init_db, mark_pushed

log=logging.getLogger(config.LOG_NAME)

def main():
    setup_logger()
    log.info("初始化完成,开始运行")

    session=make_session()
    conn=init_db()
    try:
        added,malformed=crawl_and_save(session,config.BASE_URL,config.MAX_PAGES,conn)
        log.info("爬虫完成: 新增%d 条 , 收容 %d 条",added,malformed)

        rows=get_unpushed(conn)
        if not rows:
            log.info("书本信息没有更新")
            return

        for id_ in rows:
            mark_pushed(conn,id_[0])
        commit_db(conn)
        log.info("运行成功")

    except Exception:

        log.exception("运行失败")
        raise
    finally:
        conn.close()
        session.close()

if __name__ == '__main__':
    main()



