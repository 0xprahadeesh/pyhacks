import subprocess
subprocess.call("if config eth0 down", shell=True, check=True)
subprocess.call("if config eth0 hw 00:65:55:44:33:22", shell=True, check=True)
subprocess.call("if config eth0 up", shell=True, check=True)