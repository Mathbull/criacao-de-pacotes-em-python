<div align="center" id="top"> 
  <img src="./.github/packge_.jpg" alt="Criacao De Pacotes Em Python" />
</div>


# Criação De Pacotes Em Python
O projeto tem como objetivo aplicar os conhecimentos adquiridos durante o curso "Descomplicando a criação de pacotes de processamento de imagens em Python" ministrado por Karina Kato na plataforma Digital Innovation One (DIO).

A ideia principal do projeto é desenvolver um pacote Python que inclua uma função para converter texto em áudio. O pacote será chamado `text_to_speech` e conterá um módulo chamado `converter`. O módulo `converter` terá uma função chamada `converter_audio` que receberá uma frase e um nome de arquivo como parâmetros e retornará um arquivo de áudio com a frase em português.

A função `converter_audio` utilizará a biblioteca `gtts` (Google Text-to-Speech) para converter a frase em um arquivo de áudio. O código fornecido é um exemplo de como usar a função `converter_audio` para converter uma frase em um arquivo de áudio chamado `hello_world.mp3`.

A refatoração do código fornecido para o novo pacote `text_to_speech` pode ser feita da seguinte maneira:

1. Criar uma pasta chamada `text_to_speech`.
2. Dentro da pasta `text_to_speech`, criar um arquivo chamado `__init__.py`. Este arquivo pode estar vazio, mas é necessário para que a pasta seja considerada um pacote Python.
3. Dentro da pasta `text_to_speech`, criar uma pasta chamada `converter`.
4. Dentro da pasta `converter`, criar um arquivo chamado `__init__.py`. Este arquivo também pode estar vazio.
5. Dentro da pasta `converter`, criar um arquivo chamado `converter.py`.
6. No arquivo `converter.py`, copiar e colar o código fornecido, modificando-o para importar as bibliotecas necessárias e para fazer a função `converter_audio` parte do módulo `converter`.
7. Atualizar o código no arquivo `converter.py` para que a função `converter_audio` seja exportada como um módulo.
8. Criar um arquivo chamado `requirements.txt` na raiz do pacote e listar as dependências do pacote, como `gtts`.
9. Atualizar o código no arquivo `converter.py` para que a função `converter_audio` possa ser usada como parte do pacote `text_to_speech`.

Com essas alterações, o código fornecido será refatorado para formar um pacote Python que pode ser usado em outros projetos.
