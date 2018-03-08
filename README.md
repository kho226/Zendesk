# Zendesk Ticket Viewer CLI

## Features
> search for single ticket

> view paginated tickets

## To-do
- [x] Model
- [x] View
- [x] Controller
- [x] Tests 
- [ ]  OAuth Token Access
- [ ]  More Robust Error Handling
- [ ]  More Tests
- [ ]  Circular Pagination

## Installation (macOS Sierra Version 10.12.1)
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
git clone https://github.com/kho226/Zendesk
cd <project_path>
virtualenv --python=/usr/bin/python3.5.2 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Start process
```
cd <project_path>
cd Controller
python appController.py
```
## Tests

```
cd <project_path>
cd Tests
python unitTests.py
```

## References
> https://developer.zendesk.com/rest_api/docs/core/tickets#content

## Requirements
> python==3.5.2

> certifi==2018.1.18

> chardet==3.0.4

> funcsigs==1.0.2

> get==0.0.39

> idna==2.6

> mock==2.0.0

> patch==1.16

> pbr==3.1.1

> post==0.0.26

> public==0.0.65

> query-string==0.0.28

> request==0.0.26

> requests==2.18.4

> six==1.11.0

> urllib3==1.22