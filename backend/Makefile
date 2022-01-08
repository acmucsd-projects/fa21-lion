start-mongo-db:
	brew services restart mongodb-community

stop-mongo-db:
	brew services stop mongodb-community

run-server: 
	python3 run.py

run-app: start-mongo-db run-server