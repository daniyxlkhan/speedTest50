# Speedtest50

# CS50X
# **Speedtest50, a network speedtest**
Video Demo: 

# **Description**:
This was created specifically as a final project for [CS50’s Introduction to Computer Science](https://cs50.harvard.edu/x/2022/). 

This project consists is a speedtest that uses libraries like speedtest, flask, cs50, flask session. 
<br></br>

## **A practical use**

With this final project, you can easily measure your network speed, keeping track of your network's performance over time. By simply logging in, you gain access to a valuable tool that allows you to monitor and compare your network's speed, ensuring you always stay connected at optimal speeds.
<br></br>

## **That was the gist of the app. Now onto the specifics and technicalities.**

Starting with the what was needed for this bot:

    - speedtest-cli library 
    - werkzeug.security library for hashing
    - Flask framework to work with python


Now, onto the code.

## **The gist of the web app**

    -Test- Get your network speed
    -Register - Register a new account to keep track of your network speeds
    -Login - Login to your account
    


This Speedtest works as follows:

You can get your network speed on the click of a button.

- Uses the speedtest-cli to get the optimal server.

- Gets the download speed, upload speed, ping and sponsor. (Converts speed from bps to Mbps)
  
- Saves the results for history if user is logged in

Using decorators for routes.

```

<br>
Now, the speedtest is complete and all that is needed is the option to deploy it. I chose to deploy it and make it useful to the public. 
<br></br>

I learned a lot in the process of working with this web application, specifically:
    
- Deepened my knowledge of python
- Learned how to work with various libraries 
- Learned how to create and manage a project through GitHub Desktop
- Learned SQL
- Learned how to handle a database


And with this, I got to thank all of CS50's staff for their amazing course, which was an amazing introduction that helped me progress and fundamentally, it taught me to teach myself how to code.
