import test

g = test.voice()
print(g)
import os
for root , dir , files in os.walk(r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\.SVG IMAGES'):
    for file in files:
        if file.startswith(g):
            print(os.path.join(root,file))
            #print(final_path)
            
                                  
