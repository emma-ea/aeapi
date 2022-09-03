import dj_database_url
# heroku: update database configuration from $DATABASE_URL
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
