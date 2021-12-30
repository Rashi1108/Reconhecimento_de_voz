from re import L
import speech_recognition as sr
import os
import time
import pyautogui

while True:
    def nsa():

        pyautogui.PAUSE = 1

        #abrindo o google
        os.startfile('https://nsa.cps.sp.gov.br/')

        #login nsa
        pyautogui.moveTo(x=918, y=542)
        pyautogui.leftClick()
        pyautogui.write('20340')
        pyautogui.moveTo(x=1111, y=516)
        pyautogui.leftClick()
        pyautogui.write('056')
        pyautogui.moveTo(x=861, y=621)
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(x=1110, y=681)
        pyautogui.leftClick()
        time.sleep(1)

    def luz_acesa():

        pyautogui.PAUSE = 1

        #entra no emulador de android
        os.startfile('D:\LDPlayer\LDPlayer4.0\dnplayer.exe')
        time.sleep(15)

        #entra no aplicativo da positivo
        pyautogui.moveTo(934,250)
        pyautogui.leftClick()
        time.sleep(8)

        #liga a luz e fecha o emulador, para não influenciar o apagar da luz
        pyautogui.moveTo(1186,378)
        pyautogui.leftClick()
        pyautogui.moveTo(1236,10)
        pyautogui.leftClick()
        pyautogui.moveTo(1027,624)
        pyautogui.leftClick()

    def luz_apagada():

        pyautogui.PAUSE = 1

        #entra no emulador de android
        os.startfile('D:\LDPlayer\LDPlayer4.0\dnplayer.exe')
        time.sleep(15)

        #entra no aplicativo da positivo
        pyautogui.moveTo(934,250)
        pyautogui.leftClick()
        time.sleep(8)

        #desliga a luz e fecha o emulador, para não influenciar o acender da luz
        pyautogui.moveTo(1186,378)
        pyautogui.leftClick()
        pyautogui.moveTo(1236,10)
        pyautogui.leftClick()
        pyautogui.moveTo(1027,624)
        pyautogui.leftClick()

    def email():

        pyautogui.PAUSE = 1

        #abrindo o google
        os.startfile('https://outlook.live.com/owa/')
        time.sleep(2)

        #login email
        pyautogui.moveTo(1398,128)
        pyautogui.leftClick()
        pyautogui.moveTo(802,515)
        pyautogui.leftClick
        time.sleep(1)
        pyautogui.click(clicks=3, interval=0.10)
        pyautogui.write('seu e-email')
        pyautogui.moveTo(1077,708)
        pyautogui.leftClick()
        pyautogui.moveTo(1068,651)
        pyautogui.leftClick()
        time.sleep(2)
        pyautogui.leftClick()
        time.sleep(4)

    #Função para ouvir e reconhecer a fala
    def ouvir_microfone():
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print("Diga alguma coisa: ")
            
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')

            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            
            #reconhecem frases presentes em 'frase', executando funções
            if "escrever um texto" in frase:
                os.system("start WINWORD.exe")

            if "escola" in frase:
                nsa()
            
            if "e-mail educacional" in frase:
                email()

            if "apresentação" in frase:
                os.system("start POWERPNT.exe") 

            if 'Acender luz' in frase:
                luz_acesa()

            if 'apagar luz' in frase:
                luz_apagada()

        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            print("Não entendi")

    ouvir_microfone()