
import time
def getopts(argv):
    opts = {}  # initialize dict
    while argv: # arguments left
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


# 16 for hw4
def load_page(user_str, password_str, col_num):
    browser.get(('https://www.gradesource.com/login.asp'))

    time.sleep(3)
    # fill in username and hit the next button
    username = browser.find_element_by_name('User')
    username.send_keys(user_str)
    time.sleep(1)
    password = browser.find_element_by_name('Password')
    password.send_keys(password_str)
    login_button = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr/td[1]/table/tbody/tr[12]/td[2]/input')
    login_button.click()
    # time.sleep(1)
    time.sleep(1)
    scores_button = browser.find_element_by_xpath('/html/body/center/table[1]/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/a[4]/img')
    scores_button.click()

    time.sleep(1)
    assignment = "/ html / body / center / table[2] / tbody / tr[2] / td / table[1] / tbody / tr[2] / td[2] / table / tbody / tr[3] / \
      td[{}] / a".format(col_num)
    assignment_button = browser.find_element_by_xpath(assignment)
    assignment_button.click()



def load_csv(csv_fileName):
    PID = []
    scores = []
    with open(csv_fileName, newline='', encoding='utf-8-sig') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            PID.append(row[0])
            scores.append(row[1])
    return PID, scores


if __name__ == "__main__":
    from selenium import webdriver
    import os
    import csv
    from sys import argv

    # might use these later
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui import WebDriverWait
    #from selenium.webdriver.support import expected_conditions as EC
    #import time

    # USAGE
    # python3 fill.py -u elliot -p password! -f hw4.csv -c columnNumber (ie: 16)

    args = getopts(argv)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    browser = webdriver.Chrome(dir_path + "/chromedriver")
    PID, scores = load_csv(args['-f'])
    load_page(args['-u'], args['-p'], int(args['-c']))


    notFound = []
    rows_count = browser.execute_script("return document.getElementsByTagName('tr').length")
    # Table has 38 extra rows, this is a hard coded value, sorry fam );
    rows_count = rows_count-38

    for i in range(rows_count):   # go through table
        foundFlag = False
        student = browser.find_element_by_id("student" + str(i))
        PID_Page = browser.find_element_by_xpath("/html/body/center/center/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]\
        /form/table/tbody/tr[2]/td[2]/table/tbody/tr[{}]/td[2]".format(i+7))
        PID_Page = PID_Page.text.strip()
        for j in range(len(PID)):  # go through all names in csv
            if PID_Page == PID[j]:
                student.send_keys(scores[j])
                foundFlag = True
                break
        if not foundFlag:
            notFound.append(PID_Page)

    print("\n\nPIDs that were on GradeScope but not found on .csv: ", notFound)
