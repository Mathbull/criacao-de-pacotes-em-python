"""
Ouvir de qualquer entrata de audio o que o usuário disser e te retornará em texto oq vc disse
"""
import speech_recognition as sr


def reconhecer_fala(mensagm_incial = None, quem_disse=None ):
    """
    Ouvindo de qualquer entrada de audio o que o usuário disser e te retornará em texto oq vc disse
    parametros:
        - mensagm_incial (str): Mensagem inicial para o usuario
        - quem_disse (str): Quem disse a frase. Utilizado para identificar quando não é necessário retornar a frase.
    retorno:
        - str: O texto que foi transcrito do áudio
    """

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        if(mensagm_incial == 'not_messagem'):
            pass
        else:
            print("Diga alguma coisa: " if mensagm_incial is None else mensagm_incial)
        audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(audio, language='pt-br')
            if quem_disse == 'not_messagem':
                pass
            else:
                print("Você disse: "+ frase if quem_disse is None else quem_disse + frase)
            return frase
        except Exception as e:
            print(f'Não entendi oq vc disse {e}')          

