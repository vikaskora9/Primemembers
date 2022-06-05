ip = input('Enter Sentence :- ')  # takes input from command line
tmp, ans = '', ''  # tmp for storing string temporarily, ans for storing result
for i in ip:
    if 97 <= ord(i) <= 122:  # as ascii of small letters ranges from 97 to 122
        tmp += i
    elif i == ' ':
        if len(tmp) > len(ans):
            ans = tmp
        tmp = ''
print(ans)
