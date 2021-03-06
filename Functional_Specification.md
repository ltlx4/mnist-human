# Functional Specification

## Current situation 
- we do not have an application 
- classification is done by the individual by accessing the database directly
- users have no way of evaluating themselves


## Desired system 
- it should be able to be reached and readly accesseable to everyone. 
- We need it to beable to be accessed at the same time by more than just one user at a time and we would like for it to not only be accessed in our office but anywhere.
- The webiste should show the set of rules on how the program will operate .
- We need it to be able to display an image and request the user to identify it.
- we want a web application
- it should be able to store a user input into a database 
- should be able to display an image to the user and request for user input
- we would like for it to collect the following user information:
  - region
  - language
  - age
  - degree
- the application should be able to recognize the user if he or she is a returning user
- there should be a feedback system
- the program will compare who guessed the correct answers better computer vs human
- After doing 5 tries the page will show the user his score against the computer 
- there will be a general comparison between all humans that have played including the mew user vs the computer


## Current processes/assets
- we currently have a database with images written in different fonts and images
- we do not have a way to test the classification of the input
- we do not have a platform or app to test this
- the user does not have a way of testing the classification of the image
 
## Required business processes
- Explaining how a website works to the user
- provide an image from the MNIST database
- this program should be accessable on the internet 
- it should be able to request information from the user and store it
- able to compare the user input to the image provided and accept if it was correct or not
- user can try multiples times and all the attempts should be stored 


## Rules for the program
- should only be able to get an integer value or sequence of integer values
- program should be functional on either mobile browser or computer
- should have an interface with user 
- allow user input

## List of requirements
- explain how it works
- Interactive interface
- output an image n
- accept user input and check against database 
- Evaluating solutions
- Feedback (later on)
- accessable as a web application

## Use Case 

![MNIST diagram use case.drawio.png](https://github.com/ltlx4/mnist-human/blob/deeb96106337935b4e910d5458721af9448b99c7/diagrams/MNIST%20diagram%20use%20case.drawio.png)

## Screen Design

![MNIST diagram use case.drawio.png](https://github.com/ltlx4/mnist-human/blob/78f495112efd9eec1d9d2747f403940396299acc/diagrams/2.jpeg)

![MNIST diagram use case.drawio.png](https://github.com/ltlx4/mnist-human/blob/78f495112efd9eec1d9d2747f403940396299acc/diagrams/1.jpeg)

![MNIST diagram use case.drawio.png](https://github.com/ltlx4/mnist-human/blob/78f495112efd9eec1d9d2747f403940396299acc/diagrams/3.jpeg)

![MNIST diagram use case.drawio.png](https://github.com/ltlx4/mnist-human/blob/78f495112efd9eec1d9d2747f403940396299acc/diagrams/4.jpeg)

## Scenarios
### 1.
    - new user visits our page
    - user accepts our cookies and information regarding visit is stored
    - user is asked to enter some information regarding him/herself
    - afterwards users proceeds to program
    - user is requested to enter a number against an image provided 
    - he/she has to do this 5 times
    - computer does the same
    - program compares given input to image
    - and compares the user input to the computer
    - user receives feedback
    - after a while, with other users, a comparison with other users is done
    - feedback is sent
    
### 2.
    - returning user opens the page
    - afterwards users proceeds to program
    - user is requested to enter a number against an image provided 
    - he/she has to do this 5 times
    - computer does the same
    - program compares given input to image
    - and compares the user input to the computer
    - user receives feedback
    - after a while, with other users, a comparison with other users is done
    - feedback is sent 
