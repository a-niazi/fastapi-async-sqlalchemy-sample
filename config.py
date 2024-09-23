import os


class Config:
	DEBUG = False
	CSRF_ENABLED = True

	APP_VERSION = "1.0"
	APP_NAME = 'appic'
	APP_TITLE = 'appic'

	BASE_URI = os.getenv('BASE_URI', 'https://api.appic.sy')

	SERVICE_URI = os.getenv('API_SERVICE_URI', f'{BASE_URI}:8000')

	POSTGRESQL = {
		'user': os.getenv('POSTGRESQL_USER', 'kong'),
		'pw': os.getenv('POSTGRESQL_PASSWORD', 'kong'),
		'host': os.getenv('POSTGRESQL_HOST', 'insta.tagminer.ir'), # docker image name
		'port': os.getenv('POSTGRESQL_PORT', 5432),
		'db': os.getenv('POSTGRESQL_DATABASE', 'notedb'),
		'max_overflow': os.getenv('MAX_OVERFLOW', 20),
		'pool_size': os.getenv('POOL_SIZE', 10)
	}
	DB_URI = 'postgresql+asyncpg://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRESQL

	LOG_FILE_NAME = APP_NAME + '.log'

	@property
	def url_prefix(self):
		return '/' + self.APP_NAME

	@property
	def testing(self):
		return isinstance(self, TestConfig)

	@property
	def deployed(self):
		return isinstance(self, ProductionConfig)

	@property
	def profile(self):
		return self.__class__.__name__.upper().replace('CONFIG', '')


class DevelopmentConfig(Config):
	"""Configurations for Development."""
	DEBUG = True


class TestConfig(Config):
	"""Configurations for Testing."""
	DEBUG = True


class ProductionConfig(Config):
	"""Configurations for Production."""
	DEBUG = False


config = Config()
profile = os.getenv('ENVIRONMENT') or 'DEVELOPMENT'
if profile == 'DEVELOPMENT':
	config = DevelopmentConfig()
elif profile == 'TEST':
	config = TestConfig()
elif profile == 'PRODUCTION':
	config = ProductionConfig()
