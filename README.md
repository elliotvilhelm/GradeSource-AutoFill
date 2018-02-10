# Auto-Fill for GradeSource!

##### Usage

`python3 autofill.py -u username -p password -f hw4.csv -c 16`

The last argument column number is the column of the assignment in GradeSource, for homework 4 the number is 16. 
For homework 5 it would be 17.
Start from the first column and count to the right.
This parameter is necessary as the table does not have a unique identifier so to make the program generic I need you to 
enter the column number.

The .csv is expected to have PIDs in the first column and student scores in the second column.


##### Requirements
Must have selenium installed to your python3

If starting from scratch with OSX:

`brew install python3`

`pip3 install selenium`

The chrome driver I have included is for mac OSX. I have not tested this software on windows but it *should* work if you
replace the chromedriver executable. You can find the drivers [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

The program will enter scores for all students found on GradeSource and the .csv. If a student is found on GradeScource but not the .csv, 
the field will be left blank and the students PID will be returned at the end of the program.
