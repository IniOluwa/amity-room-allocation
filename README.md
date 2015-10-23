# Checkpoint-1
Design of an automatic allocation of people to their respective places.

##Allocation
The allocation program creates rooms and offices and automatically allocates people into them.
Every room has a maximum of 4 people assigned to it.
Every office has a maximum of 6 people assigned to it.

## Walkthough
Every person to be allocated is read from a txt file and a new instance , ```STAFF``` or ```FELLOW``` is created based on the who the ```Person``` is.
Every space is read from a txt file and a new space instance object is created based on the type of ```Space``` it is, ```OfficeSpace``` or ```LivingSpace```
People are allocated to spaces based on the occupant_type of the space, ```STAFF``` or ```FELLOW```, ```MALE``` or ```FEMALE```

*SAMPLE OUTPUT*

HACKSAW - OFFICE
[MATTHEW O’CONNOR, PROSPER OTEMUYIWA, AKONAM IKPELUE, SAYO ALAGBE, HELEN EBOAGWU, GODSON UKPERE]

MAPLE - MALE ROOM
[IFEDAPO OLAREWAJU, UGWU FRANKLIN, ADEBAYO ADEPOJU, AYOOLA SOLOMON]

IROKO - FEMALE ROOM
[LAIDE AGBOOLA, MIRABEL EKWENUGO, BLESSING ORAZULUME, KOSY ANYANWU]


## How to run program
1. Navigate to the Checkpoint-1 directory
2. Run ```python output.py```

## How to run tests
1. Navigate to the Checkpoint-1 directory
2. Run ```python -m unittest tests.tests```

## How to run coverage tests and view coverage report
1. Install a virtual environment using ```pip install Virtualenv <environment-name>```
2. Activate it and ```pip install coverage```
3. Run ```coverage run -m tests.tests```
2. Run ```coverage html``` to view html report.

