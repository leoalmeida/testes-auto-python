from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *
from assistente_projeto import *
import openai

def main():
    #pedido_usuario = input("Digite um caso de uso: ")
    pedido_usuario = "Ana deseja realizar login na plataforma AcordeLab"
    pagina_considerada = "index"
    
    try:
        lista_ids_arquivos,mapa_arquivos = criar_lista_ids_app_web(diretorio="docs")
        vs_id = criar_vector_store(lista_ids_arquivos)
        assistente = criar_assistente(vs_id=vs_id, modelo=MODELO_GPT_4_1)
        thread = criar_thread()

        caso_de_uso = gerar_casos_uso(prompt=pedido_usuario,assistente=assistente,thread=thread)
        print("\nCaso de Uso:\n", caso_de_uso)

        cenario_teste = gerar_cenarios_teste(caso_uso=caso_de_uso, documento=pagina_considerada,dicionario_arquivos=mapa_arquivos, assistente=assistente,thread=thread)
        print("\nCenario Teste\n", cenario_teste)

        script_teste = gerar_script_teste(caso_de_uso, documento=pagina_considerada, dicionario_arquivos=mapa_arquivos, assistente=assistente, thread=thread)
        print("\nScript Teste\n", script_teste)

        salva(f"scripts_gerados/script_{pagina_considerada}.py", script_teste)
    except openai.APIError as e:
        print("Erro ao gerar o script de teste.", e)
    finally:
        print("Apagando assistente e arquivos...")
        apagar_arquivos(lista_ids_arquivos)
        apagar_assistente(assistente.id)
        apagar_thread(thread.id)

if __name__ == "__main__":
    main()