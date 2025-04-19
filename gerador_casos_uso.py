from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPΕΝΑΙ_API_KEY"))

def gerar_casos_uso(prompt, assistente, thread, modelo=MODELO_GPT_4_1):
    pergunta = f"""Gere um caso de uso para: {prompt}. 
                Para isso, busque nos arquivos associados a você o conteúdo # Exemplos de Caso de Uso
                (no arquivo exemplos_casos_uso.txt)

                Adote o formato de saída abaixo.

                # Formato de Saída

                *Nome da Persona*, em *contexto do app*, precisa realizar *tarefa no app* no aplicativo. Logo, *Beneficio Esperado*, para isso ela *descrição detalhada da tarefa realizada*.

                """
    cliente.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=pergunta
    )

    run = cliente.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistente.id,
        tools=[{"type":"file_search"}],
        model=modelo
    ) 

    ran = cliente.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    
    while ran.status != STATUS_COMPLETED:
        print("Gerando Caso: ", ran.status)
        ran = cliente.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if ran.status == STATUS_FAILED:
            raise Exception("Erro na execução")

    mensagens = cliente.beta.threads.messages.list(
        thread_id = thread.id
    )

    return mensagens.data[0].content[0].text.value	