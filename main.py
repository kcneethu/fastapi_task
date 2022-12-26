import logging
import random
import string
import time
from fastapi import FastAPI, Depends, HTTPException, status, Request, File, UploadFile
from fastapi.security import  OAuth2PasswordRequestForm
from fastapi.responses import FileResponse
from datetime import datetime, timedelta

from config import *
from utility import *
from auth.auth import *


app = FastAPI()


#set logger
logging.basicConfig(filename="logs/test.log", format='format=%(asctime)s loglevel=%(levelname)-6s logger=%(name)s %(funcName)s() L%(lineno)-4d %(message)s   call_trace=%(pathname)s L%(lineno)-4d',filemode='a',level=logging.DEBUG)

# Creating an object
logger = logging.getLogger() 

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

@app.post("/token", response_model=Token)
async def root(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info("token request initiated")
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/convert_image")
def upload( request: Request,current_user: User = Depends(get_current_active_user),file: UploadFile = File(...)):
    try:
        if file.filename.lower().endswith(('.jpeg','.jpg')):
            contents = file.file.read()
            with open(TEMP_IMG_FOLDER+file.filename, 'wb') as f:
                f.write(contents)
            url = request.url._url
            png_file = jpeg_to_png(file.filename,url[:url.rfind('/')])
        else:
            return {"message": "image should be jpeg" }
    except Exception as ex:
        logger.error(ex)
        print(ex)
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    logger.info( f"Successfully uploaded {png_file}")
    return {"png-url": f"{png_file}", "status" : "success"}

@app.get("/load_image/{img_name}")
def root(img_name: str):
    try:
        file_path = PNG_IMG_FOLDER+ img_name
        return FileResponse(file_path)
    except Exception as ex:
        logger.error(ex)
        return {"message": "There was an error viewing the file"}

@app.get("/list_conversion_requests")
async def root(current_user: User = Depends(get_current_active_user)):
    logger.info("list_conversion_requests request initiated")
    return get_all_requests()