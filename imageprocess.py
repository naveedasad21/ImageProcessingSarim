import cv2
import os 
import sys
def canny_img_det():
    img = cv2.imread("news.jpg")
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image,(7,7), 0)
    cv2.imshow("Originall", img)
    cv2.waitKey(0)
    canny = cv2.Canny(blurred_image, 10, 30)
    cv2.imshow("Canny with low thresholds", canny)
    cv2.waitKey(0)
    canny2 = cv2.Canny(blurred_image,50,150)
    cv2.imshow("Canny with high thresholds", canny2)
    cv2.waitKey(0)

def face_rec_multi(): 
    img = cv2.imread("news.jpg")
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 
                                          scaleFactor=1.5, 
                                          minNeighbors=5)
    print(faces)
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,255),3)
        cv2.imshow("Gray",img)
        cv2.waitKey(0)
def face_rec(): 
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread("photo.jpg")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 
                                          scaleFactor= 1.05, 
                                          minNeighbors=5)
    print(faces)
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,255),3)
        cv2.imshow("Gray",img)
        cv2.waitKey(0)


def read_images_directory():
    folder = "sample-images"
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        print (img)
        if img is not None:
            print(filename)
            resize_img  = cv2.resize(img,(100,100))
            
            cv2.imwrite(filename.replace(".jpg", "_resize.jpg"), resize_img)
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            print(filename)
            
    
img  = cv2.imread("galaxy.jpg", 0)
#read_images_directory()
#face_rec()
#face_rec_multi()
canny_img_det()
print(img)
print(img.shape)