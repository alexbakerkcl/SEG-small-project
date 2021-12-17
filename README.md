# Team Hedgehog Small Group project

## Team members
The members of the team are:
- Alexander Baker
- Chenhui Wang
- Dylan Barker
- Joshua Bebbington
- Zilin Chen

Absent team members:
- Chenhui Wang
- Joshua Bebbington

## Project structure
The project is called `system`.  It currently consists of a single app `clubs`.

## Deployed version of the application
The deployed version of the application can be found at [URL](https://safe-hollows-70921.herokuapp.com/).

## Installation instructions
To install the software and use it in your local development environment, you must first set up and activate a local development environment.  From the root of the project:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install all required packages:

```
$ pip3 install -r requirements.txt
```

Migrate the database:

```
$ python3 manage.py migrate
```

Seed the development database with:

```
$ python3 manage.py seed
```

Run all tests with:
```
$ python3 manage.py test
```

## Sources
The packages used by this application are specified in `requirements.txt`
