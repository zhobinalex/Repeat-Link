from PyInquirer import prompt, Separator
import os
import time

questions = [
    {
        'type': 'input',
        'name': 'url',
        'message': 'Enter the URL to open:',
        'validate': lambda val: val.startswith('http'),
    },
    {
        'type': 'input',
        'name': 'rest_time',
        'message': 'Enter wait time between opens (seconds):',
        'validate': lambda val: val.isdigit() and int(val) > 0,
        'filter': lambda val: int(val),
    },
    {
        'type': 'input',
        'name': 'num_clicks',
        'message': 'How many times to open the link?',
        'validate': lambda val: val.isdigit() and int(val) > 0,
        'filter': lambda val: int(val),
    }
]

answers = prompt(questions)

url = answers['url']
rest_time = answers['rest_time']
num_clicks = answers['num_clicks']

for i in range(num_clicks):
    print(f"\nOpening {url} ({i+1}/{num_clicks})")
    os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
    if i < num_clicks - 1:
        print(f"Waiting {rest_time} seconds before next open...")
        time.sleep(rest_time)

print("\nDone!")
