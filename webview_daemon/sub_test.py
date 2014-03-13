import subprocess
print "sub"
subprocess.Popen('export | grep -i display',shell=True)
