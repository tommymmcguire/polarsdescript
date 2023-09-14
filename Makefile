install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

summary:
	python main.py
		
all: install lint format test