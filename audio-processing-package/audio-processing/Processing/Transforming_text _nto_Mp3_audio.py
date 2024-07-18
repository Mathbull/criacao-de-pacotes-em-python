"""
Recebe uma frase e retorna um audio
"""

import gtts

def converter_audio(frase, name_audio):
    """
    Recebe uma frase e retorna um audio
    """
    assert isinstance(frase, str), 'Voce deve entrar com uma string'
    assert name_audio is not None, 'Voce deve entrar para o nome do audio'
    frase = gtts.gTTS(frase, lang='pt-br')
    frase.save(name_audio+'.mp3')

