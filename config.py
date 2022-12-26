#mysql configs
MYSQL_URL = "mysql://test_user:test@localhost/assignment_task"
POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60

#image file configs
TEMP_IMG_FOLDER = 'public/source/'
PNG_IMG_FOLDER = 'public/png/'

#jwt token configs
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "hashed_password": "$2y$10$5YMTHlqiJGjN4IWUn3MDzeWjHnoNG0DQ6VYxI3QnNSMjMCKqdDL12",
        "disabled": False,
    }
}


