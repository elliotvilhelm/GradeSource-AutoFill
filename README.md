# Auto-Fill for GradeSource!

#### Usage

`python3 autofill.py -u <username> -p <password> -f hw4.csv -i 589789 --pid-column 0 --score-column 1`

The last "-i" parameter is the id of the from the url of the score page
you want to update, for example given:
"https://www.gradesource.com/editscores1.asp?id=589789"
The id you would use is "589789"

The default value for PID column and student score is 0 and 1 respectively. Meaning the expected .csv format is:

> "A1235523", 8

> "A1231231", 10

##### Autograder Example

The following example is for those of you using .csv files from autograder.ucsd.edu

`python3 autofill.py -u elliot -p xxx -f Homework-3.csv -i 602223 --pid-column 1 --score-column 4`

> "email", "pid", "firstName", "lastName", "score", "daysEarly"

> "elliot@ucsd.edu", "A1235523", "Pourmand", "Elliot", 10, 0

#### Output

The program will return student PID's who were
1. Found on the .csv but not found on GradeSource
2. Found on GradeSource but not found on the .csv


#### Requirements
Must have selenium installed to your python3

If starting from scratch with OSX:

`brew install python3`

`pip3 install selenium`


#### User Notes
- The chrome driver I have included is for mac OSX. I have not tested this software on windows but it *should* work if you
replace the chromedriver executable. You can find the drivers [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

- Please note the program will not press the "submit" button, you must press it once the fields have been filled.

- The script is case sensitive in finding the PID's to match.  Make sure the student PID casing in the input CSV file matches Gradesource PID casing.

- On MacOS or Linux systems, make sure the Chrome driver has executable permission set.
