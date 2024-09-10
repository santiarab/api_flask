<<<<<<< HEAD
import os
from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
=======
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 02204442b951446d6cb5401ade7015d89e25e12f
