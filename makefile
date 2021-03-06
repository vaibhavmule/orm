init:
	cp .env-example .env
	pip install -r requirements.txt
	# Create MySQL Database
	# Create Postgres Database
test:
	python -m pytest tests
ci:
	make test
lint:
	python -m flake8 src/masonite/ --ignore=E501,F401,E203,E128,E402,E731,F821,E712,W503
format:
	black src/masonite
	black tests/
	make lint
coverage:
	python -m pytest --cov-report term --cov-report xml --cov=masonite tests/
	python -m coveralls
publish:
	make format
	python setup.py sdist
	twine upload dist/*
	rm -fr build dist .egg masonite.egg-info
	rm -rf dist/*
pypirc:
	cp .pypirc ~/.pypirc