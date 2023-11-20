import re

pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'

phone = input('Введите номер телефона => ')
print('phone =', phone, type(phone))

phone = phone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')

if re.fullmatch(pattern, phone):
    print('Номер корректный')
else:
    print('Номер некорректный')
    exit()


phone_book = [phone, '8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430']
phone_book += ['8(495)430-23-97']
print('phone book =', phone_book, type(phone_book))

phone_book = [s.replace('-', '').replace('(', '').replace(')', '').replace(' ', '') for s in phone_book]
print('phone_book =', phone_book, type(phone_book))


for i in range(len(phone_book)):
    if len(phone_book[i]) == 7:
        phone_book[i] ='+7495' + phone_book[i]
    elif len(phone_book[i]) == 10:
        phone_book[i] = '+7' + phone_book[i]
    elif (phone_book[i][0] == '8') or (phone_book[i][0] == '7'):
        phone_book[i] = '+7' + phone_book[i][1:]


print('phone_book =', phone_book, type(phone_book))


for i in range(1, len(phone_book)):
    if phone_book[0] == phone_book[i]:
        print('YES')
    else:
        print('NO')