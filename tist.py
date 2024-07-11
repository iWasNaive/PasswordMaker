import argparse
import string
from random import choices

def password_creator(length=8, upper=False, lower=False, digit=False, pun=False):
    poll = ''

    if upper:
        poll += string.ascii_uppercase
    
    if lower:
        poll += string.ascii_lowercase
    
    if digit:
        poll += string.digits
    
    if pun:
        poll += string.punctuation
    
    if poll == '':
        poll += string.ascii_letters
    
    password = choices(poll, k=length)
    return ''.join(password)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='your lenth')
    parser.add_argument('-u',action='store_true', help='UPPER')
    parser.add_argument('-l',action='store_true', help='LOWER')
    parser.add_argument('-d',action='store_true', help='DIGIT')
    parser.add_argument('-p',action='store_true', help='PUN')

    args = parser.parse_args()
    print(password_creator(args.length, args.u, args.l, args.d, args.p))