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
url = "https://leoalmeida.github.io/testes-auto-python/"

# Abrindo o site da plataforma AcordeLab
driver.get(url)

time.sleep(3)

# Preenchendo o campo de e-mail e senha
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("email@acordelab.com.br")
password_input = driver.find_element(By.ID, "senha")
password_input.send_keys("123senha")

# Clicando no botão de login
login_submit_button = driver.find_element(By.CLASS_NAME, 'botao-login')
login_submit_button.click()

# Aguardando a validação das credenciais
time.sleep(3)

# Verificando se Ana foi redirecionada para sua conta na plataforma AcordeLab
# Aqui você pode adicionar mais verificações conforme necessário

# Fechando o navegador após 3 segundos
time.sleep(3)
driver.quit()