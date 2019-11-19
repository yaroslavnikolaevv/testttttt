# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re
import winsound
import pyautogui
ur = ""
class Hui:
    def __init__(self,fromInput,fromOutput,date):
        self.fromInput=fromInput
        self.fromOutput=fromOutput
        self.date=date
        
    def trt(self):
        global ur
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        base_url = "http://rzd.ru/"
        verificationErrors = []
                

        driver.get(base_url)

        datin=driver.find_element_by_id("date0")
        datin.click()
        for i in range(13):
            pyautogui.press('backspace')
        datin.send_keys(self.date)
        inp=driver.find_element_by_id("name0")

        inp.send_keys(str(self.fromInput))
        inp.click()
        time.sleep(0.6)
        pyautogui.press('down')
        time.sleep(0.8)
        pyautogui.press('enter')
        outp=driver.find_element_by_id('name1')

        outp.send_keys(str(self.fromOutput))
        outp.click()
        time.sleep(0.6)
        pyautogui.press('down')
        time.sleep(0.6)
        pyautogui.press('enter')
        button=driver.find_element_by_xpath('//*[@id="Submit"]')
        time.sleep(0.4)
        button.click()
        ur=driver.current_url
        return(ur)
        

    # datin.clear()
    # datin.send_keys(date)
    # button=driver.find_element_by_xpath('//*[@id="new_ticket_form"]/div/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div')
    # button.click()0

        #     driver.find_element_by_id("j_username").clear()
        #     driver.find_element_by_id("j_username").send_keys("username")
        #     driver.find_element_by_id("j_password").clear()
        #     driver.find_element_by_id("j_password").send_keys("password")
        #     driver.find_element_by_id("other").click()

        #     self.logger.info('Меню покупки билетов...')

        #     driver.find_element_by_link_text("Покупка билета").click()

        #     self.logger.info('Ввод данных...')

        #     driver.find_element_by_id("fromInput").clear()
        #     driver.find_element_by_id("fromInput").send_keys(u'КАЗАНЬ ПАСС')
        #     driver.find_element_by_id("whereInput").clear()
        #     driver.find_element_by_id("whereInput").send_keys(u'МОСКВА КАЗАНСКАЯ')
        #     driver.find_element_by_id("forwardDate").clear()
        #     driver.find_element_by_id("forwardDate").send_keys(u'02.09.2012')
        #     driver.find_element_by_id("ticket_button_submit").click()

        #     time.sleep(40)

        #     self.logger.info('Поиск нужных билетов...')
        #     rawhtml = driver.find_element_by_id('ajaxTrainTable').get_attribute("innerHTML")

        #     if u'Плацкартный' in rawhtml:
        #         self.logger.info('!!!ЕСТЬ ПЛАЦКАРТ!!!')
        #         strlist = [x.strip() for x in rawhtml.split('n') if x.strip()!=u'']
        #         #print strlist
        #         train = ''
        #         for i,x in enumerate(strlist):
        #             if x == u'<div class="wotnumarrow">':
        #                 train = strlist[i+1].replace('<span><b>','')
        #             if x == u'Плацкартный':
        #                 #включаем сигнал тревоги
        #                 winsound.PlaySound('alarma.ogg', winsound.SND_NOWAIT)
        #                 self.logger.info(u'Поезд-%s Число-%s %s' % ( train, strlist[i+3].replace('<b>','').replace('</b>',''),
        #                 strlist[i+5].replace('<td><span>','').replace('</span></td>','')))

        #     elif u'Сидячий' in rawhtml:
        #         self.logger.info('Только сидячие...')
        #     elif u'Купе' in rawhtml:
        #         self.logger.info('Только купе...')

        #     self.logger.info('Выход...')

        #     driver.find_element_by_link_text("Выход").click()

        # def tearDown(self):
        #     self.logger.info('Закрываем браузер...')
        #     self.driver.close()
        #     self.driver.quit()
