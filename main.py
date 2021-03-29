import requests
import os

from pprint import pprint

import settings

from utils import HelperUtil

from bs4 import BeautifulSoup


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

    for dairy_number in [1, 2]:
        for year_number in [2021]:

            response = requests.get(settings.CAPTCHA_URL)
            captcha_number = response.json()

            data = {
                "d_no": dairy_number,
                "d_yr": year_number,
                "ansCaptcha": captcha_number 
            }

            headers = {
                # 'Host': 'main.sci.gov.in',
                # 'Origin': 'https://main.sci.gov.in',
                'Referer': 'https://main.sci.gov.in/case-status',
            } 

            # Only Referer header is required to bypass CORS 
            # You can verify using response.url 
            response = requests.post(settings.TARGET_URL, data=data, headers=headers)

            # print()
            # print()
            # pprint(dir(response)) 
            # print(response.url) 
            # print(response.status_code) 
            # print(response.text) # str
            # print(response.content) # bytes
            # print()
            # print()

            # store the response to the output folder 
            current_output_folder = os.path.join(settings.OUTPUT_FOLDER, str(dairy_number))

            HelperUtil.create_folder_if_doesnt_exists(current_output_folder)
    
            current_filename = os.path.join(current_output_folder, "{}.html".format(year_number))
            
            filenames.append(current_filename)

            with open(current_filename, "wb") as f:
                f.write(response.content)


def extract_data_from_responses():
    
    # read all the html files inside the output folder 
    urls = {}

    for root, dirs, files in os.walk(settings.OUTPUT_FOLDER):
        if root != settings.OUTPUT_FOLDER:

            diary = str(root.split("/")[-1])

            urls[diary] = []

            for file_name in files:
                if file_name.split(".")[-1] == "html":
                    absolute_file_path = root + "/" + file_name
                    urls[diary].append(absolute_file_path)
                    break


    # loop over it and extract the data from each file and store in temp dict, put dict in list 


    extracted_data = {}

    for diary_number in urls.keys():
        for response_file in urls[diary_number]: 


            extracted_data[diary_number] = {
                    "diary_no": None,
                    "who_vs_who": None 
                }

            with open(response_file) as fp:
                soup = BeautifulSoup(fp, 'html.parser')

                # print(soup.find_all('h5'))

                h5_tags = soup.find_all('h5')
                extracted_data[diary_number]["diary_no"] = h5_tags[0].string
                extracted_data[diary_number]["who_vs_who"] = h5_tags[1].string
                
                h4_tags = soup.find_all('h4')

                # Each case has different no of tabs
                for h4_tag in h4_tags:
                    extracted_data[diary_number][h4_tag.find("a").string] = {}

                
                # Read Case Details 
                
                extracted_data[diary_number][h4_tags[0].find("a").string] = {}
                case_details = soup.find("div", {"id": "collapse1"})
                
                for table_row in case_details.find("table").find_all("tr"): 

                    all_tds = table_row.find_all("td")

                    row_header = all_tds[0].string
                    row_data = all_tds[1].string

                    extracted_data[diary_number][h4_tags[0].find("a").string][row_header] = row_data

    print()
    print()
    print("extracted_data")
    pprint(extracted_data)
    print()
    print()
              
    # dump the list in csv file
    # For each dairy create a single csv for data of all years
    
    # bingo ! 


def main():
    # initial_operations()
    # download_responses()
    extract_data_from_responses()


if __name__ == "__main__":
    main()

