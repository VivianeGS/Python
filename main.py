# Programa reproduz o conteúdo de um arquivo txt em áudio.

import pyttsx3
import cowsay

texto= open('C:/Users/Viviane/PycharmProjects/Speaker/texto_python.txt', encoding='UTF8')
texto = texto.read()
cowsay.cow(texto)       # animação vaquinha
speaker = pyttsx3.init()
speaker.say(texto)
speaker.runAndWait()
