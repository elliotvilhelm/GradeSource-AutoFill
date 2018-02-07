

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


# 16 for hw4
def load_page(user, password, col_num):

    usernameStr = user
    passwordStr = password
    browser.get(('https://www.gradesource.com/login.asp'))

    # fill in username and hit the next button
    username = browser.find_element_by_name('User')
    username.send_keys(usernameStr)

    password = browser.find_element_by_name('Password')
    password.send_keys(passwordStr)
    login_button = browser.find_element_by_xpath('/html/body/center/form/table/tbody/tr/td[1]/table/tbody/tr[12]/td[2]/input')
    login_button.click()

    # time.sleep(1)
    scores_button = browser.find_element_by_xpath('/html/body/center/table[1]/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/a[4]/img')
    scores_button.click()

    assignment = "/ html / body / center / table[2] / tbody / tr[2] / td / table[1] / tbody / tr[2] / td[2] / table / tbody / tr[3] / \
      td[{}] / a".format(col_num)
    assignment_button = browser.find_element_by_xpath(assignment)
    assignment_button.click()



def load_csv(csv_fileName):
    email = []
    scores = []
    with open(csv_fileName, newline='', encoding='utf-8-sig') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            email.append(row[0])
            scores.append(row[1])

    # print(email)
    # print(scores)
    return email, scores


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
    email, scores = load_csv(args['-f'])
    load_page(args['-u'], args['-p'], int(args['-c']))
    for i in range(len(scores)):
        student = browser.find_element_by_id("student" + str(i))
        print("Email:  ", email[i], "   Score: ", scores[i])
        student.send_keys(scores[i])


