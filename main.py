from scrapy import cmdline
cmdline.execute('scrapy crawl tutorial -o items.csv -t csv'.split())
