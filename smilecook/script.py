from app import *
from models.user import User
from models.recipe import Recipe
app = create_app()

user = User(username='jack', email='jack@gmail.com', password='WkQa')
db.session.add(user)
db.session.commit()