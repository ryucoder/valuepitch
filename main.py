import settings
import requests

from pprint import pprint


START = settings.CURRENT_YEAR
STOP = settings.CURRENT_YEAR - settings.YEAR_RANGE
RANGE = -1

filenames = []

for dairy_number in range(1, 3):
    for year_number in range(START, 2023):

        response = requests.get(settings.CAPTCHA_URL)
        captcha_number = response.json()

        print()
        print()
        print("response")
        print(response)
        
        print(response.text)
        print(type(response.text))

        pprint(dir(response))

        print(response.content)
        print(type(response.content))

        print()
        print()

        data = {
            "d_no": dairy_number,
            "d_yr": year_number,
            "ansCaptcha": captcha_number 
        }


        # store the response to the output folder 

        filename = f"{settings.OUTPUT_FOLDER}/{year_number}/{dairy_number}"
        
        filenames.append(filename)

        # with open(filename, "wb") as f:
        #     f.write(response.content)

print()
print()
print("filenames")
pprint(filenames)
print()
print()
