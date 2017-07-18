from subprocess import Popen, PIPE
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys, time, os

if len(sys.argv) <= 1:
    print("Please supply an input file")
    quit()

inputFile = sys.argv[1]
directory = os.path.dirname(inputFile)

def callPandoc( inputFile ):
    indexOfExtension = inputFile.rfind(".doc")
    outputFile = inputFile[:indexOfExtension] + ".md"
    p = Popen(["pandoc", inputFile, "-s", "-o", outputFile, "--wrap=preserve"], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if err != b'' :
        print(err)
    else :
        print("Converted " + inputFile + " to " + outputFile)

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == inputFile:
            callPandoc(inputFile)

eventHandler = Handler()
observer = Observer()
observer.schedule(eventHandler, path=directory, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print()
observer.join()
