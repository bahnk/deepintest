
# PYTHON PACKAGES
# black
# click
# pylint
# pytest
# sphinx
# sphinx-rtd-theme

.PHONY: .FORCE

all: .FORCE zip

zip: readme test clean
	cd ../ && zip -r MachineLearningSoftwareEngineer_nourdine_bah.zip deepintest

readme:
	pandoc --toc -o README.pdf README.md

clean:
	find deepintest -name "__pycache__" -type d -exec rm -rfv {} \; || true
	rm -rfv dist/
	rm -rfv deepintest.egg-info/
	rm -rfv docs/build/
	rm -f docs/make.bat
	rm -rfv .pytest_cache

build:
	python3 -m build

doc:
	cd docs && make html

test: pylint
	pytest --verbose

pylint: black
	pylint setup.py
	pylint --recursive y deepintest

black:
	black setup.py
	find ./ -name ".py" -exec black {} \;

