from app.models import ChiTietHoaDons

def GetByMaHoaDon(maHoaDon):
    return ChiTietHoaDons.query.filter(ChiTietHoaDons.MaHoaDon == maHoaDon).all()