from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MahasiswaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    umur = db.Column(db.Integer, nullable=False)
    daerah = db.Column(db.String(50), nullable=False)