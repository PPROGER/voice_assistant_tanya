#!/usr/bin/python3
import os
from voice_commands import listen
from db_connect import con


def Load_command_voice():
    list_vopros = []
    list_otvet = []
    for vopros,otvet in con.execute("SELECT vopros, otvet FROM voice_assistant"):
        list_vopros.append(str(vopros))
        list_otvet.append(str(otvet))
    return list_vopros, list_otvet      

def voice_vopros():
    text_voprosa, text_otveta = Load_command_voice()
    otvet_bool = True
    os.system("echo «Говорите» | RHVoice-test -p anna")
    comand_text_vopros = listen()
    for i in range(len(text_voprosa)):
        if(text_voprosa[i] == comand_text_vopros):
            os.system("echo "+text_otveta[i]+" | RHVoice-test -p anna")
            otvet_bool = False
    if(otvet_bool == True):
        os.system("echo «Не знаю, может подскажешь?» | RHVoice-test -p anna")
        comand_text_otvet = listen()
        cur = con.cursor()
        cur.execute('INSERT INTO voice_assistant (vopros, otvet) VALUES (?,?)',(str(comand_text_vopros),str(comand_text_otvet)))
        con.commit()
        os.system("echo «Запомнила» | RHVoice-test -p anna")
        text_voprosa, text_otveta = Load_command_voice()
        voice_vopros()
voice_vopros()



#os.system("echo «Эта программа создана для обнаружения обьектов на камере, фото и видео материалах» | RHVoice-test -p anna")
