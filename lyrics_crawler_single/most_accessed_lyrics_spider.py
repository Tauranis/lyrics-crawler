import scrapy
import os

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

try:
    from lyrics_crawler_single.constants import (
        BASE_URL,
        TOP_N,
        MOST_ACCESSED,
        OUTPUT_FILE,
    )
except:
    from constants import BASE_URL, TOP_N, MOST_ACCESSED, OUTPUT_FILE


class TopNLyricsSpider(scrapy.Spider):
    name = "top_n_lyrics"
    start_urls = [
        os.path.join(BASE_URL, MOST_ACCESSED, "axe"),
        os.path.join(BASE_URL, MOST_ACCESSED, "fado"),
        os.path.join(BASE_URL, MOST_ACCESSED, "infantil"),
        os.path.join(BASE_URL, MOST_ACCESSED, "mpb"),
        os.path.join(BASE_URL, MOST_ACCESSED, "pagode"),
        os.path.join(BASE_URL, MOST_ACCESSED, "poprock"),
        os.path.join(BASE_URL, MOST_ACCESSED, "samba"),
        os.path.join(BASE_URL, MOST_ACCESSED, "bossa-nova"),
    ]

    def parse(self, response):

        for lyrics_list in response.css("ol.top-list_mus"):
            for _i, lyric in enumerate(lyrics_list.css('li a::attr("href")')):
                with open(OUTPUT_FILE, "a") as f:
                    uri = lyric.get()
                    if uri[0] == "/":
                        uri = uri[1:]
                    f.write(f"{os.path.join(BASE_URL,uri)}\n")

                if _i >= TOP_N:
                    break

