import rlcompleter, readline
readline.parse_and_bind('tab: complete')
from sys import version
print("Python {} on linux".format(version))
print('Type "help", "copyright", "credits" or "license" for more information.')
