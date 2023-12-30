#!/opt/anaconda3/bin/python
#
# Downloads "today's" input.txt from Advent of Code. Timezone set to EST
# since that's what AoC uses.
#
# Suggest having it run on a cron at 9:00 PST :-)
#
# For example (if your computer is on PST):
# 0 21 * 12 * /Users/{username}/dev/advent/{year}/download_input.py
#
# Assumes that you have a file called session.txt that has your
# session cookie in it right next to this python file. It would be
# wise to .gitignore it if you're checking your work in :-)

import requests
from os.path import dirname, abspath, join, exists
from os import mkdir 
import datetime
import time 
from pytz import timezone

time.sleep(1) # Make sure it's after midnight in EST as far as AoC is concerned :-) 
current_time = datetime.datetime.now(timezone('EST'))
day = current_time.day
year = current_time.year

base_dir = dirname(abspath(__file__))
with open(join(base_dir, 'session.txt'), 'r') as sess:
    session_cookie = sess.readline().strip()


url = f"https://adventofcode.com/{year}/day/{day}/input"
resp = requests.get(url, cookies={'session': session_cookie})
day_dir = join(base_dir, str(day))
if not exists(day_dir):
    mkdir(day_dir)
output_path = join(day_dir, 'input.txt')
with open(output_path, 'w') as outfile:
    outfile.write(resp.text)
