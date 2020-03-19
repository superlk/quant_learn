import urllib.request
from bs4 import BeautifulSoup


class Book(object):
    """
    樊登读书爬虫
    """
    def __init__(self, url):
        self.url = url  # 'http://blog.sina.com.cn/s/articlelist_6062317667_1_1.html'
        self.book_list = []
        self.duoDu_list = []
        self.download = []

    invalidLink1 = '#'
    # 非法URL 2
    invalidLink2 = 'javascript:void(0)'

    def get_soup(self, url):
        """
        获取html
        :param url:
        :return:
        """
        response = urllib.request.Request(url)
        webpage = urllib.request.urlopen(response)
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
        print(len(self.book_list))

    def get_duoDu(self, url):
        """
        获取多读链接
        :param url:
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
                if link.find("http://www.duodu.cc") == 0:
                    # print(link)
                    count += 1
                    result.add(link)
        self.duoDu_list.append(list(result))
        print(len(self.duoDu_list))

    def get_down(self, url):
        """
          获取下载链接
        :param url:
        :return:
        """
        pass

    def start(self):
        self.get_book_list()
        for i in self.book_list:
            self.get_duoDu(i)


if __name__ == '__main__':
    url = "http://blog.sina.com.cn/s/articlelist_6062317667_1_1.html"
    book = Book(url)
    book.start()
