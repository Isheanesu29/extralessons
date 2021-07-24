

# f = open('dir_exception/textfiles.txt','r')
# print(f.read())
# f.close()

# try:
#     f = open('dir_exception/textfiles.txt','r')
#     print(f.read())
#     f.close()
# except Exception as e:
#     print(e)

# try:
#     f = open('dir_exception/textfiles.txt','r')
#     print(f.read())
#     f.close()
# except FileNotFoundError as e:
#     print('Please check your file path')
    
try:
    f = open('dir_exception/textfile.txts','r')
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print('Please check your file path')
finally:
    f.close()