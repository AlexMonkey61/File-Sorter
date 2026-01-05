import os
import values

def prepare(dir):
    print('Verifying directory structure...')
    print(dir)
    if os.path.isdir(dir):
        values.mainDir = dir
        print('Directory structure verified successfully.')
    else:
        print('Directory structure NOT verified successfully.')
    print('Preparing directories to sort...')
    os.makedirs(f'{values.mainDir}/.IMAGE', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.VIDEO', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.AUDIO', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.TEXT', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.APP', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.ARCHIVE', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.PDF', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.WORD', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.POWERPOINT', exist_ok=True)
    os.makedirs(f'{values.mainDir}/.EXCEL', exist_ok=True)
    print('Directories prepared.')