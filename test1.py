#!/usr/bin/env python
# coding:utf-8

import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wx


def test_gui():
    app = wx.App()
    frame = Frame1(None, 'example')
    app.MainLoop()


class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(100, 200), size=(800, 400))
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(self.panel, value="Hello, World!", size=(200, 100))
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(self.panel, label='click me')
        sizer.Add(button)
        self.panel.SetSizerAndFit(sizer)
        self.panel.Layout()
        self.panel.Bind(wx.EVT_BUTTON, self.OnClick, button)
        self.Show(True)

    def OnClick(self, event):
        # posm = event.GetPosition()
        # wx.StaticText(parent=self.panel, label='mouse upupup', pos=posm)
        self.text1.AppendText("\r\n add here")


class Animal(object):
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print("This animal's name:", self.name)

    def sound(self):
        print("The sound of this animal goes?")


class Dog(Animal):
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def getInfo(self):
        print("This dog's name:", self.name)
        print("This dog’s size:", self.__size)


class Cat(Animal):
    def sound(self):
        print("The sound of cat goes meow ~")


def test_7():
    dog = Dog('coco','small')
    dog.sound ()
    cat = Cat('kawaii')
    print(isinstance(dog, Animal))
    print(isinstance(cat, Animal))
    print(isinstance(dog, Dog))
    print(isinstance(dog, Cat))



def main():
    dates = pd.date_range('20171001', periods=10)
    listA = ['value']
    result = pd.DataFrame(np.arange(1,11),index=dates,columns = listA)
    print(result)

    x = np.linspace(0, 1)
    y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
    plt.title('this is title')
    plt.xlabel('xxxxx')
    plt.ylabel('yyyyy')
    plt.plot(x, y, '-.*r')
    #plt.plot(x, y, 'rD')
    # plt.bar(x, y)
    plt.savefig('1.png')


def edit_excel():
    df = pd.read_excel('1.xlsx')
    print(df)
    df['sum'] = df.Python + df.Math
    df.to_excel('students.xlsx', sheet_name='scores')


from nltk.corpus import PlaintextCorpusReader
def edit_nltk():
    corpus_root = r'/data'
    books = PlaintextCorpusReader(corpus_root, '.*')
    print(books.fileids())

class Dog1(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Dog1.count += 1
    def greet(self):
        print('{}: {}'.format(self.count, self.name))

if __name__ == "__main__":
    test_7()

    dog = Dog1('huahua')
    dog.greet()
    dog = Dog1('2222')
    dog.greet()
    test_gui()
    # main()
    #edit_excel()
    #edit_nltk()
