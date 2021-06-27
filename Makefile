.PHONY: requirements

PROJECT_NAME=pyauto-aimbooster

create_environment:
	conda create --yes --name $(PROJECT_NAME)

requirements:
	pip install -r requirements.txt
	python -m ipykernel install --user
	python -m ipykernel install --user --name $(PROJECT_NAME) --display-name "$(PROJECT_NAME)"
