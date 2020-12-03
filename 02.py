import operator

FILE = "02.txt"

with open(FILE, 'r') as f:
    lines = f.read().split('\n')

# first part
count_valid_passwords = 0
for l in lines:
    tmp = l.split(' ')
    min_occurence, max_occurence = tmp[0].split('-')
    search_letter = tmp[1].replace(':', '')
    password = tmp[2]
    count_valid_passwords += int(min_occurence) <= password.count(
        search_letter) <= int(max_occurence)

print('valid passwords in first part: ' + str(count_valid_passwords))

# second part
count_valid_passwords = 0
for l in lines:
    tmp = l.split(' ')
    first_char, second_char = tmp[0].split('-')
    search_letter = tmp[1].replace(':', '')
    password = tmp[2]
    count_valid_passwords += operator.xor(password[int(first_char)-1] == search_letter,
                                          password[int(second_char)-1] == search_letter)

print('valid passwords in second part: ' + str(count_valid_passwords))
