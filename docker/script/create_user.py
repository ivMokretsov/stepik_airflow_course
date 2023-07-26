from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

def create_user(username, email, password):
    user = PasswordUser(models.User())
    user.username = username
    user.email = email
    user.password = password

    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()

if __name__ == "__main__":
    # Параметры пользователя
    username = 'admin'
    email = 'admin@example.com'
    password = '12345'

    # Создание пользователя
    create_user(username, email, password)
