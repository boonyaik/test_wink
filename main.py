#write me a code to store the current time into a file

import datetime

now = datetime.datetime.now()

with open('time.txt', 'a') as f:
    f.write(str(now))
    f.write('\n')



