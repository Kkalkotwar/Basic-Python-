# Creating a basic logging Python File
# Division of two numbers

import logging
logging.basicConfig(filename='test2.log', level=logging.INFO, format="%(levelname)s,%(asctime)s %(message)s")

def div(a,b) :
    logging.info('We are into the function')
    try :
        logging.info('User entered the number %s and %s', a,b)
        div = a/b
        logging.info('The division of two number is %s',div)
        return div
    except Exception as e:
        logging.exception(e)


div(3,0)

