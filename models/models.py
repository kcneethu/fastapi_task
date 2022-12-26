from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, TIMESTAMP, text
from sqlalchemy.dialects.mysql import VARCHAR

Base = declarative_base()
 
class Conversionrequest(Base):
    __tablename__ = "conversion_request"
    request_id = Column(INTEGER, primary_key=True)
    source_file = Column(VARCHAR(45), nullable=False)
    png_file = Column(VARCHAR(45), nullable=False)
    status = Column(VARCHAR(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))
                        