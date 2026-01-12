import os
import values
import logging

def prepare(dir):
    logging.log(1, 'Verifying directory structure...')
    logging.log(1, dir)
    if os.path.isdir(dir):
        values.mainDir = dir
        logging.log(1, 'Directory structure verified successfully.')
    else:
        logging.log(1, 'Directory structure NOT verified successfully.')
    logging.log(1, 'Preparing directories to sort...')
    for name in values.types:
        os.makedirs(f'{values.mainDir}/.SORTED/.{name.upper()}', exist_ok=True)
    logging.log(1, 'Directories prepared.')