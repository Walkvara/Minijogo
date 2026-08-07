import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import time
import os

translator = Translator()
recognizer = sr.Recognizer()

words_by_level = {
    "fácil": ["gato", "cachorro", "maçã", "leite", "sol", "livro", "carro", "flor", "bola", "mesa"],
    "médio": ["casa", "escola", "amigo", "janela", "amarelo"],
    "difícil": ["tecnologia", "universidade", "informação", "pronúncia", "imaginação"]
}

# limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# escolher dificuldade
def escolher_dificuldade():
    while True:
        escolha = input("Escolha: 1-Fácil | 2-Médio | 3-Difícil: ")
        if escolha == "1":
            return "fácil"
        elif escolha == "2":
            return "médio"
        elif escolha == "3":
            return "difícil"
        else:
            print("Escolha inválida 😅")

# escolher modo de resposta
def escolher_modo_resposta():
    while True:
        print("\nModo de resposta:")
        print("1. Voz 🎤")
        print("2. Digitar ⌨️")

        escolha = input("Escolha: ")

        if escolha == "1":
            return "voz"
        elif escolha == "2":
            return "texto"
        else:
            print("Escolha inválida 😅")

# 🎮 FUNÇÃO BASE
def jogar_base(vidas):
    limpar()
    print("🎮 Iniciando jogo...\n")

    level = escolher_dificuldade()
    modo = escolher_modo_resposta()

    score = 0
    rodada = 0

    while True:
        if vidas is not None and vidas <= 0:
            break

        rodada += 1
        palavra = random.choice(words_by_level[level])
        traducao = translator.translate(palavra, src='pt', dest='en').text

        print(f"\n🔹 Rodada {rodada}")
        print(f"Diga em inglês: {palavra}")
        time.sleep(1)

        try:
            if modo == "voz":
                print("🎤 Gravando...")

                duration = 5
                fs = 44100
                recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
                sd.wait()
                wav.write("audio.wav", fs, recording)

                with sr.AudioFile("audio.wav") as source:
                    audio = recognizer.record(source)

                resposta = recognizer.recognize_google(audio).lower()
                print(f"🗣️ Você disse: {resposta}")

            else:
                resposta = input("Digite a tradução: ").lower()

            if traducao.lower() in resposta:
                print("✅ Acertou! +10 pontos 🔥")
                score += 10
            else:
                print(f"❌ Errou! Era: {traducao}")
                if vidas is not None:
                    vidas -= 1

        except:
            print("⚠️ Não entendi 😢")
            if vidas is not None:
                vidas -= 1

        # status
        if vidas is not None:
            print(f"⭐ Pontos: {score} | ❤️ Vidas: {vidas}")
        else:
            print(f"⭐ Pontos: {score} | ♾️ Infinito")

        time.sleep(1)

    print("\n💀 Fim do jogo!")
    print(f"🏆 Pontuação final: {score}")

    if vidas == 0:
        print("Você perdeu todas as vidas 😵")
    elif score >= 50:
        print("Você amassou 😎🔥")
    elif score >= 20:
        print("Mandou bem 👏")
    else:
        print("Treina mais :( ok?")

    input("\nPressione ENTER para voltar ao menu...")

# modos
def jogar_normal():
    jogar_base(vidas=3)

def jogar_infinito():
    jogar_base(vidas=None)

def jogar_vida_unica():
    jogar_base(vidas=1)

# menu
while True:
    limpar()
    print("====== 🎮 PYTHOLINGO 🎮 ======")
    print("1. Jogar")
    print("2. Modo infinito")
    print("3. Vida única")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        jogar_normal()
    elif opcao == "2":
        jogar_infinito()
    elif opcao == "3":
        jogar_vida_unica()
    elif opcao == "4":
        print("Saindo... até mais 😄")
        break
    else:
        print("Opção inválida 😅")
        time.sleep(1)
























