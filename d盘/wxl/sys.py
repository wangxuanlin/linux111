# import getopt
# import sys
#
#
# try:
#     opts,args =getopt.getopt(sys.argv[1:],'h:p:t', [])
#     print(opts)
#     print(args)
# except Exception as a:
#     print(a)




import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-h', type=str)
ap.add_argument("-p", type=int, action='append')