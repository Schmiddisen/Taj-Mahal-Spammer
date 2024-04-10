import time
import requests
import argparse

parser = argparse.ArgumentParser(
                    prog='taj-spammer.py',
                    description='This script sends requests to the LEGO Taj Mahal in the living room of Dr. Florian Volk.',
                    epilog='Have fun!')

parser.add_argument('-m', '--mode', help='Pick what colors get sent. Available: \
                    random, police(blue and red), rainbow')
parser.add_argument('-d', '--delay', help='Set the delay between requests in seconds. Standard is 15.')

args = parser.parse_args()

mode = args.mode
delay = args.delay

payloads = \
{   'police':{
    'red':{'color': '#ff0000', 'ajax': 'true', 'beforesend': ''},
    'blue': {'color': '#0026ff', 'ajax': 'true', 'beforesend': ''}
    },
    'rainbow': {
        'red': {'color': '#ff0000', 'ajax': 'true', 'beforesend': ''},
        'orange': {'color': '#ffa500', 'ajax': 'true', 'beforesend': ''},
        'yellow': {'color': '#ffff00', 'ajax': 'true', 'beforesend': ''},
        'green': {'color': '#008000', 'ajax': 'true', 'beforesend': ''},
        'blue': {'color': '#0000ff', 'ajax': 'true', 'beforesend': ''},
        'indigo': {'color': '#4b0082', 'ajax': 'true', 'beforesend': ''},
        'violet': {'color': '#8b00ff', 'ajax': 'true', 'beforesend': ''},
    }
}


def send_request(payload):
    for _, values in payload.items():
        r = requests.get('https://iot24c.de/tajmahal/', params=values)
        if 'false' in r.text:
            print('Fehler aufgetreten!')
            print(r.text)


while True:
    if not mode:
        mode = 'rainbow'
    if not delay:
        delay = 15
    print(f'Sending {mode} with a delay of {delay}!')
    send_request(payloads[mode])
    time.sleep(delay)
