#!/opt/anaconda3/bin/python
#

import requests
from os.path import dirname, abspath, join
import time 
import os
import shutil



base_dir = dirname(abspath(__file__))
with open(join(base_dir, 'session.txt'), 'r') as sess:
    session_cookie = sess.readline().strip()

year = 2019
template_file = join(base_dir, 'template.py')
for day in range(1, 26):
    output_dir = join(base_dir, str(day))
    # os.mkdir(output_dir)
    shutil.copyfile(template_file, join(output_dir, 'part_1.py'))
    os.remove(join(output_dir, 'part_1.txt'))
    # url = f"https://adventofcode.com/{year}/day/{day}/input"
    # resp = requests.get(url, cookies={'session': session_cookie})
    # output_path = join(output_dir, 'input.txt')
    # with open(output_path, 'w') as outfile:
    #     outfile.write(resp.text)
    # time.sleep(1)
