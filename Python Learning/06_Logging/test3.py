# Creating the log file

import logging

logging.basicConfig(filename='test3.log', level= logging.DEBUG, format= '%(levelname)s, %(asctime)s, %(message)s')

# Lets try to do some basics opertions on files
# Always remember to use the exception handling
try:
    logging.info('Checking if the file exist')
    with open('kunal.txt','r') :
        logging.info('We are into the file')

except Exception as e :
    logging.error('File is not present in the Folder')
    logging.info('Please create the new File')