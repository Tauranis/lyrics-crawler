import scrapy

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

try:
    from lyrics_crawler_single.constants import (
        OUTPUT_FILE,
    )
except:
    from constants import OUTPUT_FILE


class LyricsSpider(scrapy.Spider):
    name = "lyrics"
    start_urls = open(OUTPUT_FILE).readlines()

    def parse(self, response):
        for lyric in response.css("article"):

            lyric_title = lyric.css("h1::text").get()
            lyric_author = lyric.css("span::text").get()
            # logger.info(f"lyric_title {lyric_title}")
            # logger.info(f"lyric_author {lyric_author}")

            lyric_text = ""

            for paragraph in lyric.css("p::text"):
                lyric_text += " " + paragraph.get().replace("<br>", " ")

            yield {"author": lyric_author, "title": lyric_title, "text": lyric_text}

