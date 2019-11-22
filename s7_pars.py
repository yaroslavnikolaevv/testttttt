from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re
import winsound
import pyautogui
import datetime
ur = ""
class S7:
   def __init__(self,fromInput,fromOutput,dateIn):
        self.fromInput=fromInput
        self.fromOutput=fromOutput
        self.date1=dateIn[-4:]+"-"+dateIn[3:5]+"-"+dateIn[:2]
        self.year=int(dateIn[-4:])
        if int(dateIn[3:5])<10:
            self.month=int(dateIn[4:5])
        else:
            self.month=int(dateIn[3:5])
        if int(dateIn[:2])<10:
            self.day=int(dateIn[1:2])
        else:
            self.day=int(dateIn[:2])
   def poisk(self):
        global ur
        print(self.date1)
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        base_url = "http://s7.ru/"
        verificationErrors = []
                        

        driver.get(base_url)
        time.sleep(7)
        pyautogui.press('tab')
                # datin=driver.find_element_by_id("date0")
                # datin.click()
                # for i in range(13):
                #     pyautogui.press('backspace')
                # datin.send_keys(self.date)
        time.sleep(2)
        pyautogui.typewrite('!')
        inp=driver.find_element_by_id("flights_origin2")
        
        inp.clear()
        inp.send_keys(str(self.fromInput))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="aviaBot"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div/ul/li/div[2]').click()
        outp=driver.find_element_by_xpath('//*[@id="flights_destination2"]')
        outp.send_keys(str(self.fromOutput))
        time.sleep(2)
                
        pyautogui.press('tab')
        time.sleep(0.6)

        datefalse=driver.find_element_by_xpath('//*[@id="date-opener2"]')
        time.sleep(0.4)
        datefalse.click()
        datefalse.click()
        to_one=driver.find_element_by_xpath('//*[@id="aviaBot"]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/label')
        to_one.click()
        now=datetime.datetime.now()
        then=datetime.datetime(year=self.year,month=self.month,day=self.day)
        delta=then-now
        cl=(delta.days//30)
        next_month=driver.find_element_by_xpath('//*[@id="ui-datepicker-next-avia"]')
        next_month.click()
        
        for i in range(cl):
            next_m=driver.find_element_by_xpath('//*[@id="datepicker2"]/div/div/a[2]')
            next_m.click()
        if delta.days>=359:
            print('нема,вводи меньше')
            return("извините,но билетов на эту дату нет,т.к. компанией s7 еще не составлено расписание.Вы можете искать билеты на любой день, который будет не более чем через 359 дней")
        else:
            for k in range(self.day):
                pyautogui.press('tab')
        pyautogui.press('enter')
        confirm=driver.find_element_by_xpath('//*[@id="search-btn-expand-bot"]')
        confirm.click()
        # pyautogui.press('tab')
        # time.sleep(0.4)
        # pyautogui.press('tab')
        # time.sleep(0.4)
        # pyautogui.press('tab')
        # time.sleep(0.4)
        # pyautogui.press('tab')
        # time.sleep(0.4)
        # pyautogui.press('tab')
        # time.sleep(0.4)
        # pyautogui.press('enter') #первая дата
        # 
        # for i in range(cl):
        #     next_month=driver.find_element_by_xpath('//*[@id="calendar-root"]/div/section/ul[2]/li[2]/section/h4/button')
        #     next_month.click()
        #     time.sleep(0.2)
        # confirm=driver.find_element_by_xpath('//*[@id="search-btn-expand-bot"]')
        # confirm.click()
        # time.sleep(7)
        # ur=driver.current_url
        # driver.find_element_by_xpath('//*[@id="expandSearchForm"]/div[3]/div/div/div[1]/div[2]/div/label[2]').click()
        # driver.find_element_by_xpath('//*[@id="visible-date-field"]').click()
        # time.sleep(0.5)
        ur=driver.current_url
        
        return(ur)
        # 
            
# print(S7('владивосток', 'москва', '12.09.2020').poisk())