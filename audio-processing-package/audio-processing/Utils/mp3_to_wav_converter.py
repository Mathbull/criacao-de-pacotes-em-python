"""
Converter audio de formato mp3 para wav
"""
from pydub import AudioSegment

#Carregar o arquivo MP3

def convert_mp3_wav(arquivo_mp3, nome_novo_arquivo):
    """
    Converte um arquivo mp3 para wav.
    parametros:
    arquivo_mp3 (str): nome do arquivo mp3
        - nome_novo_arquivo (str): novo nome do arquivo wav, se não informado, será 'audio.wav'
    retorno:
        - None se conseguir converter, caso contrario, printa a mensagem de erro.
    """

    assert '.mp3' in arquivo_mp3, 'arquivo mp3 deve conter arquivo no formato .mp3'
    assert isinstance(nome_novo_arquivo, str), 'Nome do arquivo deve ser string'

    audio_segment = AudioSegment.from_file(arquivo_mp3, format="mp3")
    audio_segment = audio_segment.set_channels(1)
    nome_novo_arquivo = nome_novo_arquivo +'.wav' if nome_novo_arquivo  is not None else 'audio.wav'
    audio_segment.export(nome_novo_arquivo, format="wav")

