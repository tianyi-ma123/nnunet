import os
import shutil
import json
import glob

# from train/subtype0, train/subtype1, train/subtype2
# move anything that contains _0000 into imagesTr
# move rest into labelsTr


for subtype in ['subtype0', 'subtype1', 'subtype2']:
    for f in glob.glob(f"data\\train\\{subtype}\\*"):
        filename = f.split("\\")[-1]

        if "_0000" in f:
            dest = "imagesTr"
        else:
            dest = "labelsTr"
        

        source = f
        dest = os.path.join(f"nnUNet_raw\\{dest}",filename)
        
        #print(f"Moving {source} to {dest}")
        #shutil.copy(source, dest)


for f in glob.glob(f"data\\test\\*"):
    filename = f.split("\\")[-1]
    dest = os.path.join("nnUNet_raw\\imagesTs",filename)
    #print(f"moving {f} to {dest}")
    shutil.copy(f,dest)
