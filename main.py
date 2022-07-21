#import library
import pandas as pd
import argparse
from mailmodule import mail as ma


# Script functions 

df_distance_final = pd.read_csv('./bicimad_coles_escuelas.csv')

#function that extract all the results

def all_school():
    df_distance_final = pd.read_csv('./bicimad_coles_escuelas.csv')
    return print(df_distance_final)


# function that extract just one school or kindergarten
def one_school():
    colegio = str(input("Please, enter the name of School: "))
    final = df_distance_final.loc[df_distance_final["School name"] == colegio]
    return print(final)


def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application for distance between schools and bicimad' )
    help_message ='You have two options. Option 1: "one" print one school or kindergarten in concret. Option 2: "all" school or kindergarten of Madrid city' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args

# Pipeline execution

if __name__ == '__main__':
    if argument_parser().function == 'one':
        result = one_school()
    elif argument_parser().function == 'all':
        result = all_school()
        ma.mailing()
    else:
        result = 'FATAL ERROR...you need to select the correct method'
    print(f'The result is => {result}')



