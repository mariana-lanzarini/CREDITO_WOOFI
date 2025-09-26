import os
from Utils.email_operations import email
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Utils.config import Config
class woofiNavegacao:
    @staticmethod
    def abrirWoofi():
        """ abri o site no navegador"""
        MAX_TENTATIVAS_WOOFI = 5
        CHROME_DRIVER_PATH = Config.get_chrome_driver_path()
        url_woofi = Config.url_woofi

        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--guest")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        prefs = {
            "profile.default_content_setting_values.cookies": 2,
            "profile.block_third_party_cookies": True,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True, }

        options.add_experimental_option("prefs", prefs)
        
        options.add_experimental_option("excludeSwitches", ["enable-logging"])  
        service = Service(CHROME_DRIVER_PATH, log_output=os.devnull)

        driver = None 
        print("tentando 5 vezes")
        for tentativa in range(1, MAX_TENTATIVAS_WOOFI + 1):
           
            try:

                service = Service(CHROME_DRIVER_PATH)
                driver = webdriver.Chrome(service=service, options=options)

                driver.get(url_woofi)
                driver.maximize_window()
                print("janela do driver aberta")

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/h1")))
                if driver.current_url.startswith(url_woofi):
                    print("acessa a url")
                    return driver
                else:
                    driver.quit()

            except WebDriverException as e:
                print(e)
                if driver:
                    driver.quit()

        return None
    @staticmethod
    def logarWoofi(driver):
        """ faz o login no site"""
        try:
            wait = WebDriverWait(driver, 20)
            user_email = Config.login_woofi
            user_senha = Config.senha_woofi
            campo_login = wait.until(
                EC.presence_of_element_located((By.ID, "email")))
            campo_login.send_keys(user_email)
            print("procura onde inserir o email")
            campo_senha = wait.until(EC.presence_of_element_located((By.ID, "password")))
            campo_senha.send_keys(user_senha)
            print("procura onde inserir a senha")
            clicar_enter = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/form/div/div[4]/button")))
            clicar_enter.click()
            print("clicou em enter")
            return True
        except WebDriverException as e:
            print(e)
            if driver:
                    driver.quit()
            return False
        
    @staticmethod
    def verficarValor(driver):
        """verifica se o valor for menor or igual de 150 e manda um email de aviso"""
        wait = WebDriverWait(driver, 20)
        campo_valor = wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[@id='current-value' and contains(@class,'text-3xl')]")))
        print("encontra o valor da conta")
        valor = campo_valor.text
        valor_float = float(valor.split('$')[1])
        print("pega o valor depois do $ e fica float")
        print(valor_float)
        valor_float = 120
        if valor_float <= 150:
            print("menor ou igual")
            email.enviarEmail(valor_float)
        else:
            print("maior ou igual")