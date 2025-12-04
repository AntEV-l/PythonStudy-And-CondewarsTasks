
from Topics.dict.Tasks.codeMorze import d

stringInput = input().split(" ")


reversedDict = {v:k for k, v in d.items()}

for i in stringInput:
     if i in reversedDict:
          print(reversedDict.get(i).lower(), end='')