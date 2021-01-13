import subprocess
subprocess.call("if config eth0 down", shell=True)
subprocess.call("if config eth0 hw ether 00:65:55:44:33:22", shell=True)
subprocess.call("if config eth0 up", shell=True)
