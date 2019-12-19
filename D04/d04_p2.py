from collections import Counter

input_file = open('D04/.input', 'r')

input_string = input_file.read()

input_file.close()

[pw_min, pw_max] = [int(n) for n in input_string.split('-')]

pw_range = range(pw_min, pw_max+1)

def validate_pw(n):
    n_str = str(n)
    return (2 in Counter(n_str).values()) and all(n_str[i-1] <= n_str[i] for i in range(1,len(n_str)))
    
n_valid = list(map(validate_pw, pw_range)).count(True)

print('Number of valid passwords:', n_valid)