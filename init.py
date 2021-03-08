from functionsDocZilla import executeSomeProcess,executeSomeProcessWithKeys
from time import sleep
import datetime
from selenium import webdriver
import threading
from params import conf;

params=conf()
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
driver_path =params["driver"]
def consulta1(thr):
    tiempo_inicio = datetime.datetime.now()
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    driver.get(params["url"])
    sleep(3)
    executeSomeProcess(thr,driver,20,"//*[@id='app']/section/div[2]/button[1]","1","1");
    executeSomeProcess(thr,driver,20,"//*[@id='auth0-lock-container-1']/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/a/div[2]","2","2");
    executeSomeProcess(thr,driver,20,"//*[@id='i0116']","3","3");
    executeSomeProcessWithKeys(thr,driver,20,"//*[@id='i0116']","4","4",params["username"],"//*[@id='idSIButton9']");
    executeSomeProcess(thr,driver,20,"//*[@id='i0118']","5","5");
    executeSomeProcessWithKeys(thr,driver,20,"//*[@id='i0118']","6","6",params["password"],"//*[@id='idSIButton9']");
    executeSomeProcess(thr,driver,20,"//*[@id='search_documentTypeChidropdown-basic']","7","7");
    executeSomeProcess(thr,driver,20,"//*[@id='search_documentTypeChi']/div/button[1]","8","8");
    executeSomeProcess(thr,driver,20,"//*[@id='searchButton']","9","9");
    executeSomeProcess(thr,driver,20,"(//span[contains(@class, 'clickableIcon')])[1]","10","10");
    tiempo_fin = datetime.datetime.now()
    deltatiempo=tiempo_fin-tiempo_inicio
    print("Full time duration",deltatiempo,"Thread",thr)
threads = []
for i in range(3):
    t = threading.Thread(target=consulta1,args=[i])
    threads.append(t)
    t.start()
