import sys
import time

def clear_last_line() :
    # time.sleep(1)
    sys.stdout.write(f'\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()
