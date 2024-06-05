Iniciar o projeto Django

python -m venv venv
venv\Scripts\activate
pip install django
pip install -r requirements.txt (in case you have a requirements.txt file)
django-admin startproject project .
python manage.py startapp contact

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


# Migrando a basse de dados do Django
'''
python manage.py makemigrations
python manage.py migrate
'''

# Criando e modificando a senha de um superuser do Django
'''
python manage.py createsuperuser
python manage.py changepassword USERNAME
'''

