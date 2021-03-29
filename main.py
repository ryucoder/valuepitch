import settings
import requests
import os

from pprint import pprint


def initial_operations():

    # Check and Create Output Folder
    output_folder = settings.OUTPUT_FOLDER

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)


def download_responses():
    START = settings.CURRENT_YEAR
    STOP = settings.CURRENT_YEAR - settings.YEAR_RANGE
    RANGE = -1

    filenames = []

    for dairy_number in range(1, 3):
        for year_number in range(START, 2023):

            response = requests.get(settings.CAPTCHA_URL)
            captcha_number = response.json()

            data = {
                "d_no": dairy_number,
                "d_yr": year_number,
                "ansCaptcha": captcha_number 
            }

            # store the response to the output folder 
            current_output_folder = os.path.join(settings.OUTPUT_FOLDER, str(dairy_number))

            if not os.path.exists(current_output_folder):
                os.mkdir(current_output_folder)

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

