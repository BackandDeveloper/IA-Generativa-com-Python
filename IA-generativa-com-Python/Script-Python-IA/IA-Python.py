## Nome: Pedro Henrique 
## Curso: IA Google 
## Trabalho do curso de IA. Padrão a ser seguido no desenvolvimento de uma IA: 

# Estrutura de código para criação de uma IA:

import openai

## Chave API que tem que ser gerada no site da OPEN AI:
openai.api_key = ''

def gerar_resposta(pergunta):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pergunta,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Bem-vindo ao Chatbot IA Generativa!")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit"]:
            break
        resposta = gerar_resposta(pergunta)
        print("IA: " + resposta)

if __name__ == "__main__":
    main()
