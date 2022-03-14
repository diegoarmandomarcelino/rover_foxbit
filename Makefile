lint:
	flake8

format:
	yapf -i -r -p .

run_tests:
	coverage run -m pytest
	coverage report
