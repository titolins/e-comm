from flask import Flask
#from instance.secret import install_secret_key

#from flask_bootstrap import Bootstrap
#from flask_wtf.csrf import CsrfProtect

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
# import models

app = Flask(__name__)

#install_secret_key(app)

#Bootstrap(app)
#CsrfProtect(app)

# create db engine
# engine = create_engine('path/to/db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

import project.e_comm
