# SOEN343_GroupProject

# Prerequesites

- Linux Virtual Machine (Ubuntu 14.04+) or similar 
- Python 3.4.3+ 
- Pip3
- Node v7.10.1+

# Set Up

Please do this set up before cloning the project

### Install Virtual Environment

```
  pip3 install virtualenv
```

### Set Up Virtual Environment

```
  mkdir venv && cd venv && virtualenv -p python3 darthvendor && cd darthvendor
```

### Activate Virtual Environment

```
  source bin/activate
```

### Clone Repository

```
  git clone https://github.com/xTEddie/SOEN343_GroupProject.git // or git@github.com:xTEddie/SOEN343_GroupProject.git 
```

# Installation

#### Install Python Dependencies

```
  pip3 install -r backend/requirements/dev.txt 
```

#### Install Node Dependecies

```
  cd frontend && npm install
```

# Run Application

#### Run Backend

```
  cd backend && python3 manage.py runserver 0.0.0.0:8000 
```

The Django backend will be served as a REST service on http://localhost:8000/

#### Run Frontend

```
  cd frontend && npm run start 
```

You should be able to see the web application on http://localhost:3000/


