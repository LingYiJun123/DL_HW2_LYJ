import json
import re
import numpy as np
import cv2
import os
from tqdm import tqdm

fileorderpath = os.path.join('submission_readme', 'answer.txt')

answertxt = open(fileorderpath, "rt")
text_1 = answertxt.read()
fileorder = []
fileorder = re.findall("\"image_id\":\s([-+]?\d*\.*\d+)", text_1, re.DOTALL)
fileorder = list(dict.fromkeys(fileorder))     #print(fileorder[3].type) it is type string

yoloresultpath = "../yolov5/runs/detect/exp9/labels"
imgdir = "./test/test"

result_to_json = []
missingfile = []
for i in tqdm(range(len(fileorder))):
  #print(i)

  yolotxt = os.path.join(yoloresultpath, str(fileorder[i]) + ".txt")
  imgpath = os.path.join(imgdir, str(fileorder[i]) + ".png")
  img = cv2.imread(imgpath) 
  imgheight, imgwidth, _ = img.shape
  

  
  if os.path.isfile(yolotxt):    
   with open(yolotxt, 'r') as f:
     for lines in f:
       labels, x, y, width, height, score = [float(item) for item in lines.split(' ')]
       
       
       cocox = x*imgwidth
       cocoy = y*imgheight
       cocoheight = height*imgheight
       cocowidth = width*imgwidth
       cocox = cocox - (cocowidth/2)
       cocoy = cocoy - (cocoheight/2)
       bbox = [cocox, cocoy, cocowidth, cocoheight]
       
       det_box_info = {}
       det_box_info["image_id"] = int(fileorder[i])
       det_box_info["score"] = score
       det_box_info["category_id"] = int(labels)
       det_box_info["bbox"] = bbox
       
       result_to_json.append(det_box_info)
       
  else:
    det_box_info = {}
    det_box_info["image_id"] = int(fileorder[i])
    det_box_info["score"] = score
    det_box_info["category_id"] = int(labels)
    det_box_info["bbox"] = bbox
       
    result_to_json.append(det_box_info)
    missingfile.append(fileorder[i])
    
print(missingfile)
json_object = json.dumps(result_to_json, indent=4)

with open("answer.json", "w") as outfile:
    outfile.write(json_object)
