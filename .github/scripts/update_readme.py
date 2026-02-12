import re
import requests
from datetime import datetime
import os

LEETCODE_USERNAME = 'divakarvelagacherla'

# Get absolute path to README.md
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '../../README.md'))

# Fetch LeetCode stats
leetcode_api = f'https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}'
try:
    stats = requests.get(leetcode_api).json()
    problems_solved = stats.get('totalSolved', 'N/A')
    print(f"Fetched problems solved: {problems_solved}")
except Exception:
    problems_solved = 'N/A'

# Get current date
now = datetime.utcnow()
date_str = now.strftime('%b %d, %Y')

with open(README_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Problems Solved
content = re.sub(r'Problems Solved: \[.*?\]', f'Problems Solved: [{problems_solved}]', content)
# Update Last Updated
content = re.sub(r'Last Updated: .*', f'Last Updated: {date_str}', content)

with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
