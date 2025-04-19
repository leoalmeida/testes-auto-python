from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Lista com os casos de teste
test_cases = [
    {
        "id": 1,
        "description": "Login com credenciais válidas",
        "input": {
            "email": "email@acordelab.com.br",
            "password": "123senha"
        },
        "expected_output": {
            "result": "Aprovado",
            "redirect_url": "home.html",
            "message": "Login realizado com sucesso."
        }
    },
    {
        "id": 2,
        "description": "Login com senha incorreta",
        "input": {
            "email": "ana@acordelab.com",
            "password": "SenhaErrada456"
        },
        "expected_output": {
            "result": "Reprovado",
            "message": "Senha incorreta. Tente novamente."
        }
    },
    {
        "id": 3,
        "description": "Login com e-mail incorreto",
        "input": {
            "email": "anaincorreta@acordelab.com",
            "password": "SenhaCorreta!123"
        },
        "expected_output": {
            "result": "Reprovado",
            "message": "E-mail não encontrado. Verifique seus dados e tente novamente."
        }
    },
    {
        "id": 4,
        "description": "Login com campos de e-mail e senha vazios",
        "input": {
            "email": "",
            "password": ""
        },
        "expected_output": {
            "result": "Reprovado",
            "message": "Os campos de e-mail e senha não podem estar vazios."
        }
    }
]

# Configuração do WebDriver para usar o Chromium
service = Service('driver/chromedriver.exe') # Substitua pelo caminho para o chromedriver
driver = webdriver.Chrome(service=service)

# URL base de login
base_url = "https://leoalmeida.github.io/testes-auto-python/"

time.sleep(3)
# Função para executar cada caso de teste
for test in test_cases:
    # Acesso a página de login
    driver.get(base_url)
    
    # Localiza e preenche o campo de e-mail
    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(test["input"]["email"])
    
    # Localiza e preenche o campo de senha
    password_field = driver.find_element(By.ID, "senha")
    password_field.clear()
    password_field.send_keys(test["input"]["password"])
    
    # Clica no botão de login
    login_button = driver.find_element(By.CLASS_NAME, "botao-login")
    login_button.click()
    
    time.sleep(2)  # Aguarda 2 segundos pelo processamento do login

    # Verifica o resultado esperado
    if test["expected_output"]["result"] == "Aprovado":
        # Verifica redirecionamento em caso de login bem-sucedido
        current_url = driver.current_url
        if base_url + test["expected_output"]["redirect_url"] in current_url:
            print(f"Teste {test['id']}: {test['description']} - Aprovado")
        else:
            print(f"Teste {test['id']}: {test['description']} - Reprovado")
    else:
        # Verifica mensagem de erro em caso de falha
        error_message = driver.find_element(By.CLASS_NAME, "mensagem-erro").text
        if test["expected_output"]["message"] in error_message:
            print(f"Teste {test['id']}: {test['description']} - Aprovado")
        else:
            print(f"Teste {test['id']}: {test['description']} - Reprovado")

# Espera 3 segundos antes de finalizar o script
time.sleep(3)

# Fecha o navegador
driver.quit()
