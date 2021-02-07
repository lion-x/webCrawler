# 此例子来源于七月在线（julyedu.com）Python爬虫项目班课程
import requests
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def get_province_entry(url):
    # TODO
    kv = {'user-agent': 'Mozilla/5.0'}
    content = requests.get(url, headers=kv).content.decode('gb2312')

    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()

    # print(content)
    provinces = []
    handle = DefaultSaxHandler(provinces)
    parser = ParserCreate()
    parser.StartElementHandler = handle.start_element
    parser.EndElementHandler = handle.end_element
    parser.CharacterDataHandler = handle.char_data
    parser.Parse(content)
    return provinces


provinces = get_province_entry('https://www.ip138.com/post')
print(provinces)
