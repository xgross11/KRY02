#________________________ ISA Project - makefile _____________________
#_________________ File transfer via covert channel __________________
#______________________ Author: žaneta Grossová ______________________
#______________________________ xgross11 _____________________________
#_____________________ last update: 15.11.2021 _______________________

# Define variables for commands
PYTHON = python3
PIP = $(PYTHON) -m pip
VENV = $(PYTHON) -m venv
ACTIVATE = . venv/bin/activate &&


.PHONY: build
build: 
	$(VENV) venv
	$(ACTIVATE) $(PIP) install -r requirements.txt

.PHONY: run
run:
	$(ACTIVATE) $(PYTHON) kry.py $(PORT) $(TYPE) 

