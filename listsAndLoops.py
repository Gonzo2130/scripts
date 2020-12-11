#!/usr/bin/env python3
import time

allNode = ['web1', 'web2', 'db1', 'db2', 'dc1', 'dc2']
allDCNodes = ['dc1', 'dc2']
allWebNodes = ['web1', 'web2']
allDBNodes = ['db1', 'db2']
'''
for a  in allNode: # a => web1, web2, db1,..., dc2
    time.sleep(1)
    print(a)
'''
for a in allNode:
    if a in allDCNodes:
        #Do Not update or Reboot
        print("Skipping updates, and reboots...on", a)
    elif a in allWebNodes:
        print("Updating Web Servers", a)
        # Push Updates to node a
    elif a in allDBNodes:
        print("Updating DB Server", a)
    else:
        print(a, "Could not be reached")
    time.sleep(1)

print("Hello")