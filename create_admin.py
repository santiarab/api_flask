from app import create_app
from app.auth.models import User
from config import Config

app = create_app(Config)

def create_admin():
    with app.app_context():
        existing_user = User.get_by_username(username='admin')
        if existing_user:
            print('Admin user already exists!')
            return
        admin_user = User(username='admin')
        admin_user.is_admin = True
        admin_user.set_password('123')
        admin_user.save()
        print('Admin user created!')

if __name__ == '__main__':
    create_admin()