# Code based on the flask-admin examples
# https://github.com/flask-admin/flask-admin/tree/master/examples/sqla

import os
import os.path as op
from random import randrange
from socket import gethostname

from flask import Flask
import flask_admin
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy


# Create application
app = Flask(__name__)

# Create dummy secret key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Create models
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(120))
    zip_code = db.Column(db.String(120))

    # Required for administrative interface.
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

admin = flask_admin.Admin(app, name='Persons', template_mode='bootstrap3',
                            index_view=flask_admin.AdminIndexView(
                                name='Home',
                                template='admin/index.html',
                                url='/'
                            ))
admin.add_view(sqla.ModelView(Person, db.session))


def build_sample_db():
    import datetime

    db.drop_all()
    db.create_all()

    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    user_list = []
    for i in range(len(first_names)):
        user = Person()
        user.first_name = first_names[i]
        user.last_name = last_names[i]
        user.date_of_birth = datetime.date(randrange(1940, 2006),
                                           randrange(1, 12),
                                           randrange(1, 29))
        user.zip_code = "%05d" % (randrange(501, 99950))
        user_list.append(user)
        db.session.add(user)

    db.session.commit()
    return

if __name__ == '__main__':
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Necessary to have the code run on PythonAnywhere.com
    if 'liveconsole' not in gethostname():
        app.run()