from openai import OpenAI
from openai.types.beta.assistant import Assistant  
from openai.types.beta.thread import Thread  
from dotenv import load_dotenv
import os

load_dotenv()


class AssistenteBase():
    def __init__(self, nome:str, instrucoes:str, caminho_arquivo:str):
        load_dotenv()
        self.cliente = OpenAI(api_key=os.getenv("OPΕΝΑΙ_API_KEY"))
        self.id_arquivo = self.associar_arquivo(caminho_arquivo)
        self.assistente = self.criar_assistente(nome, instrucoes, file_id=self.id_arquivo)
        self.thread = self.criar_thread()
    
    def associar_arquivo(self, caminho_arquivo:str):
        novo_arquivo = self.cliente.files.create(
            file=open(caminho_arquivo, "rb"),
            purpose="assistants"
        )
        return novo_arquivo.id
    
    def criar_assistente(self, nome:str, instrucoes:str, modelo = 'gpt-4o', file_id = ''):
        novo_assistente = self.cliente.beta.assistants.create(
            name=nome,
            instructions=instrucoes,
            model=modelo,
            tools=[{"type": "code_interpreter"}],
            tool_resources={"code_interpreter": {"file_ids": [self.id_arquivo]}}
        )
        return novo_assistente
    
    def criar_thread(self):
        return self.cliente.beta.threads.create()
    
    def apagar_assistente(self):
        resposta = self.cliente.beta.assistants.delete(self.assistente.id)
        return resposta
    
    def apagar_thread(self):
        resposta = self.cliente.beta.threads.delete(self.thread.id)
        return resposta

    def apagar_arquivos(self):
        self.cliente.files.delete(self.id_arquivo)