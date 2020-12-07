import sys

if len(sys.argv)==2:
    print(sys.argv[1])

else:
    sys.stderr.write("Usage: {} <anything>".format(sys.argv[0]))
