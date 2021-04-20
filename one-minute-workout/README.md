# One-Minute Workout App

Application users are able to have short, scheduled exercise breaks while working on their laptops or desktops.

## Documentation

[specification.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/specification.md)

[working_hours.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/working_hours.md)

## Installation

Install dependencies: poetry install

Start application: poetry run invoke start

Run tests: poetry run invoke test

Test coverage report: poetry run invoke coverage-report

Pylint: poetry run invoke lint

## Features week 3

Registering to the system:

- Basic UI for signup (entering username and password)
- Creating new user
- Saving new user to [csv file](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/src/users.csv)

## Features week 4

Backend:

- PostgreSQL database in AWS RDS
- Database class and tests
- DB methods in User class
- Credentials saved in .env file which is gitignored, so this feature is not in use yet

