#!/usr/bin/env python
# Purpose of this script: generate random bond movie recommendations
# Usage hint: $ python bondselect.py -h

import argparse
import random

def main(args):
    # print(vars(args))
    if (args.list):
        listfilms()
    elif (args.film):
        filmdetails(film=args.film)
    else:
        default(number_of_films = args.number)
    

def default(number_of_films = 1):
    for i in range(args.number):
        film, details = random.choice(list(bondfilms.items()))
        print(film)

def listfilms():
    for title in bondfilms.keys():
        print(title)

def filmdetails(film):
    if film in bondfilms:
        print('***', film, '***')
        details = bondfilms[args.film]
        for k,v in details.items():
            print(k,':',v)
    else:
        print("%s film not found" % (film))    
# --------------- Data ------------------
'''
# the data for the below 'bondfilms' dictionary was gotten 
# from Wikipedia using the below approach:

import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_James_Bond_films"
table = pd.read_html(url)[0]
table = table.droplevel(0,axis=1)
table = table.drop(columns='Ref(s)')
table = table.iloc[:-1,:]
table = table.set_index('Title')
table.to_dict(orient='index')
'''

bondfilms = {'Dr. No':
                {'Year': '1962',
                 'Bond actor': 'Sean Connery',
                 'Director': 'Terence Young',
                 'Actual $': '1.1',
                 'Adjusted $2005': '7.0'},
             'From Russia with Love':
                 {'Year': '1963',
                  'Bond actor': 'Sean Connery',
                  'Director': 'Terence Young',
                  'Actual $': '2.0',
                  'Adjusted $2005': '12.6'},
             'Goldfinger':
                 {'Year': '1964',
                  'Bond actor': 'Sean Connery',
                  'Director': 'Guy Hamilton',
                  'Actual $': '3.0',
                  'Adjusted $2005': '18.6'},
             'Thunderball':
                 {'Year': '1965',
                  'Bond actor': 'Sean Connery',
                  'Director': 'Terence Young',
                  'Actual $': '6.8',
                  'Adjusted $2005': '41.9'},
             'You Only Live Twice':
                 {'Year': '1967',
                  'Bond actor': 'Sean Connery',
                  'Director': 'Lewis Gilbert',
                  'Actual $': '10.3',
                  'Adjusted $2005': '59.9'},
             "On Her Majesty's Secret Service":
                 {'Year': '1969',
                  'Bond actor': 'George Lazenby',
                  'Director': 'Peter R. Hunt',
                  'Actual $': '7.0',
                  'Adjusted $2005': '37.3'},
             'Diamonds Are Forever':
                 {'Year': '1971',
                  'Bond actor': 'Sean Connery',
                  'Director': 'Guy Hamilton',
                  'Actual $': '7.2',
                  'Adjusted $2005': '34.7'},
             'Live and Let Die':
                 {'Year': '1973',
                  'Bond actor': 'Roger Moore',
                  'Director': 'Guy Hamilton',
                  'Actual $': '7.0',
                  'Adjusted $2005': '30.8'},
             'The Man with the Golden Gun':
                 {'Year': '1974',
                  'Bond actor': 'Roger Moore',
                  'Director': 'Guy Hamilton',
                  'Actual $': '7.0',
                  'Adjusted $2005': '27.7'},
             'The Spy Who Loved Me':
                 {'Year': '1977',
                  'Bond actor': 'Roger Moore',
                  'Director': 'Lewis Gilbert',
                  'Actual $': '14.0',
                  'Adjusted $2005': '45.1'},
             'Moonraker':
                 {'Year': '1979',
                  'Bond actor': 'Roger Moore',
                  'Director': 'Lewis Gilbert',
                  'Actual $': '34.0',
                  'Adjusted $2005': '91.5'},
             'For Your Eyes Only':
                 {'Year': '1981',
                  'Bond actor': 'Roger Moore',
                  'Director': 'John Glen',
                  'Actual $': '28.0',
                  'Adjusted $2005': '60.2'},
             'Octopussy':
                 {'Year': '1983',
                  'Bond actor': 'Roger Moore',
                  'Director': 'John Glen',
                  'Actual $': '27.5',
                  'Adjusted $2005': '53.9'},
             'A View to a Kill':
                 {'Year': '1985',
                  'Bond actor': 'Roger Moore',
                  'Director': 'John Glen',
                  'Actual $': '30.0',
                  'Adjusted $2005': '54.5'},
             'The Living Daylights':
                 {'Year': '1987',
                  'Bond actor': 'Timothy Dalton',
                  'Director': 'John Glen',
                  'Actual $': '40.0',
                  'Adjusted $2005': '68.8'},
             'Licence to Kill':
                 {'Year': '1989',
                  'Bond actor': 'Timothy Dalton',
                  'Director': 'John Glen',
                  'Actual $': '36.0',
                  'Adjusted $2005': '56.7'},
             'GoldenEye':
                 {'Year': '1995',
                  'Bond actor': 'Pierce Brosnan',
                  'Director': 'Martin Campbell',
                  'Actual $': '60.0',
                  'Adjusted $2005': '76.9'},
             'Tomorrow Never Dies':
                 {'Year': '1997',
                  'Bond actor': 'Pierce Brosnan',
                  'Director': 'Roger Spottiswoode',
                  'Actual $': '110.0',
                  'Adjusted $2005': '133.9'},
             'The World Is Not Enough':
                  {'Year': '1999',
                   'Bond actor': 'Pierce Brosnan',
                   'Director': 'Michael Apted',
                   'Actual $': '135.0',
                   'Adjusted $2005': '158.3'},
             'Die Another Day':
                 {'Year': '2002',
                  'Bond actor': 'Pierce Brosnan',
                  'Director': 'Lee Tamahori',
                  'Actual $': '142.0',
                  'Adjusted $2005':
                  '154.2'},
             'Casino Royale':
                 {'Year': '2006',
                  'Bond actor': 'Daniel Craig',
                  'Director': 'Martin Campbell',
                  'Actual $': '150.0',
                  'Adjusted $2005': '145.3'},
             'Quantum of Solace':
                 {'Year': '2008',
                  'Bond actor': 'Daniel Craig',
                  'Director': 'Marc Forster',
                  'Actual $': '200.0',
                  'Adjusted $2005': '181.4'},
             'Skyfall':
                 {'Year': '2012',
                  'Bond actor': 'Daniel Craig',
                  'Director': 'Sam Mendes',
                  'Actual $': '150–200',
                  'Adjusted $2005': '128–170'},
             'Spectre':
                 {'Year': '2015',
                  'Bond actor': 'Daniel Craig',
                  'Director': 'Sam Mendes',
                  'Actual $': '245–250[b]',
                  'Adjusted $2005': '202–206'},
             'No Time to Die':
                 {'Year': '2021',
                  'Bond actor': 'Daniel Craig',
                  'Director': 'Cary Joji Fukunaga',
                  'Actual $': '250–301',
                  'Adjusted $2005': '189–226'}}

# ----------------end of Data -----------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=1)
    parser.add_argument("-v", "--verbose", action='store_true')
    parser.add_argument("-l", "--list", action='store_true')
    parser.add_argument("-f", "--film", help="film name", default=None)
    args = parser.parse_args()
    main(args)

#  LocalWords:  args usr bondfilms listfilms
