#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons
# Edited 12/3/2020 - v1.1 - csimmons
# Edited 12/10/2020 - v1.2 - csimmons
#edited 12/11 - 12/13 2020 - v2.0 -csimmons

import sys
import os 
import pathlib
from operator import itemgetter

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Rutolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

menu_prompt = '\n'.join(('Please choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Send thank you letters to all donors',
          '4 - Quit',
          '>>> '))

thanks_prompt = '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '\n>>>  '))

gift_prompt = '\n'.join(('\nPlease enter the donation amount ("$" and commas are not needed)',
                '>>>  '))

letter = (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands, perhaps\n'
        'even millions, enjoy the wonders of the Emerald city!\n\n'
        'Sincerely,\n\n'
        'H.P. Lovecraft \n'))

def print_donors(donors):
    print('\nMaster List of Donors:\n')
    for donor in donors:
        print(donor)
    print('\n')

def exist_donor(response, donors):
    gift = int(input(gift_prompt))
    response = response.title()
    for donor in donors:
        if response == donor:
            donorlist_dict.setdefault(donor, []).append(gift)
    print(letter.format(response, gift))

def new_donor(response):    
    response = response.title()
    print(('\n{} is a new donor!').format(response))
    gift = int(input(gift_prompt))
    donorlist_dict[response] = [gift]
    print(letter.format(response, gift))

def print_donorlist(all_info):
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 32) +'\n'
    info_row = '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format
    print(header1)
    print(header2)
    for donor in all_info:
        idx = all_info.index(donor)
        name1 = all_info[idx][0]
        total1 = all_info[idx][1]
        gifts1 = all_info[idx][2]
        avg1 = all_info[idx][3]
        print(info_row(dname=name1, total=total1, gifts=gifts1, avg=avg1))
    print('\n')

def send_thankyou():
    donors = list(donorlist_dict.keys())
    response = input(thanks_prompt)
    if response.lower() == 'list':
        print_donors(donors)
    elif response.lower() == 'exit': 
        return
    elif response.title() in donors:
        exist_donor(response, donors)
    else:
        new_donor(response)

def generate_letters():
    isdir = os.path.isdir('letters')  
    if isdir == True:
        pass
    else:
        os.mkdir('letters')
    for key, value in donorlist_dict.items():
        donor = str(key.replace(' ', '_'))
        gift = (list(value))[-1]
        filename = 'letters/' + donor + '.txt'
        with open(filename, 'w') as output:
            output.write(letter.format(donor, gift))
        output.close
    print('\nThank You letters were generated for all donors\n')

def display_report():
    all_info = []
    for key, value in donorlist_dict.items():
        donor_info = []
        donor_info.append(key)
        donor_info.append(sum(value))
        donor_info.append(len(value))
        donor_info.append(sum(value)/len(value))
        all_info.append(donor_info)
    all_info = sorted(all_info, key=itemgetter (1), reverse=True)
    print_donorlist(all_info) 

def program_exit():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

menu_prompt = '\n'.join(('Please choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Send thank you letters to all donors',
          '4 - Quit',
          '>>> '))

menu_dict = {
            '1' : send_thankyou,
            '2' : display_report,
            '3' : generate_letters,
            '4' : program_exit
            }
             
def menu_select(menu_prompt, menu_dict):
    while True:
        response = input(menu_prompt)
        if menu_dict[response]() == 'exit menu':
            break
    
if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!')
    menu_select(menu_prompt, menu_dict)