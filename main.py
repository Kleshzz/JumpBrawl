from multiprocessing import Process
import subprocess

def run_script(script_name):
    subprocess.run(['python3', script_name])

files = ['core.py', 'botuser.py', 'antibot.py', 'antiddos.py']

processes = []
for file in files:
    process = Process(target=run_script, args=(file,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()