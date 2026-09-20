import sqlite3

import config

SCHEMA="""
    CREATE TABLE IF NOT EXISTS XIA_XUN(
    ID INTEGER NOT NULL PRIMARY KEY ,
    book_name TEXT ,
    price TEXT ,
    stock TEXT ,
    href TEXT NOT NULL ,
    img TEXT ,
    star INTEGER  ,
    access_status TEXT DEFAULT 'normal',
    pushed INTEGER DEFAULT 0,
    UNIQUE(href))"""

def init_db()-> sqlite3.Connection:
    conn = sqlite3.connect(config.DB_NAME)
    c = conn.cursor()
    c.execute(SCHEMA)
    conn.commit()
    return conn

#储存
def save_xia_xun(
        conn: sqlite3.Connection,
        book_name: str,
        price: str,
        stock: str,
        href: str,
        img: str,
        star: int,
        access_status: str,) -> None:

    c = conn.cursor()

    c.execute(
        """INSERT INTO XIA_XUN(book_name, price, stock, href, img, star, access_status)
           VALUES (?,?,?,?,?,?,?)
           ON CONFLICT (href) DO UPDATE SET
               book_name = excluded.book_name,
               price = excluded.price,
               stock = excluded.stock,
               img = excluded.img,
               star = excluded.star,
               access_status = excluded.access_status""",
        (book_name, price, stock, href, img, star, access_status),
    )

#去重
def link_exists(
        conn: sqlite3.Connection,
        href: str,) -> bool:
    c = conn.cursor()
    c.execute(
        "SELECT 1 FROM XIA_XUN WHERE href=? AND access_status IS NOT ? LIMIT 1",
        (href, "malformed"),
    )
    exists = c.fetchone() is not None
    return exists

def get_unpushed(conn: sqlite3.Connection) -> list:
    c = conn.cursor()
    #倒序
    c.execute("SELECT id , book_name , price ,stock, img , star FROM XIA_XUN WHERE access_status IN ('normal') AND pushed=0  ORDER BY pushed DESC")
    return c.fetchall()

def mark_pushed(conn: sqlite3.Connection,id_) -> None:
    c = conn.cursor()
    c.execute("UPDATE XIA_XUN SET pushed=1 WHERE id = ? ", (id_,))

def commit_db(conn: sqlite3.Connection) -> None:
    conn.commit()