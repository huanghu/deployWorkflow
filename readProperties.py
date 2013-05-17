# _*_ coding:gbk _*_
'''
Created on 2013-1-8

@author: huanghu
'''

import codecs

class saveProperties():
    def init(self):
        pass
    
    def read(self):
        f = open("path.properties");
        items = dict();
        while True:
            char = f.readline();
            if not char:
                break;
            else:
                if len(str(char)) <= 1:
                    continue;
                prop = str(char).split('=');
                items[prop[0]] = prop[1]
        return items;
    
    def readUnicode(self):
        f = codecs.open("test.properties" ,'r' ,'gbk');
        while True:
            char = f.readline();
            if not char:
                break;
            else:
                #unicode转中文 去掉回车
                chars = char.decode('unicode_escape');
                print chars.strip();

if __name__ == '__main__':
    save = saveProperties();
    save.read();