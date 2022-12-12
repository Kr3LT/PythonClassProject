from app import app, db
from datetime import date
from app.models import HoaDons

def GetHoaDonByMaKhachHang(maKhachHang):
    return HoaDons.query.filter(HoaDons.MaKhachHang == maKhachHang).all()

def XacNhanHoaDon(maHoaDon):
    hoaDon = HoaDons.query.filter(HoaDons.MaHoaDon == maHoaDon).first()
    hoaDon.NgayThanhToan = date.today()
    # HoaDons.update().where(HoaDons.MaHoaDon == maHoaDon).values(NgayThanhToan = date.today())
    db.session.commit()
