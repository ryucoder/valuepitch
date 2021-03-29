import os 
import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

CAPTCHA_URL = "https://main.sci.gov.in/php/captcha_num.php"
TARGET_URL = "https://main.sci.gov.in/php/case_status/case_status_process.php"


CURRENT_YEAR = datetime.datetime.now().year
YEAR_RANGE = 20 
DAIRY_RANGE = 100 

