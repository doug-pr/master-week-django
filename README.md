# Requisitos
* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* MySQL 8 ou superior - Conferir a versão: mysql --version

## Sequência para criar projeto
Instalar o Django:
´´´
pip install Django
´´´

Criar o projeto com Django:
´´´
django-admin startproject admin .
´´´

Rodar o projeto:
´´´
python manage.py runserver
´´´

Instalar conector MySQL:
´´´
pip install mysqlclient
´´´

Criar a Base de Dados:
´´´
create database django_celke character set utf8mb4 collate utf8mb4_unicode_ci;
´´´

Alterar no arquivo "settings.py" as credenciais do banco de dados:
´´´
'ENGINE': 'django.db.backends.mysql',
'NAME': 'nome-do-banco-de-dados',
'USER': 'nome-do-usuario',
'PASSWORD': 'senha',
'HOST': 'endereco',
'PORT': 3306
´´´

Executar as Migrations para criar as tabelas:
´´´
python manage.py migrate
´´´

