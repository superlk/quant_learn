#  处理anki
#     pip install translate  英文翻译中文库


from translate import Translator


# 以下是将简单句子从英语翻译中文
# translator = Translator(to_lang="chinese")
# translation = translator.translate("Good night!")
# print(translation)


def readWord():
    f3 = open('/Users/superlk/Desktop/麦克米伦1星.txt', 'w')
    f1 = open('/Users/superlk/Desktop/english 3.txt', 'r')
    f = open('/Users/superlk/Desktop/麦克米伦7000.txt', 'r')

    data = f.readlines()
    data1 = f1.readlines()
    print(len(data))
    num = 0
    for n in data:
        for m in data1:
            # print(m.split('\n')[0] in  n.split('[')[0])
            if (m.split('\n')[0] == n.split('[')[0].strip()):
                num += 1
                print(num, m.split('\n')[0], '-----', n.split(' ')[0])
                f3.writelines(n)

    f.close()
    f1.close()


if __name__ == '__main__':
    readWord()
