from flask_migrate import Migrate
from flask_script import Manager
from app01 import create_app, db
from app01.user.model import User
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    manager.run()




