<h1 align="Center">
  Criar o projeto e gerar as distribuições
</h1>

# Distribuições

Para subir o pacote, criar uma distribuição binária ou distribuição de código fonte.
As versões mais recentes do pip instalam primeiramente a binária e usam a distribuição de código fonte, apenas se necessário.
De qualquer forma, iremos criar ambas distribuições.

## Passos para gerar as distribuições
1. Acessar a raiz do projeto;
2. Comando de instalação;
3. Comando para a distribuição.

## Comandos de instalação
```
python -m pip install --upgrade pip

```

``` 
python -m pip install --user twine

```

``` 
python -m pip install --user setuptools

```

## Comandos para criar distribuições

``` 
python setup.py sdist bdist_wheel
	
```

## Exemplos de estruturas de pacotes
### Simples:
``` 
project_name/
    README.md
    setup.py
    requirements.txt
    package_name/
        __init__.py
        file1_name.py
        file2_name.py
```
* O __init__.py serve para sejam chamados como modulos
* Exemplos de chamadas a file1_name:
``` 
import package_name.file1_name
from package_name import file1_name
    
```

### Com vários modulos: 
``` 
project_name/
  README.md
  setup.py
  requirements.txt
  package_name/
      __init__.py
      module1_name/
          __init__.py
          file1_name.py
          file2_name.py
      module2_name/
          __init__.py
          file1_name.py
          file2_name.py

```
* Exemplos de chamadas a file1_name:
  
``` 
import package_name.module1_name.file1_name
from package_name.module1_name import file1_name

```
