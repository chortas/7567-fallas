# -- Run scripts
.PHONY: install
install:
	python3 -m pip install --no-cache-dir -r app/requirements.txt
	(cd front && npm install)

.PHONY: app
app:
	python3 app/main.py

.PHONY: front
front:
	(cd front && npm start)
