#config file that loads variables etc

import os

from dotenv import load_dotenv
load_dotenv()

#API key
api_key = os.getenv('api_key') #pulls the api key from the .env file. Please note .env file is not within the git repo. 
