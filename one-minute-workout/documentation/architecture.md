# Architecture

## Structure and application

###  Packages and classes

Application class initializes the users.json file in the db package and starts UI Main class in the main window.

ui package contains all the user interface classes.

UI Main class depends on classes UI Signup and UI Login. Both of these classes depend on UI Timer class and use User class to save or check user info in the users.json file.

UI Timer class uses User, Timer and Counter classes to save timer values with user data and start the exercise loop. UI Timer class depends on UI Exercise class, which uses Exercise class to load and render the exercises from the exercises package.

![architecture image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/application_architectrue_2.png)


## User Interface and Features

### User Sign Up

New user chooses signing up by clicking Sign up button in the main window. User enters username and password to the fields and application validates if username is already in use. If not, new user is created and saved in users.json file and timer set view opens in the main window.

![signup image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_signup_2.png)

### User Log In

Existing user chooses logging in by clicking Log in button in the main window. User enters username and password to the fields and application validates if username exists in the users.json file. If yes, the application validates if the password matches username data in the users.json file. If yes, the timer set view opens in the main window.

![login image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_login.png)

### Timer set

After signup / login the timer set view opens to the main window. If user has set timer values before, the values are shown in the UI. User enters timer values, ending hours, minutes and exercise interval in the separate fields and clicks Apply timer button. Application validates if the entries are correct and if so, saves the values with the user data in the users.json file. Timer values are also updated in the UI.

![timer set image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_timer_set.png)

### Workout schedule start

When timer values are set, user clicks the Start exercise button. Application counts the amount of exercise loops based on current time and user's end time and interval values. The first random exercise runs immediately in a new window. After 60 seconds the exercise window closes. The loop runs with random exercises after user's defined interval and ends before user's defined end time. Main window remains open until the user terminates it.

![exercise start image](https://github.com/KooEeVee/ot_harjoitustyo/blob/main/one-minute-workout/documentation/user_timer_exercise_start.png)

## Data Save

User, timer and exercise data is saved locally. User and timer data use json file format and exercise data is stored in a folder.

### Files and Folders

- users.json file includes user and timer data: username (String), password (String), timer_stop (String), timer_interval (String).
- Exercise texts and images are stored as .txt and .jpg files in exercises folder. Each file name contains a number, which is common for the text and image of the same exercise. For example, 1.jpg and 1.txt are rendered to exercise 1.







