# Purpose of the system
- the purpose of this program is to establish a challenge to the user and test his or her ability to classify a given image
- it serves the purpose to provide a way of passing time and providing an entertaining as well as challenging task to the user
- the program should be able to run on a mobile device and or a computer and should not be limited to one. The website will be compatible with most browsers, this means operation and display.
- Only numbers can be entered in the answer fields during the running of the program. 
- After entering the number, you must submit the task, which will work using the button provided.
-  the user should receive a feedback on the actual number they were supposed to have entered .

# Project plan
members participating in  the project:
 - Ryan
 - Yasin
 - Tawfiq



# Business process model
* The Client asked our team to create a program able to be accessed on the internet.
* We will do the software with the developers for several weeks, with documentation, concluding the necessary contracts, and in the meantime we will continuously communicate with the customer periodically.
* If the software suits both the client and the developers, we will  initially start by getting a beta version then eventually publish it.


# Requirements List
## general requrements :
- The functions of the system can be used by any user.
- we would like the program to be operated on a Web page
- also available from computers and mobile devices 

## Surface requirements:

- The website should have a clean and transparent interface
- the user should be able to understand how it operates
- provide an image from the MNIST database


## Functional requirements:
- program displays an image
- Users can fill in the the given space with the number they think is correct or similar to the one on image
- Unless there needs to be a change, all rights to amend this program remain with us and not provided to client  (rights)

# Functional design
## System participants:
  - user
  - developers

## Access rights within the system:
### System Admin(developers) :
    - can access all parts of the program and make changes without any restrictions
    - with amends coming from the client, can change part of the program as requested by client

### User :
    - have no access rights
    - can only provide input information only

# Physical environment
- The program is designed to be accesed on any web platform.
- The website will run on any of the popular web browsers. (e.g. Chrome, Firefox, Opera, Microsoft Edge, Safari, Brave)

# Our developer software:
- Trello
- Github
- CodePen
- Visual studio code
- python
- draw.io
- Django

# Abstract domain model
## Basic operations: 
- comparison of the number entered by user to the one provided prom the MNIST database.
- keeps the number entered in the given space so that the user can see the correct number against his/hers

## User interface : 
- Less number of mouse clicks and keystrokes are required to accomplish this task.
- Icons and labels should be concise and cogent
- should be simple.



# Architectural plan
* the web application is going to be built using Django, a high-level Python web framework
* we will be hosting this app from github
* the app when ,open will operate as follows
* user accepts our cookies and information regarding visit is stored
* user is asked to enter some information regarding him/herself
* afterwards users proceeds to program
* user is requested to enter a number against an image provided 
* he/she has to do this 5 times
* computer does the same
* program compares given input to image
* and compares the user input to the computer
* user receives feedback


# Implementation plan
* we would want our web page to be hosted from a server
* administration changes and up keep will be done using django
* by assigning small task to each other we were able to bring out the dream system
* using trello, we will have the work flow for everyone set


# Testing plan
* we will conduct a series of tests until the required output is reached
* a table log to show what was done will be implimented
* we took the test using the known terms, testing the normal conditions, extreme and exceptional
* we noted down the required conditions we want to have
* when we had an error we fixed it so that the program ran smoothly
* we will have a log system to document every test and change done

# Install plan
we will put all the files on our server,and install the necessary enviorement, then our user can reach this program via our website

# Maintenance plan
* our goal is to have a program that will run soomthly
* unless required to be changed by the client, the program will have no updates or any changes
* in this ase of updates or changes, there will need to be a planning and a documation of the new requirements
