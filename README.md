# Speedtest50 - Network Speed Test

[Video Demo](https://youtu.be/pCiRFMbQ8D8)

## Description
Speedtest50 is a network speed measurement tool created as the final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). It harnesses the power of various libraries, including speedtest, flask, cs50, and flask session.

### Practical Use
Speedtest50 allows you to effortlessly measure your network speed and monitor your network's performance over time. By logging in, you unlock the ability to track and compare your network's speed, ensuring you always stay connected at optimal speeds.

## Technical Details
To bring this web app to life, I relied on essential components:

- **speedtest-cli library**: For network speed testing.
- **werkzeug.security library**: To handle password hashing securely.
- **Flask framework**: To create a robust Python web application.

## Core Features
Speedtest50 offers three main functionalities:

- **Test**: Get your network speed with a single click.
- **Register**: Create a new account to save your speed test history.
- **Login**: Access your account to view your historical network speeds.

### How It Works
Here's a breakdown of how Speedtest50 operates:

- It utilizes the speedtest-cli library to identify the most suitable server for your speed test.
- The application gathers key metrics, including download speed, upload speed, ping latency, and sponsor information. Speeds are converted from bits per second (bps) to megabits per second (Mbps) for better comprehension.
- When users are logged in, their results are stored in the database for future reference.

### Project Structure
Speedtest50's project structure comprises the following components:

- **static**: This directory contains images and CSS files used for styling and enhancing the user interface.

- **templates**: Here, you'll find HTML files that define the structure and layout of the web pages, dynamically rendering your network speed test results.

- **app.py**: The heart of the application, where routing, data retrieval, and result presentation are managed. Decorators for routes ensure smooth navigation.

- **db.txt**: Contains SQL queries responsible for establishing the database structure to store historical speed test results.

- **helper.py**: This file hosts essential functions used across app.py to optimize various tasks.

- **requirements.txt**: A list of Python libraries and dependencies needed for your project. Generate it with the `pip freeze > requirements.txt` command.

- **speedtest.db**: An SQLite database that stores historical speed test results for registered users.


## Learning Journey
During this project, I acquired valuable skills:

- Deepened my Python knowledge.
- Learned to work with diverse libraries.
- Mastered GitHub Desktop for project management.
- Gained proficiency in SQL.
- Developed database management skills.

My journey with CS50's Introduction to Computer Science has been transformative, teaching me not only coding but also the ability to self-learn a fundamental skill in the world of programming.
