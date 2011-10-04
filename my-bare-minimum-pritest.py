#!/usr/bin/env python
import serial
s = None

def open():
  global s
  s = serial.Serial('COM1', 1200, timeout=1)

def close():
  s.close()

def testLine(str, max=100):

  s.write(str)
  s.write('\r')

  res = []
  while True:
    r = s.read(max)
    if not r: break
    res.append(' '.join(['%02x' % ord(x) for x in r]))

  return '\n'.join(res)

def getLine(str):

  s.write(str)
  res = []
  while True:
    c = s.read(1)
    if not c: break
    res.append(c)
    if c == '\r': break

  return ''.join(res)
 
def ascii(s):
  return ''.join([chr(int(x, 16)) for x in s.split(' ')])

if False:
  open()
  for i in range(20, 30):
    print i
    print testLine('\0' * i)
  close()

  # '\0' * i + '\r' if i < 11
  # '\0' * (i - 11) + '\r' if i >= 11
  # '\0' * (i - 22) + '\r' if i >= 22

  # Seems to use packets of 11 chars

  # All the multi-bytes probably end in \r

if True:

  import time

  open()
  start = time.time()

  for i in range(0, 1):
    
    r = getLine('V1\r')
    print repr(r)
    r = getLine('V2\r')
    print repr(r)
    r = getLine('V3\r')
    print repr(r)
    r = getLine('I1\r') 
    print repr(r)
    r = getLine('I2\r') 
    print repr(r)
    r = getLine('I3\r') 
    print repr(r)
    r = getLine('i1\r') 
    print repr(r)
    r = getLine('i2\r') 
    print repr(r)
    r = getLine('i3\r') 
    print repr(r)
    r = getLine('p1\r') 
    print repr(r)
    r = getLine('p2\r') 
    print repr(r)
    r = getLine('p3\r') 
    print repr(r)
    r = getLine('P1\r') 
    print repr(r)
    r = getLine('P2\r') 
    print repr(r)
    r = getLine('P3\r') 
    print repr(r)

    r = getLine('UA\r')
    print repr(r)
    r = getLine('F\r') 
    print repr(r)
    r = getLine('UV\r') 
    print repr(r)
    r = getLine('UW\r')
    print repr(r)
    r = getLine('S\r')
    print repr(r)
    r = getLine('s\r') 
    print repr(r)
    r = getLine('uA\r') 
  end = time.time()
  close()
  
  print 'Time taken: %0.3f ms\n' % ((end - start) * 1000)

