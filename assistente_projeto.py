from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPΕΝΑΙ_API_KEY"))

def apagar_assistente(assistant_id):
    cliente.beta.assistants.delete(assistant_id)
    
def apagar_thread(thread_id):
    cliente.beta.threads.delete(thread_id)

def apagar_arquivos(lista_ids_arquivos):
    for id_arquivo in lista_ids_arquivos:
        cliente.files.delete(id_arquivo)

def apagar_vector_store(vs_id):
    cliente.vector_stores.delete(vs_id)

def criar_thread():
    return cliente.beta.threads.create()

def criar_assistente(vs_id, modelo=MODELO_GPT_4_1):
    return cliente.beta.assistants.create(
        name="Atendente Eng. Software",
        instructions = f"""
            Assuma que você é um assistente virtual especializado em orientar desenvolvedores e QA testers na criação de testes automatizados para aplicações web usando Python e Selenium. 
            
            Você deve oferecer suporte abrangente, desde o setup inicial do ambiente de desenvolvimento até a implementação 
            de testes complexos, adotando e consultando principalmente os documentos de sua
            base (para identificar padrões e formas de estruturar os scripts solicitados).

            Consulte sempre os arquivos html, css e js para elaborar um teste.
            
            Adicionalmente, você deve ser capaz de explicar conceitos chave de 
            testes automatizados e Selenium, fornecer templates de código personalizáveis, e oferecer feedback sobre scripts de teste escritos pelo usuário. 

            O objetivo é facilitar o aprendizado e a aplicação de testes automatizados, 
            melhorando a qualidade e a confiabilidade das aplicações web desenvolvidas.

            Caso solicitado a gerar um script, apenas gere ele sem outros comentários adicionais.

            Você também é um especialista em casos de uso, seguindo os templates indicados.
            E também é um especialista em gerar cenários de teste.
                """,
        model = modelo,
        tools=  [{"type": "file_search"}],
        tool_resources= {"file_search": {"vector_store_ids": [vs_id]}}
    )

def criar_vector_store(lista_ids_arquivos):
    vector_store = cliente.vector_stores.create(name="vs_assistant", file_ids=lista_ids_arquivos)
    
    print(vector_store.file_counts)
    
    return vector_store.id

def criar_lista_ids_app_web(diretorio = "docs"):
    
    lista_ids_arquivos = []
    dicionario_arquivos = {}

    for caminho_diretorio, nomes_diretorios, nomes_arquivos in os.walk(diretorio):
        arquivos_web = [f for f in nomes_arquivos if f.endswith(('.html', '.css', '.js'))]
        for arquivo in arquivos_web:
            caminho_completo = os.path.join(caminho_diretorio, arquivo)
            with open(caminho_completo, 'rb') as arquivo_aberto:
                web_file = cliente.files.create(
                    file=arquivo_aberto,
                    purpose="assistants"
                )
                lista_ids_arquivos.append(web_file.id)
                dicionario_arquivos[arquivo] = web_file.id

    caminho_arquivo = "documentos/exemplos_caso_uso.txt"
    nome_arquivo = os.path.basename(caminho_arquivo)
    aquivo_exemplo_caso = cliente.files.create(
                    file=open(caminho_arquivo, 'rb'),
                    purpose="assistants"
                )
    lista_ids_arquivos.append(aquivo_exemplo_caso.id)
    dicionario_arquivos[nome_arquivo] = aquivo_exemplo_caso.id

    return lista_ids_arquivos, dicionario_arquivos
    