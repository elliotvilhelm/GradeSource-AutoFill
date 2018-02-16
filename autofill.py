"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
File Name: autofill.py
Description: GradeSource Autofill.
Usage:
    python3 autofill.py -u <username> -p <password> -f <*.csv> -i <page_id>
Author: Elliot V Pourmand
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""


def get_CL_args(argv):
    args = {}  # initialize dict
    while argv: # arguments left
        if argv[0][0] == '-':  # Found a "-name value" pair.
            args[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return args


def login(user_str, password_str):

    browser.get(('https://www.gradesource.com/login.asp'))
    time.sleep(1)
    # fill in username and hit the next button
    username = browser.find_element_by_name('User')
    username.send_keys(user_str)
    time.sleep(1)
    password = browser.find_element_by_name('Password')
    password.send_keys(password_str)
    time.sleep(1);
    login_button = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr/td[1]/table/tbody/tr[12]/td[2]/input')
    login_button.click()
    time.sleep(1)


def load_csv(csv_fileName):
    PID = []
    scores = []
    with open(csv_fileName, newline='', encoding='utf-8-sig') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            PID.append(row[0])
            scores.append(row[1])
    return PID, scores


def fill_scores(pid, scores, page_id):
    # print("https://www.gradesource.com/editscores1.asp?id={}".format(page_id))
    browser.get("https://www.gradesource.com/editscores1.asp?id={}".format(page_id))
    missing = []
    rows_count = browser.execute_script("return document.getElementsByTagName('tr').length")
    # Table has 38 extra rows, this is a hard coded value, sorry fam );
    rows_count = rows_count-38
    # set([1, 2]).symmetric_difference(set([2, 3]))
    # Found pids
    # Get pids on page compare to pids on csv
    # Analogous to the missing list
    # missing: is what is on csv but not on GradeSource Webpage
    # found_pids: was on the GradeSouce but not csv
    found_pids = []
    for i in range(rows_count):   # go through table
        found_flag = False
        student = browser.find_element_by_id("student" + str(i))
        pid_page = browser.find_element_by_xpath("/html/body/center/center/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]\
        /form/table/tbody/tr[2]/td[2]/table/tbody/tr[{}]/td[2]".format(i+7))
        pid_page = pid_page.text.strip()

        for j in range(len(pid)):  # go through all names in csv
            if pid_page == pid[j]:
                found_pids.append(pid_page)
                student.send_keys(scores[j])
                found_flag = True
                break
        if not found_flag:
            missing.append(pid_page)

    pids_diff = pid
    pids_diff = list(set(pids_diff).symmetric_difference(found_pids))
    if len(pids_diff) is 0:
        print("All PID's on .csv found and filled.")
    print("\n\nPIDs that were on .csv but not found on GradeScope: ", pids_diff)
    print("\n\nPIDs that were on GradeScope but not found on .csv: ", missing)
    return missing


if __name__ == "__main__":
    from selenium import webdriver
    import os
    import csv
    from sys import argv
    import time
    import selenium.webdriver.chrome.options
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui import WebDriverWait
    #from selenium.webdriver.support import expected_conditions as EC
    #import time

    # Get Command line arguments
    args = get_CL_args(argv)

    # Load Sys Path to Current Directory
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Append chrome driver executable to path
    browser = webdriver.Chrome(dir_path + "/chromedriver")

    # PID's and Scores
    PID, Scores = load_csv(args['-f'])

    # Login
    login(args['-u'], args['-p'])

    # Fill the scores
    fill_scores(PID, Scores, args['-i'])




