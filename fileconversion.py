import os
import shutil
import json
import glob

DATASET = "nnUNet_raw\\Dataset001_Pan"

for folder in [
    "nnUNet_results",
    "nnUNet_preprocessed",
    f"{DATASET}\\imagesTr",
    f"{DATASET}\\imagesTs",
    f"{DATASET}\\labelsTr",]:
    os.makedirs(folder, exist_ok=True)

shutil.copy("dataset.json", f"{DATASET}\\dataset.json")

for subtype in ['subtype0', 'subtype1', 'subtype2']:
    for f in glob.glob(f"data\\train\\{subtype}\\*"):
        filename = f.split("\\")[-1]

        if "_0000" in f:
            dest = "imagesTr"
        else:
            dest = "labelsTr"
        source = f
        dest = os.path.join(f"{DATASET}\\{dest}",filename)
        #print(f"Moving {source} to {dest}")
        shutil.copy(source, dest)

for f in glob.glob(f"data\\test\\*"):
    filename = f.split("\\")[-1]
    dest = os.path.join(f"{DATASET}\\imagesTs",filename)
    #print(f"moving {f} to {dest}")
    shutil.copy(f,dest)
