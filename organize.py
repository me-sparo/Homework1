import json
import re
import os
import nbformat as nbf

nb = nbf.v4.new_notebook()

print("Hi! This program writes all of your correct (score=100%) HackerRank submissions to a jupyter notebook file and creates a README.md file")
print('If you still don\'t have it you can download the JSON file containing all of your submissions from https://www.hackerrank.com/settings/account and then \'Export Data\'\n')

file_name = input("Enter file name or path of JSON file: ")

if not os.path.exists('excercises/'):
    os.makedirs('excercises/')

print('--------------------------------------------------')

readme = open('README.md', 'w')
name = input('Please input your name and surname: ')
matricola = input('Please input your Student ID (Matricola): ')
readme.write(f'# {name} - {matricola}\nThe content of this repo is organized as follows: each and every excercise is included both in the `excercises/` folder (each excercise in a different file) **and** aggregated in the file `scripts.ipynb`')
print('\n--------------------------------------------------')

with open(file_name) as json_file:
    data = json.load(json_file)

    for sub in data['submissions']:
        if sub['score'] < 1:
            continue
        print(sub['challenge'])

        title = re.sub(r'[\s\.",!?\-\(\)]', '',sub["challenge"])
        mode = 'w' if os.path.exists(f'excercises/{title}.py') else 'x'
        with open(f'excercises/{title}.py', mode) as f:
            f.write(sub['code'])

        nb['cells'].append(nbf.v4.new_markdown_cell(f'#### {sub["challenge"]}'))
        nb['cells'].append(nbf.v4.new_code_cell(sub['code']))


readme.close()         
with open('scripts.ipynb', 'w') as f:
    nbf.write(nb, f)

print('\n--------------------------------------------------')
print('All done!\nBefore submitting the repo remember to: \n - generate the pdf file from Hackerrank (https://www.hackerrank.com/submissions/)\n - delete this and the JSON file\n - Customize the README.md file if needed')
print('Also remeber that this program only considers excercises that got the full score, if you wish to add any excercise which scored less than 100% you\'ll have to do it manually')
print('If you need any help contact me on telegram: @mamiglia\n\nBest of Luck ~ Matteo Migliarini')