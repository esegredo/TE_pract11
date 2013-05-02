#!/usr/bin/python

import os, platform, sys

def getCPUinfo():
  infofile = '/proc/cpuinfo'
  cpuinfo = {}

  if (os.path.isfile(infofile)):
    f = open(infofile, 'r')
    for line in f:
      try:
        name, value = [w.strip() for w in line.split(':')]
      except:
        continue
      if name == 'model name':
        cpuinfo['CPU type'] = value
      elif name == 'cache size':
        cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
        cpuinfo['CPU speed'] = value + ' Hz'
      elif name == 'vendor_id':
        cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo

def getOSinfo():
  return platform.platform()

def getPythoninfo():
  return platform.python_version()

if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print 'Correct usage: {0} file_name'.format(sys.argv[0])
  else:
    cpuinfo = getCPUinfo()
    osinfo = getOSinfo()
    pythoninfo = getPythoninfo()

    f = open(sys.argv[1], 'w')
    f.write('{:*^80}\n'.format('CPU Info'))
    f.write('{0:<15} {1:<60}\n'.format('CPU type:', cpuinfo['CPU type']))
    f.write('{0:<15} {1:<60}\n'.format('CPU cache size:', cpuinfo['cache size']))
    f.write('{0:<15} {1:<60}\n'.format('CPU speed:', cpuinfo['CPU speed']))
    f.write('{0:<15} {1:<60}\n'.format('CPU vendor ID:', cpuinfo['vendor ID']))

    f.write('{:*^80}\n'.format('OS Info'))
    f.write('{0:<15} {1:<60}\n'.format('Platform:', osinfo))
    
    f.write('{:*^80}\n'.format('Python Info'))
    f.write('{0:<15} {1:<60}\n'.format('Version:', pythoninfo))
    f.close()
