from app import create_app, db
from config import Config

app = create_app(Config)

def drop_all_tables():
    with app.app_context():
        db.drop_all()
        print('All tables have been dropped!')

if __name__ == '__main__':
    drop_all_tables()