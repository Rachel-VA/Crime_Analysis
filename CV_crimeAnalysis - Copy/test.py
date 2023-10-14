from deepface import DeepFace

import pandas as pd #to create AI label dataset for images
import os #for working w/ files

input_dir = "C:\dataIMG"
target_image = "Ivan.jpg"

data = {
    "Name": [],
    "Age": [], #empty list of age
    "Gender": [],
    "Race": []      
}


image_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.jpg')]



for image_file in image_files:
    result = DeepFace.verify(target_image, image_file)
    if result['verified']:
        print("MATCHED IMAGE FOUND: ",f"{image_file} matches the identity of {target_image}")
        matched = result['verified']
        
        print("HERE IS THE IMAGE MATCHED of : ",f"{image_file} matches the identity of {target_image}")
        
        if result['verified'] and matched:
            print("HERE IS THE IMAGE MATCHED of : ",f"{image_file} matches the identity of {target_image}")
            
            print("Name: ",target_image.split(".")[0])       
            #data["Name"].append(target_image.split(".")[0], f"{image_file} name is mached of {target_image}")                      
        
print("matched IMAGE FOUND: ",matched)

# df = pd.DataFrame(data) 
# print("SHOW DF DATA HERE: ",df)

print("\n\n\n\n\n")