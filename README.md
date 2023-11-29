<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="200"/>
</p>

## Consumidor RabbitMQ

Este script conecta-se a um Message Broker RabbitMQ, declara uma fila e consome mensagens dessa fila. As mensagens recebidas são registradas com informações detalhadas.
Instalação

## Instale o Python:

Certifique-se de ter o Python instalado no seu sistema. Você pode baixar o Python em python.org.

## Instale as Bibliotecas:

Abra um terminal e execute o seguinte comando para instalar a biblioteca pika:

    pip install pika

## Utilização



Execute o script do consumidor com o seguinte comando:

    python consumidor.py

#### Monitore a Saída:

O script do consumidor começará a aguardar mensagens na fila especificada. Monitore o terminal para mensagens de log que fornecem detalhes sobre as mensagens recebidas.

## Formato de Log:

O formato de log está configurado para data/hora, nível de log e duas quebras de linha entre cada log. 