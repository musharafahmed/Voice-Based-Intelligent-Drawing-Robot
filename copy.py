import test2
import os
import shutil
emp=os.listdir(r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\talha')
destination = r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\talha'
print(emp)
if len(emp)==0:
   dest=shutil.copy(final_path,destination)
else:
    shutil.rmtree('talha')
    os.makedirs('talha')
    dest=shutil.copy(final_path,destination)
    

