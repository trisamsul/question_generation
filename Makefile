setup:
	if [ -d "venv" ]; then echo "VENV exists"; else echo "VENV not exists"; python -m venv venv; fi
	. venv/bin/activate; pip install --upgrade pip; pip install -Ur requirements.txt
	python -m nltk.downloader punkt

run:
	. venv/bin/activate
	FLASK_APP=index FLASK_ENV=development flask run

