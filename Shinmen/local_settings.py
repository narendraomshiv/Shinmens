import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # 'default': {
    #     'ENGINE'  : 'django.db.backends.mysql',
    #     'NAME'    : 'shinmandb',
    #     'USER'    : 'root',                     
    #     'PASSWORD': 'Root@1234',            
    #     'HOST'    : 'localhost',               
    #     'PORT'    : '3306',
    # },
    
}    