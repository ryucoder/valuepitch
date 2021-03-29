import settings
import requests

from pprint import pprint


START = settings.CURRENT_YEAR
STOP = settings.CURRENT_YEAR - settings.YEAR_RANGE
RANGE = -1

all_data = []

for dairy_number in range(1, (settings.DAIRY_RANGE + 1)):
    for year_number in range(START, STOP, RANGE):

        response = requests.get(settings.CAPTCHA_URL)
        captcha_number = response.json()

        data = {
            "d_no": dairy_number,
            "d_yr": year_number,
            "ansCaptcha": captcha_number 
        }
        print() 
        print() 
        pprint(data) 
        print() 
        print()

        all_data.append(data)


print() 
print() 
pprint("all_data") 
pprint(len(all_data)) 
print() 
print()
