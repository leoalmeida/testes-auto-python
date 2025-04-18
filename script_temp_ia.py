from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configurando o driver do Chrome
chrome_path = "Caminho_para_o_executável_do_chrome"
webdriver_service = Service('driver/chromedriver.exe')
webdriver_service.start()
driver = webdriver.Chrome(service=webdriver_service)

# URL da plataforma AcordeLab
url = "https://leoalmeida.github.io/"

# Abrindo o site da plataforma AcordeLab
driver.get(url)

time.sleep(3)
# Localizando e clicando no botão de login
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_button.click()

# Preenchendo o campo de e-mail e senha
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("email@acordlab.com.br")
password_input = driver.find_element(By.ID, "senha")
password_input.send_keys("123senha")

# Clicando no botão de login
login_submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_submit_button.click()

# Aguardando a validação das credenciais
time.sleep(3)

# Verificando se Ana foi redirecionada para sua conta na plataforma AcordeLab
# Aqui você pode adicionar mais verificações conforme necessário

# Fechando o navegador após 3 segundos
time.sleep(3)
driver.quit()