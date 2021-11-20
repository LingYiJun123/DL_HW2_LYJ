# DL_HW2_LYJ

Collab link: https://colab.research.google.com/drive/1LZq1cBZlutuho6HNUHVSbywkJfDly56p?authuser=3#scrollTo=xP3Cp5vYXVYq


# Step by step procedure to recreate answer.json

0.) Requirements, the usual: https://pytorch.org/get-started/locally/

1.) Clone github repo

2.) Download best.pt using google drive link: https://drive.google.com/file/d/1eHOUYUmY-mZlOMl52rjy9xQY4U5Td33B/view?usp=sharing

3.) wget testing images

4.) run command:   python detect.py --source [test image directory] --save-txt  --save-conf --nosave --weights [path to best.pt] --conf 0.05

5.) run makejson.py (change yoloresultpath) to create answer.json. (Oh, before that, download the submission_readme file so the program would know the order of files to do detection)


# Getting best.pt

0.) Refer to https://github.com/ultralytics/yolov5
