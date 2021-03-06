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

    for year_number in range(START, STOP, RANGE):
        for dairy_number in range(1, (settings.DAIRY_RANGE + 1)):

            response = requests.get(settings.CAPTCHA_URL)
            captcha_number = response.json()

            data = {
                "d_no": dairy_number,
                "d_yr": year_number,
                "ansCaptcha": captcha_number,
            }

            headers = {
                # 'Host': 'main.sci.gov.in',
                # 'Origin': 'https://main.sci.gov.in',
                "Referer": "https://main.sci.gov.in/case-status",
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
            current_output_folder = os.path.join(
                settings.OUTPUT_FOLDER, str(year_number)
            )

            HelperUtil.create_folder_if_doesnt_exists(current_output_folder)

            current_filename = os.path.join(
                current_output_folder, "{}.html".format(dairy_number)
            )

            filenames.append(current_filename)

            with open(current_filename, "wb") as f:
                f.write(response.content)


def extract_data_from_responses():

    # read all the html files inside the output folder
    urls = HelperUtil.get_urls()

    extracted_data = HelperUtil.get_extracted_data(urls)

    HelperUtil.write_extracted_data_to_xlsx(extracted_data)


def main():
    # Operation 1
    initial_operations()
    download_responses()

    # # Operation 2
    extract_data_from_responses()


if __name__ == "__main__":
    main()
