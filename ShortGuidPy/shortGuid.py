# Works on Linux and on Windows.

import sys
MIN_PYTHON = (3, 7)
assert sys.version_info >= MIN_PYTHON, f"requires Python {'.'.join([str(n) for n in MIN_PYTHON])} or newer"
#
import time

def ConvertFromBase10toBase34(n, vDig, nBase):
	sGuid = ''
	n2 = n
	while (n2 > 0):
		pass
		r = (n2 % nBase)
		#print(r);
		sGuid = (vDig[r] + sGuid)
		n2 = (n2//nBase)
	return sGuid

###main
# usage: 
# python shortGuid.py
# or
# python shortGuid.py 8
# 
# The max resolution is about 12 base34 digits.
# I mostly choose 8
#
nChar = 0
nArgCount = len(sys.argv)
#print(nArgCount);

if (nArgCount > 1):
	nChar = int(sys.argv[1])

#print(nChar);
sDigits = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
vDig = list(sDigits)
nTotalDigitCount = len(sDigits)
#print(nTotalDigitCount);
nNanosec = time.time_ns()
#print(nNanosec);

sGuid = ConvertFromBase10toBase34(nNanosec, vDig, nTotalDigitCount)

if (nChar > 0):
	sGuid = sGuid[0:nChar]
	#print(sGuid)
	#print(len(sGuid))
#
print(sGuid)
#print(len(sGuid))
#
