import pyfiglet
import requests
import os

def obter_palavra_aleatoria():
    url = "https://random-word-api.herokuapp.com/word?lang=es"
    response = requests.get(url)
    palavra_aleatoria = response.json()[0]
    return palavra_aleatoria

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_boas_vindas():
    titulo = pyfiglet.figlet_format("Joga da Forca!", font="slant")
    print(titulo)
    jogador = input("Nome do jogador: ")
    print(f"\nBem-vindo, {jogador}!")

def inicializar_palavra_secreta():
    palavra_secreta = obter_palavra_aleatoria()
    return palavra_secreta

def esconder_palavra(palavra):
    return "_" * len(palavra)

def exibir_forca(tentativas_restantes):
    forca = [
        "  ◯ ",
        " -|-",
        " _|_"
    ]
    for linha in forca:
        print(linha)
    print(f"Tentativas restantes: {tentativas_restantes}")

def adivinhar_letra(palavra_secreta, palavra_atual, letra):
    nova_palavra = ""
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            nova_palavra += letra
        else:
            nova_palavra += palavra_atual[i]
    return nova_palavra

def main():
    limpar_tela()
    exibir_boas_vindas()
    palavra_secreta = inicializar_palavra_secreta()
    palavra_atual = esconder_palavra(palavra_secreta)
    tentativas_restantes = 7

    while tentativas_restantes > 0 and "_" in palavra_atual:
        limpar_tela()
        exibir_forca(tentativas_restantes)
        print(f"Palavra: {palavra_atual}")
        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            print(f"A letra '{letra}' está na palavra!")
            palavra_atual = adivinhar_letra(palavra_secreta, palavra_atual, letra)
        else:
            print(f"A letra '{letra}' não está na palavra!")
            tentativas_restantes -= 1

    limpar_tela()
    if "_" not in palavra_atual:
        print(f"Parabéns! Você ganhou! A palavra era '{palavra_secreta}'.")
    else:
        print(f"Você perdeu! A palavra era '{palavra_secreta}'.") 

if __name__ == "__main__":
    main()
