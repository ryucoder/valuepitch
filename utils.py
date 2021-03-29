import os 

import settings


class HelperUtil():

    @staticmethod
    def create_folder_if_doesnt_exists(output_folder):
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

