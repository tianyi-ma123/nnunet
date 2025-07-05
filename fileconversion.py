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

#shutil.copy("dataset.json", f"{DATASET}\\dataset.json")

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

for subtype in ['subtype0', 'subtype1', 'subtype2']:
    for f in glob.glob(f"data\\validation\\{subtype}\\*"):
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

count = 0
for f in glob.glob(f"{DATASET}\\imagesTr\\*"):
    count = count + 1


print(count)  #check for number of training files


dataset_dic = { 
 "channel_names": { 
   "0": "CT" 
   
 }, 
 "labels": {
   "background": 0.0,
   "Pan": 1.0,
   "Lesion": 2.0
 }, 
 "numTraining": count, 
 "file_ending": ".nii.gz",
 "overwrite_image_reader_writer": "SimpleITKIO"  
 }

with open(f"{DATASET}\\dataset.json", 'w') as f:
    json.dump(dataset_dic,f, indent=2, sort_keys=False)


