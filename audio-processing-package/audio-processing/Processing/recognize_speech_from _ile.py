"""
Modulo para reconhcer audio.wav de algum arquivo
"""
import speech_recognition as sr

def reconhecer_fala_de_arquivo(arquivo_audio):
    """
    Reconhece a frase dada em um arquivo audio.wav
    parametro:
        - arquivo_audio (str): Caminho do arquivo.wav a ser reconhecido
    retorno:
        - str: Frase reconhecida
    """
    assert '.wav'  in arquivo_audio, 'Nesseraio arquivo no formato .wav'

    microfone = sr.Recognizer()
    with sr.AudioFile(arquivo_audio) as source:
        audio = microfone.record(source)

        try:
            frase = microfone.recognize_google(audio, language='pt-br')
            print("Você disse: "+ frase)
            return frase
        except Exception as e:
            print(f'Não entendi oq vc disse {e}')

testando_mpe= 'audio.wav'

reconhecer_fala_de_arquivo(arquivo_audio=testando_mpe)
