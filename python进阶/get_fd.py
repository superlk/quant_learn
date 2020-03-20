import urllib.request
import urllib
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time


class Book(object):
    """
    樊登读书爬虫
    """

    def __init__(self, url):
        self.url = url  # 'http://blog.sina.com.cn/s/articlelist_6062317667_1_1.html'
        self.book_list = []
        self.duoDu_dict = {}
        self.download_dict = {}
        self.duoDu_not_found = []

    invalidLink1 = '#'
    # 非法URL 2
    invalidLink2 = 'javascript:void(0)'

    def get_soup(self, url):
        """
        获取html
        :param url:
        :return:
        """
        try:
            response = urllib.request.Request(url)
            webpage = urllib.request.urlopen(response)
        except urllib.error.URLError as e:
            print(e)
            return
        html = webpage.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_book_list(self):
        """
        获取书的列表
        :return:
        """
        soup = self.get_soup(self.url)
        result = set()
        count = 0
        for k in soup.find_all('a'):
            link = k.get('href')

            if link == self.invalidLink1:
                pass
            elif link == self.invalidLink2:
                pass
            elif link.find("javascript:") != -1:
                pass
            else:
                # print(link.find("http://blog.sina.com.cn/s/blog"))d
                if link.find("http://blog.sina.com.cn/s/blog") == 0:
                    # print(link)
                    count += 1
                    result.add(link)
        self.book_list = list(result)
        # print(len(self.book_list))

    def get_duoDu(self, url):
        """
        获取多读链接
        :param url:
        :return:
        """
        soup = self.get_soup(url)
        if not soup:
            return
        for k in soup.find_all('a'):
            link = k.get('href')

            if link == self.invalidLink1:
                pass
            elif link == self.invalidLink2:
                pass
            elif link.find("javascript:") != -1:
                pass
            else:
                # print(link.find("http://blog.sina.com.cn/s/blog"))d
                if link.find("http://www.duodu.cc") == 0:
                    # print(link)
                    self.duoDu_dict[k.find('b').get_text()] = link

    def get_down(self, name, url):
        """
          获取下载链接
        :param url:
        :return:
        """
        # print("url:===>",url)
        soup = self.get_soup(url)
        if not soup:
            self.duoDu_not_found.append(name)
            print("not found:", name)
            return

        for k in soup.find_all('a'):
            link = k.get('href')
            if link == self.invalidLink1:
                pass
            elif link == self.invalidLink2:
                pass
            elif link.find("javascript:") != -1:
                pass
            else:

                if link.find("https://") == 0:
                    # print("===",k.get_text())
                    self.download_dict[k.get_text()] = link

    def start(self):
        self.get_book_list()
        for i in self.book_list:
            self.get_duoDu(i)
        for n, u in self.duoDu_dict.items():
            self.get_down(n, u)
        # print(self.duoDu_not_found)
        for f, l in self.download_dict.items():
            self.download_button_onclick(l)
            break

    def download_button_onclick(self, url):
        """
        下载
        :param url:
        :return:
        """
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        browser.find_element_by_xpath("//button[@onclick='file_down( 0, 0)']").click()
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    url = "http://blog.sina.com.cn/s/articlelist_6062317667_1_1.html"
    book = Book(url)
    # book.start()
    book.download_button_onclick('https://545c.com/file/18852109-393346266')
    # book.text()
