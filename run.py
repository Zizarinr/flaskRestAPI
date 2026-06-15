from flask import Flask
from flask_restful import Api
from models import db
from resources.mahasiswa import absenMahasiswa

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app) # Menghubungkan SQLAlchemy dengan App

api.add_resource(absenMahasiswa, "/Mahasiswa/<int:stambuk>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)