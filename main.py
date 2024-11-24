import os
import sys
import time
from frames import frames_maker
from painter import main, out

frames_maker()

out = sys.stdout
for i in range(1120):
    f = str(i)
    s = main(f"CC\\{f}.jpg")
    os.system('cls')
    out.write(s)
    out.flush()
    time.sleep(0.25)






