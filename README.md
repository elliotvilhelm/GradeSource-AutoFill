# Auto-Fill for GradeSource!

##### Usage

`python3 autofill.py -u username -p password -f hw4.csv -i 589789`

The last "-i" parameter is the id of the from the url of the score page
you want to update, for example given:

"https://www.gradesource.com/editscores1.asp?id=589789"
The id you would use is "589789"

The .csv is expected to have PIDs in the first column and student scores in the second column.
For example:

>A99884200, 9.2

>A19338822, 3.5


##### Requirements
Must have selenium installed to your python3

If starting from scratch with OSX:

`brew install python3`

`pip3 install selenium`


The chrome driver I have included is for mac OSX. I have not tested this software on windows but it *should* work if you
replace the chromedriver executable. You can find the drivers [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

The program will enter scores for all students found on GradeSource and the .csv. If a student is found on GradeScource but not the .csv, 
the field will be left blank and the students PID will be returned at the end of the program.
