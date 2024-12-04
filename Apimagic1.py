import json
import requests
from deep_translator import GoogleTranslator

url = 'https://api.adviceslip.com/advice'

def linha(tamanho=40):
    
    return '-' * tamanho


def menu_principal():
    print('\n')
    print(linha())
    print('    🍹 Cachaçaria do Seu Zé 🍹')
    print(linha())
    print('         Conselhos Digitais')
    print('  "Porque até uma boa dose merece um bom conselho."')
    print(linha())
    print('1. Receber conselhos digitais.')
    print('2. Relembrar conselhos guardados.')
    print('3. Encerrar o programa.')
    print(linha())
    
    while True:
        try:
            opcao = int(input('👉 Escolha uma opção: '))
            if opcao in [1, 2, 3]:
                return opcao
            else:
                print('🚫 Opção inválida! Escolha entre 1, 2 ou 3.')
        except ValueError:
            print('🚫 Letras ou caracteres são inválidos! Digite um número válido.')


def ouvir_seu_ze():
    print('\n' + linha())
    print('📜 Vamos buscar sabedoria!')
    print('Quantos conselhos digitais você deseja receber?')
    print(linha())
    try:
        num = int(input('👉 Digite o número de conselhos: '))
        conselhos = []
        print('\n' + linha())
        for i in range(num):
            response = requests.get(url)
            data = response.json()
            conselho = data["slip"]["advice"]
            id_conselho = data["slip"]["id"]
            conselhos.append({"id": id_conselho, "conselho": conselho})
            print(f'🔹 Conselho {i+1}: {conselho}')
        print(linha())
        return conselhos
    except ValueError:
        print('🚫 Número inválido! Voltando ao menu...')
        return []


def salvar_conselhos(conselhos):
    print('\n' + linha())
    if not conselhos:
        print('🚫 Não há conselhos para salvar. Peça novos primeiro.')
        return
    with open('conselhos_seu_ze.txt', 'a', encoding='utf-8') as arquivo:
        for item in conselhos:
            arquivo.write(f"ID: {item['id']} - Conselho: {item['conselho']}\n")
    print('✅ Conselhos salvos com sucesso!')
    print(linha())


def mostrar_conselhos_guardados():
    print('\n' + linha())
    try:
        with open('conselhos_seu_ze.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print('📜 Conselhos Guardados:')
                print(linha())
                print(conteudo)
                print(linha())
            else:
                print('🚫 Nenhum conselho salvo até o momento.')
    except FileNotFoundError:
        print('🚫 Arquivo de conselhos não encontrado. Parece que você ainda não salvou nenhum.')


def traduzir_conselhos(conselhos):
    print('\n' + linha())
    if not conselhos:
        print('🚫 Não há conselhos para traduzir. Peça novos primeiro.')
        return
    print('🔄 Traduzindo conselhos...')
    print(linha())
    for item in conselhos:
        traduzido = GoogleTranslator(source='auto', target='pt').translate(item['conselho'])
        print(f"ID: {item['id']} - Conselho Traduzido: {traduzido}")
    print(linha())


def main():
    while True:
        opcao = menu_principal()
        if opcao == 1:
            conselhos = ouvir_seu_ze()
            print('\n' + linha())
            print('O que deseja fazer com os conselhos recebidos?')
            print(linha())
            print('1. Salvar conselhos no arquivo.')
            print('2. Traduzir conselhos para português.')
            print('3. Voltar ao menu principal.')
            print(linha())
            escolha = int(input('👉 Escolha uma opção: '))
            if escolha == 1:
                salvar_conselhos(conselhos)
            elif escolha == 2:
                traduzir_conselhos(conselhos)
        elif opcao == 2:
            mostrar_conselhos_guardados()
        elif opcao == 3:
            print(linha())
            print('🍹 Até a próxima, Seu Zé! Obrigado por confiar nos conselhos digitais. 🥃')
            print(linha())
            break

if __name__ == "__main__":
    main()
