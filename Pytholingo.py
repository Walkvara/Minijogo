import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

words_by_level = {
    "fácil": ["gato", "cachorro", "maçã", "leite", "sol", "livro", "carro", "flor", "bola", "mesa"],
    "médio": ["casa", "escola", "amigo", "janela", "amarelo"],
    "difícil": ["tecnologia", "universidade", "informação", "pronúncia", "imaginação"]
}

print("--------Olá amigo! Eu sou o Pytholingo. Eu estou aqui para te ajudar a aprender idiomas.--------")
sd.wait(3)
print("--------Por agora iremos começar pelo inglês. Já que é a língua mais falada no mundo.--------")
sd.wait(3)
difficulty = ("Escolha por favor um nível de dificuldade: 1 - Fácil, 2 - Médio, 3 - Difícil"
" Darei 10 segundos para escolher, ok :)")

int(input(difficulty))

sd.wait(10)

if difficulty == 1:
        print("Você escolheu o nível fácil. Vamos começar com palavras simples.")
        print("Vamos começar a brincadeira!!!")
        print("Eu vou dar 10 segundos para você se preparar, e depois você terá 5 segundos para falar a palavra que eu disser. Ok :)")
        sd.wait(10)

























