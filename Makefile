start:
	pipenv run flask run # runs flask app
db-migrate:
	pipenv run flask db migrate # creates the migration file
db-upgrade:
	pipenv run flask db upgrade # applies all migrations
install:
	pipenv install
