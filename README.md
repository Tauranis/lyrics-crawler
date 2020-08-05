
## Install dependencies

```
virtualenv -p /usr/bin/python3 ./venv

source ./venv/bin/activate

pip install -r requirements.txt

```


## Run Scrapy

```
scrapy runspider lyrics_crawler_single/most_accessed_lyrics_spider.py

scrapy runspider lyrics_crawler_single/lyric_spider.py -o lyrics.json

```