import os
from os.path import dirname
from pathlib import Path

#path = os.path.dirname(__file__) + '/text.txt'
#path = Path(os.path.dirname(__file__) + '/text.txt').resolve()
path = Path(dirname(__file__) + '/text.txt').resolve()
print(path)

with open(path,'r') as file:
    print(file.read())
    
    