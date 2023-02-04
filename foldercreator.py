from pathlib import Path
import os

os.makedirs(Path.home()/Path('Desktop/2302 Şub'))
for i in range (1,32):
    os.makedirs(Path.home()/Path('Desktop/2302 Şub/'+str(i)))