import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = openai.Client()

mensagens = []

def geracao_texto(mensagens):

    resposta = client.chat.completions.create(
        mensagens=mensagens,
        model='gpt-3.5-turbo-0125',
        temperature=0,
        max_tokens=100,
        stream=True
    )

    print('Assistant: ', end='')
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()

    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens

if __name__ == '__main__':

    print('Bem-vindo ao chat bot do Champs!')
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens = [{'role': 'user', 'content': input_usuario}]
        mensagens = geracao_texto(mensagens)