#Object Oriented Programming
class Student(object) :
    def __init__(self,name,score):
        self.__name=name #privated para,can not be accessed from outta space
        self.__score=score
    def printScore(self):
         print('%s \'s score is %d' %(self.__name,self.__score))
    def getScore(self):
        return self.__score
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def setScore(self,score):
        self.__score=score
Bob=Student('Bob',90)
Bob.printScore()
Bob.setName('Liao')
Bob.setScore(100)
Bob.printScore()
