import subprocess

cmd = '/opt/splunk/etc/apps/tested_app/bin/tg_app/bin/python3 /opt/splunk/etc/apps/tested_app/bin/teleg_app.py'


py_pipe = subprocess.Popen(cmd,subprocess.PIPE, shell=True)

out, err = py_pipe.communicate()
print(out, err)
