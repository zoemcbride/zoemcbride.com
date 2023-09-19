import os
from flask_frozen import Freezer
from app import app

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True

if __name__ == '__main__':
    freezer.freeze()