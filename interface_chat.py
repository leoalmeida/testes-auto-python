from openai import OpenAI
from assistente_base import AssistenteBase
import os

STATUS_COMPLETED = "completed"

class InterfaceChat():
    def __init__(self, nome:str, instrucoes:str, caminho_arquivo:str):
        self.chat: AssistenteBase = AssistenteBase(nome, instrucoes, caminho_arquivo)
        self.mensagens = []
        
    def conversar(self, mensagem:str):
        self.chat.cliente.beta.threads.messages.create(
            thread_id=self.chat.thread.id,
            role="user",
            content=mensagem
        )
        run = self.chat.cliente.beta.threads.runs.create_and_poll(
            thread_id=self.chat.thread.id,
            assistant_id=self.chat.assistente.id
        ) 

        if run.status == STATUS_COMPLETED:
            self.mensagens = self.chat.cliente.beta.threads.messages.list(
                thread_id=self.chat.thread.id
            ).data[0].content
        return self.mensagens
    
    def apagar_assistente(self):
        self.chat.apagar_arquivos()
        self.chat.apagar_thread()
        self.chat.apagar_assistente()