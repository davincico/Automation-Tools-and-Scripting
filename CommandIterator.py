import subprocess
import argparse

#construct the argument parser
parser = argparse.ArgumentParser(description="This tool is to help execute a single command on a list of items in a specified file. ie. ping",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#adding arguments to parser
parser.add_argument("-c", "--command", required=True, help="command to execute")
parser.add_argument("-f", "--file", required=True, help="file with list of items to iterate command execution on")
#assign the parse
args = parser.parse_args()

# ping a server list once (-c 1 flag requires admin priv)
def executeCommand(serverList):
    command = args.command

    resultsList = []

    for server in serverList:
        temporary = subprocess.Popen(
            [command, server], stdout=subprocess.PIPE
    )
        result = str(temporary.communicate())
        resultsList.append(result)

    return resultsList

print("Script is running...\n")

# this will only call if invoked as a script - etc. ./ExecutePing.py
# if other scripts import ExecutePing, this will not execute# https://builtin.com/articles/name-python
if __name__ == '__main__':
    print("""
          
 .---. .-. .-..----.    .---.  .----. .-.   .-..-.   .-.  .--.  .-. .-..----.    .-. .---. .----..----.   .--.  .---.  .----. .----. 
{_   _}| {_} || {_     /  ___}/  {}  \|  `.'  ||  `.'  | / {} \ |  `| || {}  \   | |{_   _}| {_  | {}  } / {} \{_   _}/  {}  \| {}  }
  | |  | { } || {__    \     }\      /| |\ /| || |\ /| |/  /\  \| |\  ||     /   | |  | |  | {__ | .-. \/  /\  \ | |  \      /| .-. \\\
          
  `-'  `-' `-'`----'    `---'  `----' `-' ` `-'`-' ` `-'`-'  `-'`-' `-'`----'    `-'  `-'  `----'`-' `-'`-'  `-' `-'   `----' `-' `-'
          """)
    
    command = args.command
    file = args.file
    serverList = list(open(file))
    for i in range(len(serverList)):
        serverList[i] = serverList[i].strip('\n')

    print("Executing " + str(command) + " for the items list in the file, please wait ... \n " + str(serverList) + "\n")
    resultsList = executeCommand(serverList)
    # print(resultsList)

    ResultCount = 0
    for i in resultsList:
        
        ResultCount = ResultCount + 1
        print("Count: " + str(ResultCount) + " === " + i +"\n")