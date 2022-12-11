import os
from app import app,db
from flask import redirect, render_template,flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask import request, jsonify,send_from_directory
from werkzeug.urls import url_parse 
from werkzeug.utils import secure_filename
from app.models import SanPhams,LoaiSanPhams

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS'] 

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename) 


@app.route('/product', methods = ['POST'])
@login_required
def createProduct():
    ProductJson = request.get_json()
    ProductThumbnail = request.file['thumbnail']
    if ProductThumbnail.filename == '':
        flash('No Thumbnail uploaded')
    if ProductThumbnail and allowed_file(ProductThumbnail.filename):
        filename = secure_filename(ProductThumbnail.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        ProductThumbnail.save(path)
    newSanpham = SanPhams(MaSanPham=ProductJson['MaSanPham'],TenSanPham=ProductJson['TenSanPham']
                          ,Thumbnail = filename, MaLoaiSanPham = ProductJson['MaLoaiSanPham'])
    db.session.add(newSanpham)
    db.session.commit()    
    return "Create Product Success", 201

@app.route('/product', methods=["GET"])
def getAllProduct():
    ProductList = SanPhams.query.all()
    return jsonify(ProductList)
    
@app.route('/product/<int:product_id>/', methods = ['GET'])
def getProductByProductId(product_id):    
    Product = SanPhams.query.filter_by(MaSanPham = product_id).first_or_404()
    return jsonify(Product)
    
@app.route('/product/<int:product_id>', methods = ['POST'])
@login_required
def updateProductByProductId(product_id):
    Product = SanPhams.query.filter_by(MaSanPham = product_id).first_or_404()
    ProductJson = request.get_json()
    Action = ProductJson['action']
    if Action == "Update":
        ProductThumbnail = request.file['thumbnail']
        if ProductThumbnail.filename == '':
            flash('No Thumbnail uploaded')
        if ProductThumbnail and allowed_file(ProductThumbnail.filename):
            filename = secure_filename(ProductThumbnail.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            ProductThumbnail.save(path)
        Product.TenSanPham = ProductJson['TenSanPham']
        Product.Thumbnail = ProductThumbnail.filename
        Product.MaLoaiSanPham = ProductJson['MaLoaiSanPham']
        db.session.commit()
        return "Update product Success", 200
    elif Action == "Delete":
        db.session.delete(Product)
        db.session.commit()
        return "Delete product Success",200
    return "No action specified",400
    
