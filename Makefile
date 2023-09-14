install:
	pip install -r requirements.txt

lint:
	pylint pals.py

test:
	python -m unittest discover

run:
	python your_script.py

