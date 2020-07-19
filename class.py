class hello:
    def __init__(self,name):
        print("hello")#this statment will be printed every time the object is called
        self.name = name
    def timepass(self):
        print("you look great")
if __name__  ==  '__main__':
    l1 = hello('nanditha')
    l1.timepass()