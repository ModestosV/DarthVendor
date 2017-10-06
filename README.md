# SOEN343_GroupProject

# Prerequisites

- Linux Virtual Machine (Ubuntu 14.04+) or similar 
- Python 3.4.3+ 
- Pip3
- Node v7.10.1

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
  python3 manage.py runserver 0.0.0.0:8000 
```

The Django backend will be served as a REST service on http://localhost:8000/

#### Run Frontend

```
  cd frontend && npm run start 
```

You should be able to see the web application on http://localhost:3000/

# Database

#### Dump Database

```
  python3 scripts/dump_database.py
```

#### Set Up Database

```
  ./scripts/populate_db.sh
```

#### Connect To Database

```
  sqlite3 backend/db.sqlite3
```

# Deploy Application

#### Collect Static Files

```
  python3 manage.py collectstatic --no-input
```

#### Compile Javascript modules for Frontend

```
  cd frontend && npm run build 
```

The REST API URL is located at http://api.darthvendor.me/

The web application is located at http://darthvendor.me/ 


# Continuous Integration

#### Jenkins

A Jenkins instance exists to pull new changes, build the application and restart the apache server on every commit.

The Jenkins instance is located at http://165.227.44.65:8080/ or http://jenkins.darthvendor.me/


# Contribution

- **Dev** branch **MUST** be a working branch
- **NEVER** push directly to **dev** branch
- Any new feature should be branched out from **dev** and be named as follow: [username]/[feature]
- **ALWAYS** make sure that your branch has the latest changes from **dev**
- **ALWAYS** make a pull request to **dev** and assign **ONE** person at minimum to review the new **feature** 
- **NEVER** merge your own pull request


# References

- https://python.swaroopch.com/
- https://docs.djangoproject.com/en/1.11/
- http://www.django-rest-framework.org/
- http://drfdocs.com/
- https://facebook.github.io/react/
- http://redux.js.org/docs/introduction/
- https://www.youtube.com/watch?v=DiLVAXlVYR0&list=PL6gx4Cwl9DGBbSLZjvleMwldX8jGgXV6a
- https://egghead.io/courses/getting-started-with-redux
- https://github.com/creationix/nvm
