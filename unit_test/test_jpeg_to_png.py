import warnings, sys, os
warnings.filterwarnings("ignore")
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
import pytest
from config import *
from pathlib import Path

class TestJpegToPng:
    def test_source_folder_exist(self):
        source_path = Path(TEMP_IMG_FOLDER)
        assert source_path.exists() == True, "Source folder exists"

    def test_png_folder_exist(self):
        source_path = Path(PNG_IMG_FOLDER)
        assert source_path.exists() == True, "output folder exists"