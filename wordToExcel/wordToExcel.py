# author:lk
# date: 20200224
# word 转 excel

import xlwt


class WordToExcel(object):

    def __init__(self):
        self.data = []
        self.path = '/Users/superlk/Desktop/e.txt'
        self.file = '/Users/superlk/Desktop/English900.xlsx'
        self.error = ''
        self.write_data = []

    def read_word(self):
        """
        读取word
        :return:None
        """

        if self.path:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self.data = f.readlines()
            except Exception as  e:
                self.error = str(e)

    def format_data(self):
        """
        处理数据格式化
        :return: None
        """
        if self.get_error():
            print(self.error)
            return
        if len(self.data) > 0:
            for line in self.data:
                # print(line.strip())
                # print(line.strip().split('.'))
                if len(line.strip().split('+')) == 4:
                    # print(len(line.strip().split('+')))
                    # print(line.strip().split('+'))
                    res = (line.strip().split('+')[2], line.strip().split('+')[1])
                    self.write_data.append(res)
                else:
                    self.error = str(line.strip().split('+'))
                    print(line.strip().split('+'))

    def write_excel(self):
        """
        写excel
        :return: None
        """
        if self.get_error():
            print(self.error)
            return
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("sheet1")
        for i in range(len(self.write_data)):
            print(i, self.write_data[i][0], self.write_data[i][1])
            sheet.write(i, 0, self.write_data[i][0])
            sheet.write(i, 1, self.write_data[i][1])
        workbook.save(self.file)

    def get_error(self):
        """
        获取error
        :return: True/False
        """
        if self.error:
            return True
        else:
            return False

    def start(self):
        """
        :return: None
        """
        self.read_word()
        self.format_data()
        self.write_excel()


if __name__ == '__main__':
    read_word = WordToExcel()
    read_word.start()
