import requests
import os

from pprint import pprint

import settings

from utils import HelperUtil


def initial_operations():

    # Condition 1 
    HelperUtil.delete_folder_if_exists(settings.OUTPUT_FOLDER)

    # Condition 2 
    HelperUtil.create_folder_if_doesnt_exists(settings.OUTPUT_FOLDER)
    
    # Any Other Conditions Go Below 
    # pass 


def download_responses():
    START = settings.START_YEAR
    STOP = settings.START_YEAR - settings.YEAR_RANGE
    RANGE = -1

    filenames = []

    # for dairy_number in range(1, (settings.DAIRY_RANGE + 1)):
    #     for year_number in range(START, STOP, RANGE):

    # for dairy_number in range(1, 3):
    #     for year_number in range(START, 2018, -1):

    for dairy_number in [1]:
        for year_number in [2021]:

            response = requests.get(settings.CAPTCHA_URL)
            captcha_number = response.json()

            data = {
                "d_no": dairy_number,
                "d_yr": year_number,
                "ansCaptcha": captcha_number 
            }

            headers = {

                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Length': '32',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'BNI_persistence=NUIffASvAES-Jfr7DCxSQMtFVHFbIE1c9pth3xH4rA1jUKtiDGvBUg0z-lEWCRTcSfIuUWPWSAqd_uVdJtAGFw==; has_js=1; SESS3e237ce09ea0ff0fb3e315573005c968=FAM9zw7x6417Ll8z0EcZIRVCx80CPVSVkOAObKG7HUs',
                'Host': 'main.sci.gov.in',
                'Origin': 'https://main.sci.gov.in',
                'Referer': 'https://main.sci.gov.in/case-status',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'

            } 

            response = requests.post(settings.TARGET_URL, data=data, headers=headers)
            # response is not what we need 
            # Request gets redirected because of cors policy
            # Need to find a solution for that 
            # response.url is https://main.sci.gov.in/


            print()
            print()
            print(response) 
            print(response.url) 
            # pprint(dir(response)) 
            print(response.status_code) 
            # print(response.text) # str
            # print(response.content) # bytes
            print()
            print()

            # store the response to the output folder 
            current_output_folder = os.path.join(settings.OUTPUT_FOLDER, str(dairy_number))

            HelperUtil.create_folder_if_doesnt_exists(current_output_folder)
    
            current_filename = os.path.join(current_output_folder, "{}.html".format(year_number))
            
            filenames.append(current_filename)

            with open(current_filename, "wb") as f:
                f.write(response.content)


def extract_data_from_responses():
    pass 


def main():
    initial_operations()
    download_responses()
    extract_data_from_responses()


if __name__ == "__main__":
    main()

