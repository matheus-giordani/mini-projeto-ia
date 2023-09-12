import json

# Carregar a base de conhecimento do arquivo JSON
with open("base_conhecimento_doenças.json", "r") as arquivo_json:
    base_conhecimento = json.load(arquivo_json)
    doencas = base_conhecimento["doenças"]
    caracteristicas = base_conhecimento["caracteristicas"]

def identificar_doenca():
    respostas = {}
    print("Responda com 'sim' ou 'não' para as seguintes perguntas:")

    for caracteristica in caracteristicas:
        resposta = input(f"O doença tem {caracteristica}? ").lower()
        respostas[caracteristica] = resposta

    for doenca in doencas:
        todas_as_respostas_corretas = True
        for caracteristica, resposta_esperada in doenca["caracteristicas"].items():
            resposta_usuario = respostas[caracteristica]
            if resposta_usuario != resposta_esperada:
                todas_as_respostas_corretas = False
                break
        if todas_as_respostas_corretas:
            print(f"A doença é {doenca['nome']}.")
            return

    print("doença não identificado.")

if __name__ == "__main__":
    identificar_doenca()