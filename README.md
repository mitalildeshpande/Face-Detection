# Face-Detection

In this project I have detected faces present in a corpus of images using the face detection algorithm available in OpenCV library. I tried using two libraries Face Recognition and Harr Cascade. The Face Recognition library gave an accuracy of 45.1 % but the Harr Cascade performed extremely well and provided an accuracy of 78.91 %. A funtion is used to detect this and then it gives the co-ordinates of the bounding box of the faces that are detected. Then, the image co-ordinate of every bounding box along with the image name is sent to a dictionary and which is then appended to a list.

# Face clustering

The co-ordinates of the bounding box of the faces detected are now used to crop the part of the image which has a face. The cropped image is being sent to a cluster function. This function provides us with a vector of cropped images and is then appended in a list of dimensions. The list of dimensions is now sent to the clustering algorithm like k-means for creation of clusters which are created based on the similarity of vectors. K-means provides labels for images and on the basis of these labels the images are grouped.
