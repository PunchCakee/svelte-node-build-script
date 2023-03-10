import shutil
import subprocess
from contextlib import contextmanager
import os


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)



subprocess.run(["npm","run","build"], shell=True,stdout=True)
shutil.copy2("package.json",'build')
shutil.copy2("package-lock.json",'build')



with cd('build/'):
    subprocess.run(["npm","ci","--omit","dev"], shell=True,stdout=True)



