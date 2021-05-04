# One-Minute Workout App

Application users are able to have short, scheduled exercise breaks while working on their laptops or desktops.

## Documentation

[specification.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/specification.md)

[working_hours.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/working_hours.md)

[architecture.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/architecture.md)

[user_faq.md](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_faq.md)

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
- DB credentials are saved in local .env file which is gitignored, so these db features are not in use yet (how to share the credentials?)

Logging in to the system:

- Basic UI for login (entering username and password)
- User validation from [csv file](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/src/users.csv)

Main window:

- Basic UI for main window
- Either Sign up or Log in, no further logic yet

## Features week 5

Setting the personal workout program:

- Basic UI for Timer
- Timer data save with user data
- Show saved timer data

Backend:

- User and Timer data save in [json file](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/src/users.json)

## Features week 6

- User logic improvements: Login/Signup --> Timer --> Exercise
- Exercise UI with 5 example exercises
- Random exercise starts with exercise button click and closes after 60 seconds


