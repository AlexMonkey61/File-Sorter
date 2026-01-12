import os
import shutil
import time
import values
from values import *
import logging

def sort_type(file):
    for t, ends in types.items():
        if file.endswith(tuple(ends)):
            logging.log(1, f'{file} <- {t}')
            shutil.move(f'{values.mainDir}/{file}', f'{values.mainDir}/.SORTED/.{t.upper()}')


def sort_files():
    for file in os.listdir(values.mainDir):
        try:
            sort_type(file)
        except Exception as e:
            logging.log(1, e)