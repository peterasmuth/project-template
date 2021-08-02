import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()
login.login_view = 'auth.login'


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	bootstrap.init_app(app)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix = '/auth')

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	if app.config['LOG_TO_STDOUT']:
		stream_handler = logging.StreamHandler()
		stream_handler.setLevel(logging.INFO)
		app.logger.addHandler(stream_handler)
	else:
		if not os.path.exists('logs'):
			os.mkdir('logs')
		# CHANGE TO PROJECT NAME
		file_handler = RotatingFileHandler('logs/project_template.log',
										   maxBytes=10240, backupCount=10)
		file_handler.setFormatter(logging.Formatter(
			'%(asctime)s %(levelname)s: %(message)s '
			'[in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.INFO)
		app.logger.addHandler(file_handler)

	app.logger.setLevel(logging.INFO)
	# CHANGE TO PROJECT NAME
	app.logger.info('Project Template startup')

	return app

from app import models