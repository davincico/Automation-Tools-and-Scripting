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

# execute command given on every item in the list in the file
def executeCommand(ListItems):
    command = args.command

    resultsList = []

    for item in ListItems:
        temporary = subprocess.Popen(
            [command, item], stdout=subprocess.PIPE
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
    ListItems = list(open(file))
    for i in range(len(ListItems)):
        ListItems[i] = ListItems[i].strip('\n')

    print("Executing " + str(command) + " for the items list in the file, please wait ... \n " + str(ListItems) + "\n")
    resultsList = executeCommand(ListItems)
    # print(resultsList)

    ResultCount = 0
    for i in resultsList:
        
        ResultCount = ResultCount + 1
        print("Count: " + str(ResultCount) + " === " + i +"\n")
