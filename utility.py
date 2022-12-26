'''
Utils.py contains all utility functions
used during the inference process
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.models import *
from db.database import Database
from sqlalchemy import and_, desc
from schemas.user import *
import logging
import PIL.Image # Adding the GUI interface
from tkinter import *
import os
from config import *
import uuid


database = Database()
engine = database.get_db_connection()

logger = logging.getLogger() 

def jpeg_to_png(filename,url):
    '''
    Method for converting jpeg/jpg to png
    Input: filename of image, current url 
    Output: Returns url of converted png file
    Example usage: pmg_gile = jpeg_to_png(filename,url)
    '''
    im = PIL.Image.open(TEMP_IMG_FOLDER+filename)
    png_filename = str(uuid.uuid4()) +'-' + os.path.splitext(filename)[0]+'.png'
    im.save(PNG_IMG_FOLDER+png_filename)
    #os.remove(TEMP_IMG_FOLDER+filename)
    png_url = url+'/load_image/'+png_filename 
    insert_requests(TEMP_IMG_FOLDER+filename,png_url)
    return png_url

def insert_requests(source_file,png_file):
    '''
    Method for insert image conversion requests
    Input: source file to convert, filepath of png image  
    Output: Returns inserted data
    Example usage: data = insert_requests(source_path,png_url)
    '''
    session = database.get_db_session(engine)
    data = Conversionrequest(
                    source_file = source_file,
                    png_file = png_file,
                    status = 'success')
    session.add(data)   
    session.commit()
    return data

def get_all_requests():
    '''
    Method for get all image conversion requests
    Input: No Input  
    Output: Returns requests
    Example usage: requests = get_all_requests()
    '''
    session = database.get_db_session(engine)
    data = session.query(Conversionrequest.source_file, Conversionrequest.png_file, Conversionrequest.status, Conversionrequest.created_at).order_by(
        desc(Conversionrequest.created_at)).all()
    return data