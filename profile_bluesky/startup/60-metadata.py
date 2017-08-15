print(__file__)

# Set up default metadata

import socket 
import getpass
import sqlite3

def print_scan_ids(name, start_doc):
    """prints scan IDs at the start of each scan"""
    print("Transient Scan ID: {0}".format(start_doc['scan_id']))
    print("Persistent Unique Scan ID: '{0}'".format(start_doc['uid']))

HOSTNAME = socket.gethostname() or 'localhost' 
USERNAME = getpass.getuser() or 'synApps_xxx_user'

# Set up default metadata

md = dict(**RE.md)
md['beamline_id'] = '32-ID-C'
md['proposal_id'] = 'MONA project 6875'
md['pid'] = os.getpid()
md['login_id'] = USERNAME + '@' + HOSTNAME
try:
    RE.md = dict(**md)
    RE.subscribe('start', print_scan_ids)   # add as callback
except sqlite3.OperationalError as exc:
    # FIXME: this is not trapping the exception yet!
    # TODO: find the thread
    # TODO: report the user/host/pid that has it locked
    msg = "Cannot write to the ipython history file."
    msg += "  It is open by another session."
    print(msg)


###  import os
###  for key, value in os.environ.items():
###	     if key.startswith("EPICS"):
###  		     gs.RE.md[key] = value
