from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    page_description = f.read()

with open("requirements.txt", "r", encoding='utf-8') as f:
    requiments = f.read().splitlines()

setup(
    name="audio-processing-teste-math_bull",
    version="0.0.3",
    author="Matheus Santos",
    description="Passo a passo da implementação de package passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type='text/markdown',
    url= "https://github.com/Mathbull/criacao-de-pacotes-em-python",
    packages= find_packages(),
    install_requires=requiments,
    python_requires='>=3.8')

