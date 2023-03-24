# django1 - projeto web simples

Desenvolvimento de um simples CRUD de produtos utilizando Python e Django, como descrito 
no curso https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/

## Para rodar a app: 

```bash
python -m venv venv
```

```bash
Linux:
source venv/bin/activate
OU
. venv/bin/activate
```

```bash
Windows:
.\venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

## Criando um usuário no painel admin:

```bash
python manage.py createsuperuser
```

- Após a criação do superuser, basta rodar a app e digitar no final do 
- endereço/admin para realizar o login

#### Dependências:
- python: 3.11
- django: 4.1
