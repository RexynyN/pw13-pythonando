## Configurações iniciais

Primeiro devemos criar o ambiente virtual:

```python
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv
```

Após a criação do venv vamos ativa-lo:

```python
#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Agora vamos fazer a instalação do Django e as demais bibliotecas:

```python
pip install django pillow
```

Vamos criar o nosso projeto Django:

```jsx
django-admin startproject core .
```

Rode o servidor para testar:

```jsx
python manage.py runserver
```

Crie o app usuario:

```jsx
python manage.py startapp usuarios
```


Fazer uma Migração 
```python
python manage.py migrate 
```

Criar uma migration de um model
```python
python manage.py makemigrations
```
