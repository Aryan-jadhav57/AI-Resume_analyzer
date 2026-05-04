from sqlalchemy import create_engine

# sqlalchemy.orm is used to raw code is used for database and declarative base is used as base classes for tables and session maker is used for session,read
from sqlalchemy.orm import declarative_base, sessionmaker  

DATABASE_URL = "mysql+pymysql://2SkfjRTzvkJdFfE.root:M9vDcq7xECfxAm8T@gateway01.us-east-1.prod.aws.tidbcloud.com:4000/test"

engine = create_engine(    # create databaase connection
  DATABASE_URL,            #use the above link
  pool_pre_ping=True,      #check connection before use
  connect_args={           #extra settings and secure connection
    "ssl":{                 # ssl used for security
      "ca": "C:/Users/Aryan/Downloads/isrgrootx1.pem"
    }
  }
)

SessionLocal = sessionmaker(bind=engine)      #session updates
Base = declarative_base()                     #used for tables