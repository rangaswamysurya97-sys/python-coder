import psutil

for process in psutil.process_iter():

    try:
        print(process.pid, process.name())

    except:
        pass
