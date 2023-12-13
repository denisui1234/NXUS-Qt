
print("Starting NXUS...")
import os
print ("Finished loading modules!")
print("Working in: " + os.getcwd())
path = "NXUS-Rev"
os.chdir(path)
with open("nxus.py") as f:
    exec(f.read())