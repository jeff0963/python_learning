#透過unittest模組來自動測試
"""
import unittest
from name_function import get_formatted_name#先把模組叫進來

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name("jeff","chen")
        self.assertEqual(formatted_name,"Jeff Chen")#assertEqual用來比對得到結果是否與預期相同

    def test_first_last_name2(self):
        formatted_name=get_formatted_name("jeff","chen","yi")#函式輸入值
        self.assertEqual(formatted_name,"Jeff Yi Chen")#用來比對得到結果是否與預期相同  formatted_name是輸出的結果，"Jeff Yi Chen"是預期的結果

if __name__ == '__main__':
    unittest.main() 

"""
#實作練習
#1編寫一個能接收兩個參數的函式，這兩個引數是city、country，這兩個參數會回傳一個字串，然後用unittest測試
#2加上一個人口數，這個參數可有可無，再在unittest測試是否有或沒有都能順利執行
"""
def city_descript(city,country,population=""):
    if population:
        descirption=f"{population} {city} {country}"
    else:
        descirption=f"{city} {country}"
    return descirption.title()

import unittest

class Test(unittest.TestCase):
    def test1(self):#無population測試
        descript=city_descript("taipei","taiwan")
        self.assertEqual(descript,"Taipei Taiwan")
    
    def test2(self):#有population測試
        descript=city_descript("taipei","taiwan","1000000")
        self.assertEqual(descript,"1000000 Taipei Taiwan")

if __name__=="__main__":
    unittest.main()
"""
#再定義一個AnonymousSurvey類別
class AnonymousSurvey:
    def __init__(self,question):
        self.question=question
        self.respond=[]

    def show_question(self):
        print(self.question)
    
    def store_question(self,new_respond):
        self.respond.append(new_respond)

    def show_result(self):
        print("調查結果")
        for responses in self.respond:
            print(responses)
"""
#對AnonymousSurvey類別進行自動化測試
import unittest
class TestAnonymousSurvey(unittest.TestCase):
    def testAnonymousSurvey_SingleAnswer(self):
        question="你愛看甚麼電影"
        my_survey=AnonymousSurvey(question)
        my_survey.store_question("鐵達尼號")
        self.assertIn("鐵達尼號",my_survey.respond)#看看輸入的答案是否會在串列中
    
    def testAnonymousSurvey_MultiAnswer(self):
        question="你愛看甚麼電影"
        my_survey=AnonymousSurvey(question)
        responses=["鐵達尼號","斷背山","海角七號"]
        for response in responses:
            my_survey.store_question(response)
        for response in responses:
            self.assertIn(response,my_survey.respond)#看看輸入的答案是否會在串列中

if __name__=="__main__":
    unittest.main()
"""
#我們為了測試我們為了測試TestAnonymousSurvey要一直在方法裡建立my_survey=AnonymousSurvey(question)很麻煩
#用setUp()方法可以解決
"""
import unittest
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):#用setUp先建立好會用到的元件
        self.question="你愛看甚麼電影"
        self.my_survey=AnonymousSurvey(self.question)
        self.responses=["鐵達尼號","斷背山","海角七號"]

    def testAnonymousSurvey_SingleAnswer(self):
        self.my_survey.store_question(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.respond)
    
    def testAnonymousSurvey_MultiAnswer(self):
        for response in self.responses:
            self.my_survey.store_question(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.respond)#看看輸入的答案是否會在串列中

if __name__=="__main__":
    unittest.main()
"""
#實作練習
#1.寫一個Employee類別，可以接收名、姓、年薪等資訊，設計一個give_raise()方法，其預設會對年薪加5000，但也能接收其他加薪數值
#2.為Employee類別寫一個測試程式，有兩個方法:test_give_default_raise()、test_give_custom_raise()，用setUp()方法建立實例
class Employee:
    def __init__(self,first,last,income=5000):
        self.first=first
        self.last=last
        self.income=income

    def give_raise(self,raise_income=0):
        self.income+=raise_income
        message=f"{self.first} {self.last} {self.income}"
        return message

import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee=Employee("陳","奕君")
    def test_give_default_raise(self):
        self.assertEqual("陳 奕君 5000",self.employee.give_raise())
    
    def test_give_custom_raise(self):
        self.assertEqual("陳 奕君 6000",self.employee.give_raise(1000))
if __name__=="__main__":
    unittest.main()