# Auto-Fill for GradeSource!

##### Usage

`python3 -u username -p password -f hw4.csv -c 16`

The last argument column number is the column of the assignment in GradeSource, for homework 4 the number is 16. 
For homework 5 it would be 17.
Start from the first column and count to the right.
This parameter is necessary as the table does not have a unique identifier so to make the program generic I need you to 
enter the column number.


##### Requirements
Must have selenium installed to your python3

If starting from scratch with OSX:

`brew install python3`

`pip3 install selenium`

The chrome driver I have included is for mac OSX. I have not tested this software on windows but it *should* work if you
replace the chromedriver executable. You can find the drivers [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

The csv file is expected to be perfect, as of now the script does no verification meaning it does not check to see if the
name or PID of the student matches on gradescope. It is expecting the .csv to have the right number of students in the right
order. The csv should have two columns "email/PID" and "Score". Since email is not being verified all thats really needed
is the student scores in the second column **in the correct order**.


##### Coming soon
Verification of student PID/Email and student count.
