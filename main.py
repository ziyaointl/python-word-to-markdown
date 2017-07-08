from subprocess import Popen, PIPE
import sys

if len(sys.argv) <= 1 :
    print("Please supply an input file")
    quit()

def callPandoc( directory ) :
    indexOfExtension = directory.rfind(".doc")
    outputFile = directory[:indexOfExtension] + ".md"
    p = Popen(["pandoc", directory, "-s", "-o", outputFile], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if err != b'' :
        print(err)
    else :
        print("Converted " + directory + " to " + outputFile)

callPandoc(sys.argv[1])
