from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import db, MahasiswaModel

mahasiswa_put_args = reqparse.RequestParser()
mahasiswa_put_args.add_argument("Nama", type=str, required=True)
mahasiswa_put_args.add_argument("Daerah", type=str, required=True)
mahasiswa_put_args.add_argument("Umur", type=int, required=True)

mahasiswa_update_args = reqparse.RequestParser()
mahasiswa_update_args.add_argument("Nama", type=str)
mahasiswa_update_args.add_argument("Daerah", type=str)
mahasiswa_update_args.add_argument("Umur", type=int)

resource_fields = {
    'id': fields.Integer,
    'nama': fields.String,
    'umur': fields.Integer,
    'daerah': fields.String
}

class absenMahasiswa(Resource):
    @marshal_with(resource_fields)
    def get(self, stambuk):
        result = MahasiswaModel.query.filter_by(id=stambuk).first()
        if not result:
            abort(404, message="Hasil dari stambuk tidak ditemukan")
        return result

    @marshal_with(resource_fields)
    def put(self, stambuk):
        args = mahasiswa_put_args.parse_args()
        result = MahasiswaModel.query.filter_by(id=stambuk).first()
        if result:
            abort(409, message="Stambuk sudah terdaftar...")

        mahasiswa = MahasiswaModel(
            id=stambuk,
            nama=args['Nama'],
            umur=args['Umur'],
            daerah=args['Daerah']
        )
        db.session.add(mahasiswa)
        db.session.commit()
        return mahasiswa, 201

    @marshal_with(resource_fields)
    def patch(self, stambuk):
        args = mahasiswa_update_args.parse_args()
        result = MahasiswaModel.query.filter_by(id=stambuk).first()
        if not result:
            abort(404, message="Mahasiswa tidak ditemukan, tidak bisa memperbarui!...")

        if args['Nama']:
            result.nama = args['Nama']
        if args['Daerah']:
            result.daerah = args['Daerah']
        if args['Umur']:
            result.umur = args['Umur']

        db.session.commit()
        return result

    def delete(self, stambuk):
        mahasiswa = MahasiswaModel.query.get(stambuk)
        if not mahasiswa:
            abort(404, message="Mahasiswa tidak ditemukan")
        db.session.delete(mahasiswa)
        db.session.commit()
        return '', 204