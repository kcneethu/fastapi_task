from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from config import *

logger = logging.getLogger() 

class Database():
    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_db_connection(self):
        if self.connection_is_active == False:
            connect_args = {"connect_timeout":CONNECT_TIMEOUT}
            try:
                self.engine = create_engine(MYSQL_URL, pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE,
                        pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW, connect_args=connect_args)
                logger.info("mysql connected successfully ")
                return self.engine
            except Exception as ex:
                logger.error("Error connecting to DB : ")
                logger.error(ex)
        return self.engine

    def get_db_session(self,engine):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            return session
        except Exception as ex:
            logger.error("Error getting DB session : ")
            logger.error(ex)
            return None