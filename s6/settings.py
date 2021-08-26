class BaseConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123.com@127.0.0.1:3306/s6'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
	DEBUG=True
	ENV='development01'


class Testing(BaseConfig):
	ENV = 'testing'
