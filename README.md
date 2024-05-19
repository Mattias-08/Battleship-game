
# Three in a row

![Responsive Mockup]

*The link to [Three in a row](https://three-in-a-row-21c4d9510ed4.herokuapp.com/)*

Three in a row is a python terminal project that is made give the user 
a fun game to kill time. The rules are simple and the game is fast passed. 

---

# How to play:

-Click this *[link](https://three-in-a-row-21c4d9510ed4.herokuapp.com/)* or copy this text: `https://three-in-a-row-21c4d9510ed4.herokuapp.com/` and paste it in your browser's address bar.
- The page loads as soon as you start the program.
- The rules are displayed and you can start inputing your commands according
to the limitations.
-Keep placing your pieces on the board untill a winner is declared.


---

# Features

- **Loading the page**

  The terminal gets loaded and the game is displayed with rules and board, waiting for the users input

  ![loading Program](documentation/Start_game.png)

  - **Playing the game**

  The user gives the input and the board gets updated 
  
  After that the computers move gets displayed by updating the board, and the request for user input gets repeated

  ![loading Program](documentation/Playing.png)
  

- **End of the game**

  When all the boards are filled or a player gets three in a row the winner gets declared.

  Then the user gets prompted to input y or n depending on if he wants to play another game or not.

  Depending on the answer the game restarts if y, if the input message is n then a thank you message is displayed and

  the program ends.

  ![loading Program](documentation/Game_end.png)
  ![loading Program](documentation/End_terminal.png)
  

  - **Error handling**

  There is some errorhandling for incorrect inputs. Examples of this will be displayed below

  ![loading Program](documentation/Invalid_input.png)



---

# Flowchart

The flowchart represents the logic of the application:

  ![Flash Card Page](documentation/image_flowchart_three_in_row.png)

---

## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.


##### Third-party imports:

#### Other tools:

- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [GIMP](https://www.gimp.org/) was used to make and resize images for the README file.


---


## Bugs

All the bugs are resolved and the program runs well

## Testing

## Compatibility

In order to confirm the correct functionality, responsiveness, and appearance:

+ The website was tested on the following browsers: Chrome, Firefox, Brave.

No issues was found after the manual testing.

## Manual testing

Manual testing have been done on all the features personally and by a friend to make that there are no interactice bugs.

The testing has also been done on a tablet and phone to ensure that the website works and looks like it should on all normal screensizes.

---
## Validator testing

[online validation tool](http://pep8online.com/) was used to ensure didnt have any issues related to the styling or syntax.

The testing was done manually by coping in the code ![Python Validator](documentation/python%20linter.png)

---
## Deployment
- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://three-in-a-row-21c4d9510ed4.herokuapp.com/)

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. Python is required to be installed on your local PC on order to run this program:
  - `sudo apt install python3`

  1. Pip installed is also requirede to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/Mattias-08/three-in-a-row).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/Mattias-08/three-in-a-row`

- Alternatively, Gitpod can be used by click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/Mattias-08/three-in-a-row)

   
---
## Credits

- Color formatting: [Colorama](https://pypi.org/project/colorama/).

---
## Acknowledgements

[Juliia Konn](https://github.com/IuliiaKonovalova)

I am extremely thankful to my mentor Juliia Konn for her advice and support.
