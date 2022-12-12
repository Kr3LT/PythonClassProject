from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class LoaiSanPhams(db.Model):
    __tablename__ = 'LoaiSanPhams'
    MaLoaiSanPham = db.Column(db.Integer, primary_key=True)
    TenLoaiSanPham = db.Column(db.String(128))


class SanPhams(db.Model):
    __tablename__ = 'SanPhams'
    MaSanPham = db.Column(db.Integer, primary_key=True)
    TenSanPham = db.Column(db.String(128))
    Thumbnail = db.Column(db.String(128))
    MaLoaiSanPham = db.Column(db.Integer, db.ForeignKey('LoaiSanPhams.MaLoaiSanPham', ondelete = "CASCADE"))
    ChitietSanPham = db.relationship("ChiTietSanPhams",backref='chitiet', lazy='dynamic')


class ChiTietSanPhams(db.Model):
    __tablename__ = 'ChiTietSanPhams'
    MaChiTietSanPham = db.Column(db.Integer, primary_key=True)
    MaSanPham = db.Column(db.Integer, db.ForeignKey('SanPhams.MaSanPham'))
    RAM = db.Column(db.String(128))
    ROM = db.Column(db.String(128))
    AnhTo = db.Column(db.String(128))
    AnhNho = db.Column(db.String(128))
    Mau = db.Column(db.String(128))
    Gia = db.Column(db.Float)
    SoLuong = db.Column(db.Integer)


class ChiTietHoaDons(db.Model):
    __tablename__ = 'ChiTietHoaDons'
    MaChiTietHoaDon = db.Column(db.Integer, primary_key=True)
    MaHoaDon = db.Column(db.Integer, db.ForeignKey('HoaDons.MaHoaDon'))
    MaChiTietSanPham = db.Column(db.Integer, db.ForeignKey('ChiTietSanPhams.MaChiTietSanPham'))
    SoLuong = db.Column(db.Integer)
    DonGia = db.Column(db.Float)


class HoaDons(db.Model):
    __tablename__ = 'HoaDons'
    MaHoaDon = db.Column(db.Integer, primary_key=True)
    MaKhachHang = db.Column(db.Integer, db.ForeignKey('KhachHangs.MaKhachHang'))
    DiaChiNhanHang = db.Column(db.String(128))
    HinhThucThanhToan = db.Column(db.String(128))
    NgayThanhToan = db.Column(db.Date) #khong chac lam co kieu db.Date ko nha, hoac la dung DateTime


class KhachHangs(db.Model):
    __tablename__ = 'KhachHangs'
    MaKhachHang = db.Column(db.Integer, primary_key=True)
    TenKhachHang = db.Column(db.String(128))
    SoDienThoai = db.Column(db.String(128))
    DiaChi = db.Column(db.String(128))