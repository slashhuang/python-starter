import os
# process 29093 start...
print('process %s start...'% os.getpid())

pid = os.fork()
if pid == 0:
    print("i'm a child process %s and my parent is %s" % (os.getpid(),os.getppid()))
else:
    print("i %s just created a child process %s" % (os.getpid(), pid))