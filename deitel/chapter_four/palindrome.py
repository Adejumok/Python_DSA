def check_pal(number):
    while len(number) != 5:
        print('This is not a five digit integer')
        number = input('Enter a five digit integer: ')

    if number == number[::-1]:
        return print('This is a palindrome')

    return print('This is not a palindrome')


number= input('Enter a five digit integer: ')
print(check_pal(number))
