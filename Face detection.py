'''
All of your implementation should be in this file.
'''
'''
This is the only .py file you need to submit. 
'''
'''
    Please do not use cv2.imwrite() and cv2.imshow() in this function.
    If you want to show an image for debugging, please use show_image() function in helper.py.
    Please do not save any intermediate files in your final submission.
'''
from helper import show_image

import cv2
import numpy as np
import os
import sys
import glob
import face_recognition
from sklearn.cluster import KMeans


'''
Please do NOT add any imports. The allowed libraries are already imported for you.
'''


def detect_faces(input_path: str) -> dict:
    result_list = []
    '''
    Your implementation.
    '''
    detector=cv2.CascadeClassifier('frontalface.xml')
    for k in glob.glob(input_path+'/*'):
        top = os.path.basename(k)
        image = cv2.imread(k)
        bounding_boxes = detector.detectMultiScale(image = image, scaleFactor = 1.1, minNeighbors = 6)
        i = 0
        while(i < len(bounding_boxes)):
            boundary_box = list()
            for j in list(bounding_boxes[i]):
                boundary_box.append(int(j))
            dic = dict(iname = top, bbox = boundary_box)
            result_list.append(dic)
            i = i+1
    return result_list


'''
K: number of clusters
# '''
def cluster_faces(input_path: str, K: int) -> dict:
    list_of_img = list()
    result_list = list()
    top_list = list()
    list_of_dimension = list()
    '''
    Your implementation.
    '''
    detector = cv2.CascadeClassifier('frontalface.xml')
    for z in glob.glob(input_path + '/*'):
        top_list.append(os.path.basename(z))
        read_img = cv2.imread(z)
        list_of_img.append(read_img)
        bbox = list(detector.detectMultiScale(image = read_img, scaleFactor = 1.1, minNeighbors = 6)[0])
        j = 0
        while (j < len(bbox)):
            bbox[j] = int(bbox[j])
            j = j + 1
        a, b, c, d = bbox
        cut_image = read_img[b:b + d, a:a + c]
        list_of_dimension.append(face_recognition.face_encodings(cut_image)[0])

    clusters = int(K)
    clustered = KMeans(n_clusters = clusters, random_state = 0).fit(list_of_dimension)
    ret = clustered.labels_
    i = 0
    while (i < clusters):
        images_cal = list()
        j = 0
        while (j < len(ret)):
            if i == ret[j]:
                images_cal.append(top_list[j])
            j = j + 1
        d = dict(cluster_no=i, elements=images_cal)
        result_list.append(d)
        i = i + 1
    return result_list


'''
If you want to write your implementation in multiple functions, you can write them here. 
But remember the above 2 functions are the only functions that will be called by FaceCluster.py and FaceDetector.py.
'''

"""
Your implementation of other functions (if needed).
"""


