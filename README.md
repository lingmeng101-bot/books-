# books-

books.toscrape.com 爬虫示例代码。

## 目录
- `src/`  示例代码
- `data/` 数据存储

## 功能
- 抓书籍列表页，解析书名、价格、库存、评分、封面图
- 存 SQLite，去重 href
- 分页抓取

## 使用方法
1. `pip install -r requirements.txt`
2. `cd src`
3. `python main.py`
4. `python db_clean.py` 导出 books_clean.csv
5. `python analyze.py` 出 books_stats.xlsx
