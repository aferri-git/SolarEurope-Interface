# Command launchers 

TESTS = tests
	
Install:
	pip install – upgrade pip
	pip install -r requirements.txt
	
test:
	pytest