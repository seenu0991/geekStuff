#************************************************************
          #  *SITE CLONING SNIPPETS*
#************************************************************
# Prerequisites Libraries 

from concurrent.futures import process
from posixpath import dirname
import subprocess
from tabnanny import verbose
from matplotlib.pyplot import bar
import os

# Directory creation 

Dirname =input("enter the dir name:")
os.mkdir(Dirname)
#url =input("enter the url:")

# Function wget
def runcmd(cmd, verbose = True, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass
print('::::::::::copying site::::::::::')

runcmd('wget --recursive --level=3 --convert-links  https://progeco-holland.com  -q --show-progress --progress=dot', verbose = True )

print(':::::::::copy completed:::::::::::::::::')

##workin progress
