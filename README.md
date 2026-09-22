# books-

books.toscrape.com 爬虫示例代码。

## 功能
- 抓书籍列表页，解析书名、价格、库存、评分、封面图
- 存 SQLite，按 href 去重，重复跑不会重复入库
- 分页抓取，页数在 config.py 里改

## 使用方法
1. `pip install -r requirements.txt`
2. `python main.py`
3. `python db_clean.py` 导出 books_clean.csv
4. `python analyze.py` 出 books_stats.xlsx
