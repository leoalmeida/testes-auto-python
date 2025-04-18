from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *

def main():
    caso_de_uso = gerar_casos_uso()
    print(caso_de_uso)

    cenario_teste = gerar_cenarios_teste(caso_de_uso)
    print("\nCenario Teste\n", cenario_teste)

    script_teste = gerar_script_teste(caso_de_uso, cenario_teste)
    print("\nScript Teste\n", script_teste)

    salva("script_temp_ia.py", script_teste)

if __name__ == "__main__":
    main()