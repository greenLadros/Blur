#ivri korem 2020
'''
This script will go through given image and detect and blur the plate in there
'''

#init
#import
import cv2 
import numpy as np
import sys

# if script syntax is wrong or no params given
if len(sys.argv) < 4 or len(sys.argv) > 5:
    print('''
    ██████╗░██╗░░░░░██╗░░░██╗██████╗░
    ██╔══██╗██║░░░░░██║░░░██║██╔══██╗
    ██████╦╝██║░░░░░██║░░░██║██████╔╝
    ██╔══██╗██║░░░░░██║░░░██║██╔══██╗
    ██████╦╝███████╗╚██████╔╝██║░░██║
    ╚═════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝

    + blur is a script that detects target in an image and blurs it
    + Syntax: /blur.py <target> <img> <path> *(optional)<cascade>
    + target - plate/face/text/badge/custom (if custom just fill the path to an xml file with cascade data)
    + img - the target image path
    + path - the path of were to save the result image
    ''')
    quit()
else:
    #saving input into vars
    target = sys.argv[1]
    filename = sys.argv[3]
    try:
        img = cv2.imread(sys.argv[2])
    except:
        print('Error: <image> is invalid')

if target == 'plate':
    #create cascade
    plateCascade = cv2.CascadeClassifier(r"C:\Users\USER\Desktop\DataScience\Blur\plate_cascade.xml")

    #detecting and blurring
    platesDetected = plateCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    result = img.copy()

    for (x,y,width,height) in platesDetected:
        #define roi and blur it
        roi = img[y:y+height,x:x+width]
        roi = cv2.blur(roi, (5,5))
        result[y:y+height,x:x+width] = roi

    #save the result
    cv2.imwrite(filename, result)
    cv2.imshow("result", result)

elif target == 'face':
    #create cascade
    faceCascade = cv2.CascadeClassifier(r"C:\Users\USER\Desktop\DataScience\Blur\haarcascade_frontalface_alt.xml")

    #detecting and blurring
    facesDetected = faceCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)
    result = img.copy()

    for (x,y,width,height) in facesDetected:
        #define roi and blur it
        roi = img[y:y+height,x:x+width]
        roi = cv2.blur(roi, (5,5))
        result[y:y+height,x:x+width] = roi

    #save the result
    cv2.imwrite(filename, result)
    cv2.imshow("result", result)

elif target == 'text':
    pass

elif target == 'badge':
    pass

elif target == 'custom':
    try:
        #create cascade
        objectCascade = cv2.CascadeClassifier(sys.argv[4])
    except:
        print('faild to load custom cascade')

    #detecting and blurring
    objectsDetected = objectCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbor=3)
    result = img.copy()

    for (x,y,width,height) in objectsDetected:
        #define roi and blur it
        roi = img[y:y+height,x:x+width]
        roi = cv2.blur(roi, (5,5))
        result[y:y+height,x:x+width] = roi

    #save the result
    cv2.imwrite(filename, result)
    cv2.imshow("result", result)

else:
    print('Error: <target> is invalid')

#closing all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
quit()