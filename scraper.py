# -*- coding: utf-8 -*-
__author__ = 'hmharshit'
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.goodreads.com/genres/most_read/business'


class GoodReads:
    def scrap(self):
        response = {
            "new_releases": [],
            "most_read_this_week": [],
            "most_popular": [],
        }
        soup = self.convert(BASE_URL)
        books = soup.find_all('img', {'class': 'bookImage'})
        for book in books:
            goodreads_id = book.get("src")[35:46]
            response.get("most_read_this_week").append(
                {"goodreads_id": goodreads_id,
                 "title": book.get("alt"),
                 "isbn_id": None}
            )
        return response

    def convert(self, url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/39.0.2171.95 	Safari/537.36')
        resp = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(resp, 'lxml')
        return soup


if __name__ == "__main__":
    print(GoodReads().scrap())
