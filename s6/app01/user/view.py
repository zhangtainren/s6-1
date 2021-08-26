from flask import Blueprint, render_template, request, url_for, redirect
import hashlib

from app01 import db
from app01.user.model import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['get','post'])
def register():
    if request.method == 'POST':
        loginid = request.form.get('loginid')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        password = hashlib.sha1(password.encode('utf-8'))
        user = User()
        user.username = username
        user.loginid = loginid
        user.password = password
        user.phone = phone
        db.session.add(user)
        db.session.commit()

        return  redirect(url_for('user.user_center'))
    else:
        return render_template('user/register.html')

    return render_template('base.html')


@user_bp.route('/usercenter/')
def user_center():
    print("ok")
    users = User.query.all()
    return render_template('user/center.html',users=users)

