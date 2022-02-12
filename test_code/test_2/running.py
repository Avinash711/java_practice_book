import os
from time import sleep

sleep(5)
os.system('python -m pytest -s test_2.py -n 6 -v')