import os 
import shutil

import settings


class HelperUtil():

    @staticmethod
    def delete_folder_if_exists(output_folder):
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
            
    @staticmethod
    def create_folder_if_doesnt_exists(output_folder):
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

