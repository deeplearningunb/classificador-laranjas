# API Classificador de Laranjas 
### Projeto Integrador 2 - Grupo 11 - 2020/1


# Esteira Seletora de Laranjas

## O Projeto

A esteira seletora de frutas, trata-se de um projeto desenvolvido coletivamente pela equipe 11, para a disciplina de Projeto Integrador para Engenharias 2. Estas engenharias englobam todos os cursos em vigência na Universidade de Brasília - Campus Gama (FGA), sendo estas, Engenharia de Software, Aeroespacial, de Energia, Automotiva e Eletrônica. 

O projeto foi idealizado como uma alternativa a seleção manual de frutas para agricultores de todos os portes, automatizando o processo utilizando inteligência artificial e mecanismos eletrônico-estruturais de engenharia para realizar tal feito. Afunilamos o escopo para o de laranjas, de forma a simplificar o escopo e viabilizar o projeto no prazo estipulado. Por se tratar da fruta mais consumida no mundo e principalmente, no Brasil, escolhemos a laranja como nosso aporte frutífero.

## Este repositório

A API do projeto foi desenvolvida com o intuito de facilitação e aplicação do treinamento obtido através do módulo de aprendizado de máquina, localizado [neste repositório](https://github.com/Projeto-Integrador-2-Grupo-11/Classificador-de-Laranjas-Modulo-de-ML). Este código contêm um módulo de inserção de imagens para a classificação do projeto, sendo usada a posteriori para enviar os resultados aos demais módulos do projeto e alimentação dos sistemas web e local.

## Requisitos para execução do código

É necessário ter as seguintes bibliotecas instaladas para a execução do projeto, além do Python 3.7+:

* Flask
* Torch
* OpenCV
* Numpy
* Keras
* Pymongo
* Base64
* Datetime

## Rodando o projeto

Para rodar o projeto é necessário rodar os seguintes comandos: 

### pip install -r requirements.txt


### sudo docker-compose up --build (Subir mongoDB)


### python3 main.py (Executar api flask)



