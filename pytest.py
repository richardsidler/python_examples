import sys
if sys.version_info < (2, 4):
    raise "must use python 2.5 or greater"
else:
    # syntax error in 2.4, ok in 2.5
    x = 1 if True else 2
    print x