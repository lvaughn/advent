#!/opt/anaconda3/bin/python
#
# Downloads "today's" input.txt from Advent of Code. Timezone set to EST
# since that's what AoC uses.
#
# Suggest having it run on a cron at 9:00 PST :-)
#
# For example (if your computer is on PST):
# 0 21 * 12 * /Users/{username}/dev/advent/2022/download_input.py
#
# Assumes that you have a file called session.txt that has your
# session cookie in it right next to this python file. It would be
# wise to .gitignore it if you're checking your work in :-)

import requests
from os.path import dirname, abspath, join
import datetime
from pytz import timezone

current_time = datetime.datetime.now(timezone('EST'))
day = current_time.day
year = current_time.year

base_dir = dirname(abspath(__file__))
with open(join(base_dir, 'session.txt'), 'r') as sess:
    session_cookie = sess.readline().strip()


url = f"https://adventofcode.com/{year}/day/{day}/input"
resp = requests.get(url, cookies={'session': session_cookie})
output_path = join(base_dir, str(day), 'input.txt')
with open(output_path, 'w') as outfile:
    outfile.write(resp.text)
