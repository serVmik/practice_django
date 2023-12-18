MANAGE := poetry run ./manage.py
TEST_JUST :=

start:
	@$(MANAGE) runserver

lint:
	poetry run flake8

test:
	poetry run coverage run --source='.' manage.py test

test-just:
	@$(MANAGE) test $(TEST_JUST)

shell:
	poetry run python manage.py shell_plus --notebook

shell-ipython:
	poetry run python manage.py shell_plus --ipython

dry:
	@$(MANAGE) makemigrations --dry-run

mmigrate:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate


.PHONY: static
static:
	@$(MANAGE) collectstatic
