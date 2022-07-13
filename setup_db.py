from flask_sqlalchemy import SQLAlchemy

# Создаем объект алхимии, который будут использовать все:
# И модели,
# и приложение,
# и блупринты.

db = SQLAlchemy()