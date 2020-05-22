from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)

db: SQLAlchemy = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#  ADMIN

from models import *
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))


# Flask security

user_datastore = SQLAlchemyUserDatastore(db, user_model=User, role_model=Role)
security = Security(app, datastore=user_datastore)