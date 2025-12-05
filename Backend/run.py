from app.init import create_app
from config import DevelopmentConfig
from app.extensions import db
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run(debug=True)
