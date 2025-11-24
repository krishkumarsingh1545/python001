import os
path = input("Enter path: ")
print(os.system(f"cd {path} && dir"))
