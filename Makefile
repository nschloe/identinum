VERSION=$(shell python3 -c "import identinum; print(identinum.__version__)")

default:
	@echo "\"make publish\"?"

upload: clean
	# Make sure we're on the master branch
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	rm -f dist/*
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	twine upload dist/*
	curl -H "Authorization: token `cat $(HOME)/.github-access-token`" -d '{"tag_name": "$(VERSION)"}' https://api.github.com/repos/nschloe/identinum/releases

tag:
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then exit 1; fi
	@echo "Tagging v$(VERSION)..."
	git tag v$(VERSION)
	git push --tags

publish: tag upload

clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	@rm -rf *.egg-info/ build/ dist/ MANIFEST .pytest_cache/ .cache/

format:
	isort .
	black .
	blacken-docs README.md

lint:
	black --check .
	flake8 .
