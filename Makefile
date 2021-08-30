init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python main.py

clean:
	rm -rf __pycache__

.PHONY: init test run clean
