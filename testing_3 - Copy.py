from sys import argv
#color=input('enter the color:')
color=argv[1]
print('stop') if color=='red'  else print('go slow') if color=='green' else print('cool')