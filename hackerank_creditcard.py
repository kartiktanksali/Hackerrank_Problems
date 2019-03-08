import re

string="4253 6258 7961 5786"
string1="5122-2368-7954-3214"

pattern = re.compile(r"[4,5,6]\d{3}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}")

#pattern = re.compile(r"4253625879615786")


if pattern.match(string1) == None:
    print("False")
else:
    print("True")