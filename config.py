#!/usr/bin/env python3

import requests
import sys
import subprocess
from datetime import datetime

requests.packages.urllib3.disable_warnings()

# Make sure requested arguments are given
# registry_source -> Docker Registry where actual images are allocated
# registry_dest -> Docker Registry where images will be pushed to
try:
    registry_source = (sys.argv[1])
    registry_dest = (sys.argv[2])
except IndexError:
    print(colored("Please specify source and destination registry", 'red'))
    raise SystemExit(0)

# Register start migrate datetime
start_time = str(datetime.now().strftime("%D, %H:%M:%S"))
