from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import threading
from progressBarUi import *
from SecondFrame import *


class Searching:

    def googleSearch(self, master, frame1, value, searchbutton):
        self.master = master
        self.frame1 = frame1

        z = ContinousProgressBar()
        t2 = threading.Thread(target=lambda: z.progressBar(self.master))
        t2.setDaemon(True)
        t2.start()

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'C:\Users\karti\Desktop\browser_driver/chromedriver.exe',
                                  options=options)
        driver.get("http://www.google.com")
        search = driver.find_element_by_name('q')
        search.send_keys('define ' + value)
        search.send_keys(Keys.RETURN)
        time.sleep(2)

        try:
            content = driver.find_element_by_id('dictionary-modules')
        except :
            resultVal = 'No result Found'
            print(resultVal)
        else:
            resultVal = content.text
            print(resultVal)
            #self.frame1.update()

        z.forgetProgressBar()
        global c
        try:
            c.close_button(c.frame2, c.button)
        except:
            pass

        a = NewFrame2()
        c = a
        a.stage2(self.master)
        a.outputField(resultVal)
        driver.close()
        searchbutton.configure(state='!disabled')

if __name__ == '__main__':
    search1 = Searching()
    search1.googleSearch()