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
    "fácil": [
        "gato", "cachorro", "maçã", "leite", "sol", "livro", "carro", "flor", "bola", "mesa",
        "porta", "janela", "cadeira", "água", "fogo", "terra", "ar", "mão", "pé", "olho",
        "nariz", "boca", "dia", "noite", "céu", "mar", "rio", "pão", "queijo", "ovo"
    ],

    "médio": [
        "casa", "escola", "amigo", "janela", "amarelo",
        "cidade", "estrada", "viagem", "tempo", "chuva",
        "vento", "montanha", "praia", "floresta", "animal",
        "comida", "bebida", "trabalho", "dinheiro", "mercado",
        "família", "história", "música", "filme", "jogo",
        "telefone", "computador", "internet", "notícia", "festa"
    ],

    "difícil": [
        "tecnologia", "universidade", "informação", "pronúncia", "imaginação",
        "desenvolvimento", "conhecimento", "responsabilidade", "comunicação", "experiência",
        "oportunidade", "necessidade", "criatividade", "inteligência", "consciência",
        "sociedade", "economia", "filosofia", "psicologia", "educação",
        "organização", "globalização", "sustentabilidade", "diversidade", "independência",
        "possibilidade", "realidade", "personalidade", "motivação", "determinação"
    ]
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























