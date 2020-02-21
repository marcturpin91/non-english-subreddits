import csv

# will contain existing subreddits (removing '/r/') in file, and allow adding new subreddits via console
subreddit_set = set()

with open('foreign_language_subreddits.txt', 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        for subreddit in row:
            subreddit_set.add(subreddit.lower())

# console input loop for adding additional new subreddits
new_subreddits = []
while True:
    print('Enter subreddit name without "/r/" prefix, q to Quit, r to remove last entry')
    input_text = str(input()).lower().strip()
    # quit
    if input_text == 'q':
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
        subreddit = '/r/' + input_text
        if subreddit not in subreddit_set:
            subreddit_set.add(subreddit)
            new_subreddits.append(subreddit)
            print(subreddit, 'added to set')
        else:
            print(subreddit, 'already present in set')

# sorted subreddit list
subreddit_list = sorted([subreddit for subreddit in subreddit_set])

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

### List of Non-English Subreddits'''

with open('README.md', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\n',escapechar=' ',quoting=csv.QUOTE_NONE)
    writer.writerow([readme_static_info])
    writer.writerow(subreddit_list)
