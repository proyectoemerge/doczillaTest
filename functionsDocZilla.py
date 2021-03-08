from numpy import append
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
def beginProcess(step,name,thr):
    t = datetime.datetime.now()
    print("Begin process:"+step+", With name "+name+", thread:"+str(thr))
    return t
def endProcess(step,name,ti,thr):
    t = datetime.datetime.now()
    print("End process:"+step+", With name "+name+", thread:"+str(thr))   
    print("Time to process:","Step:"+step,"name:"+name,(t-ti),", thread:"+str(thr))
def executeSomeProcess(thr,driver,val,xpath,step,name):
    ti=beginProcess(step,name,thr)
    element = WebDriverWait(driver, val).until(
    EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click();
    endProcess(step,name,ti,thr)  
def executeSomeProcessWithKeys(thr,driver,val,xpath1,step,name,keys,xpath2):
    ti=beginProcess(step,name,thr)
    imput_user=driver.find_element_by_xpath(xpath1)
    imput_user.send_keys(keys)
    element_enter = WebDriverWait(driver, val).until(
    EC.element_to_be_clickable((By.XPATH, xpath2)))
    element_enter.click();
    endProcess(step,name,ti,thr)     