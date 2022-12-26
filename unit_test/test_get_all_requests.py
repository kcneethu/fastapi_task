import warnings, sys, os
warnings.filterwarnings("ignore")
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
import pytest
from utils import *
from pathlib import Path
from db.database import Database

class TestGetAllRequests:
    def check_table_exists(self):
        database = Database()
        engine = database.get_db_connection()
        insp = engine.inspect(engine)
        assert insp.has_table("conversion_request", schema="dbo") == True, "connection_request_table_exist"
