from app import app
from app import db
from flask import Flask
from app.models import HoaDons, ChiTietHoaDons, ChiTietSanPhams, LoaiSanPhams, SanPhams, KhachHangs


@app.shell_context_processor
def pro_shell_context():
    return {'db': db, 'HoaDons': HoaDons, 'ChiTietHoaDons': ChiTietHoaDons, 'ChiTietSanPhams': ChiTietSanPhams,
            'LoaiSanPhams': LoaiSanPhams, 'SanPhams': SanPhams, 'KhachHangs': KhachHangs}
