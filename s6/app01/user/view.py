from flask import Blueprint, render_template, request, url_for, redirect
import hashlib

from sqlalchemy import or_

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
        password = hashlib.sha1(password.encode('utf-8')).hexdigest()
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


@user_bp.route('/')
def index():
    return render_template('base.html')


@user_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sec_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        user_list = User.query.filter_by(username=username)
        print(user_list)
        for user in user_list:
            if user.password == sec_password:
                return '登陆成功'
        else:
            return render_template('user/login.html',msg="用户名或密码错误")
        # return render_template('user/login.html')
    else:
        return render_template('user/login.html')


@user_bp.route('/search/', methods=['GET', 'POST'])
def search():
    # users = User.query.all()
    # users = User.query.filter(User.username.contains('tt')).all()
    # users = User.query.filter(User.username.in_(['张大仙2', '张大仙3'])).all()
    # users = User.query.filter(or_(User.phone='23433',User.loginid='117970')).all()
    # users = User.query.order_by(-User.loginid).limit(3)  #限制数量
    # users = User.query.limit(3).offset(5).all()
    # users = User.query.offset(5).limit(3).all()
    # users = User.query.slice(2, 5).all()
    # users = User.query.all().slice(2, 5)
    # users = User.query.filter(User.username.contains('张大仙')).all()
    users = User.query.filter_by(username='张大仙').all()
    # users = User.query.get('11790')
    return render_template('user/search.html', users=users)

@user_bp.route('/search_name/', methods=['GET', 'POST'])
def search_name():
    keyword = request.args.get('search')
    userlist = User.query.filter(or_(User.username.contains(keyword), User.loginid.contains(keyword))).all()
    print(userlist)
    return render_template('user/center.html', users=userlist)
