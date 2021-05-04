# Architecture

## Structure

### Packages
WIP

## User Interface and Features

### User Sign Up

New user chooses signing up by clicking Sign up button in the main window. User enters username and password to the fields and application validates if username is already in use. If not, new user is created and saved in users.json file and timer set appears in the main window.

![signup image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_signup.png)

### User Log In

Existing user chooses logging in by clicking Log in button in the main window. User enters username and password to the fields and application validates if username exists in the users.json file. If yes, the application validates if the password matches username data in the users.json file. If yes, the timer set appears in the main window.

![login image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_login.png)

### Timer set
WIP

### Exercise
WIP

## Data Save

User, timer and exercise data is saved locally. User and time data use json file format and exercise data is stored in a folder.

### Files and Folders

- users.json file includes user and timer data: username (String), password (String), timer_start (String), timer_stop (String), timer_interval (String)
- Exercise texts and images are stored as .txt and .png files in exercises folder. Each file name contains a number, which is common for the text and image of the same exercise. For example, 1.png and 1.txt are rendered to exercise 1.







