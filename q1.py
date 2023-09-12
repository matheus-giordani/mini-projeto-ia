import json

# Carregar a base de conhecimento do arquivo JSON
with open("base_conhecimento_animais.json", "r") as arquivo_json:
    base_conhecimento = json.load(arquivo_json)
    animais = base_conhecimento["animais"]
    caracteristicas = base_conhecimento["caracteristicas"]

def identificar_animal():
    respostas = {}
    print("Responda com 'sim' ou 'não' para as seguintes perguntas:")

    for caracteristica in caracteristicas:
        resposta = input(f"O animal tem {caracteristica}? ").lower()
        respostas[caracteristica] = resposta

    for animal in animais:
        todas_as_respostas_corretas = True
        for caracteristica, resposta_esperada in animal["caracteristicas"].items():
            resposta_usuario = respostas[caracteristica]
            if resposta_usuario != resposta_esperada:
                todas_as_respostas_corretas = False
                break
        if todas_as_respostas_corretas:
            print(f"O animal é um(a) {animal['nome']}.")
            return

    print("Animal não identificado.")

if __name__ == "__main__":
    identificar_animal()