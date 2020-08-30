fmt:
	poetry run isort .
	poetry run black .

jaeger:
	docker run -d -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one
	open http://localhost:16686

jaegerkill:
	docker rm $(shell docker stop $(shell docker ps -a -q  --filter ancestor=jaegertracing/all-in-one))

setup:
	asdf install
	poetry install

test:
	python -m unittest

example:
	poetry run uvicorn examples.fastapi_server.server:app --reload

request:
	curl http://localhost:8000/predict