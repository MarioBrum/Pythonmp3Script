from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

##abre navegador
navegador = webdriver.Chrome()
musica = ''
#le o txt
with open('musicasBot.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        musica = line.strip()

        ##abre site
        navegador.get("https://www.google.com/")

        time.sleep(2)


        musicaNavegador = navegador.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        ##musicaNavegador.click()
        musicaNavegador.clear()
        musicaNavegador.click()
        musicaNavegador.send_keys(musica)
        musicaNavegador.send_keys(Keys.ENTER)

        ##entra no yt da musica
        navegador.find_element(
            By.XPATH,'/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/video-voyager/div/div/div/div[1]/a/div/cite'
            ).click();
        time.sleep(1)
        linkMusica = navegador.current_url

        navegador.get("https://flvto.com.mx/")

        musicaNavegador = navegador.find_element(
            By.XPATH, '/html/body/div/div[1]/section[1]/div/div[2]/div/div/form/input'
            )
        musicaNavegador.clear()
        musicaNavegador.click()
        musicaNavegador.send_keys(linkMusica)
        musicaNavegador.send_keys(Keys.ENTER)
        time.sleep(5)
        navegador.find_element(
            By.XPATH, '/html/body/div/div[1]/section[2]/div/div[2]/ul/li[1]/a'
        ).click()                                      
        time.sleep(10)

        navegador.find_element(
            By.XPATH, '/html/body/div/div[4]/div/div[2]/div[1]/div[1]/a'
        ).click()


       
        navegador.find_element(
            By.XPATH, '/html/body/div/div[1]/section[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/button'
        ).click()
        time.sleep(5)
       

'''

##clica enter na aba pesquisar
navegador.find_element(
    By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    ).send_keys(Keys.ENTER)

time.sleep(2)
##entra no yt da musica
navegador.find_element(
    By.XPATH,'/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/div/div/div/div/div/div/div/div[2]/h3/a/h3'
    ).click();
##



##abre site pra baixar musica pela url
navegador.get("https://flvto.com.mx/")

##acha aba de input
navegador.find_element(
    By.XPATH , "/html/body/div/div[1]/section[1]/div/div[2]/div/div/form/input"   
    ).click(2)
'''
'''
##muta a musica do yt
navegador.find_element(
    By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[28]/div[2]/div[1]/span/button'
    ).click();
##MUTADO NO PROPRIO WINDOWS, ANTES DA EXECUCAO DO BOT
'''
    
'''
##clica na música
navegador.find_element(
    By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
    ).send_keys(Keys.ENTER)
    '''