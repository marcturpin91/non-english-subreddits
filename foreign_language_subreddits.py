#!/usr/bin/python

import csv
import re

# will contain existing subreddits in file, and allow adding new subreddits via console
subreddit_set = set()

with open('foreign_language_subreddits.txt', 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        for subreddit in row:
            subreddit_set.add(subreddit.lower())

# valid subreddit name pattern requirements
subreddit_pattern = re.compile("\A\/r\/[A-Za-z0-9][A-Za-z0-9_]{1,20}\Z")
new_subreddits = []

# console input loop for adding additional new subreddits
instruction_string = 'Enter subreddit name (ex: /r/brasil), q to Quit, r to remove last entry'
print(instruction_string)
while True:
    input_text = str(input()).lower().strip()
    # quit
    if input_text == 'q':
        print('Added the following subreddits: ', new_subreddits)
        break
    # remove last subreddit inputted
    elif input_text == 'r':
        if new_subreddits:
            removed_subreddit = new_subreddits.pop()
            subreddit_set.remove(removed_subreddit)
            print(removed_subreddit, 'removed')
        else:
            print('no new subreddits left to remove')
    # subreddit inputted
    else:
        if not re.match(subreddit_pattern, input_text):
            print('invalid input -', instruction_string)
            pass
        elif input_text not in subreddit_set:
            subreddit_set.add(input_text)
            new_subreddits.append(input_text)
            print(input_text, 'added to set')
        else:
            print(input_text, 'already present in set')

# sorted subreddit list
subreddit_list = sorted(subreddit_set)

# write results back to text file
with open('foreign_language_subreddits.txt', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\n')
    writer.writerow(subreddit_list)

# generate README file for GitHub display
readme_static_info = '''\
# non-english-subreddits
List of non-English subreddits. Useful for data science projects using English-based Reddit content.

### Instructions
Use foreign_language_subreddits.py script to add new foreign language subreddits to the existing list. 
The script overwrites the foreign_language_subreddits.txt with previous and new subreddits that 
were added by the user via console input. The script also updates the project's README MD file.

Users are encouraged to create a PR if they have foreign language subreddits not included in the current list.

##### Do not edit README.md directly. Changes to this file should be done in the script.

### List of Non-English Subreddits'''

with open('README.md', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\n',escapechar=' ',quoting=csv.QUOTE_NONE)
    writer.writerow([readme_static_info])
    writer.writerow(subreddit_list)
