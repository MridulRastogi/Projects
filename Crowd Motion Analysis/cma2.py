import cv2
import numpy as np
import time
import random

cap = cv2.VideoCapture('d:/Python Inputs/vtest2.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()
'''
list = [[0,255,0],      #Green
        [255,0,0],      #Red
        [0,0,255],      #Blue
        [255,255,0],    #Yellow
        [255,0,255],    #Pink
        [0,255,255],    #Cyan
        [255,255,255]   #White
        ]
'''
list = [0,255]
def ran(list):
    return (list[random.randint(0,len(list)-1)])    

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)   #no this difference is going to be converted to grayscale mode
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)   
    blur = cv2.GaussianBlur(gray, (5,5), 0) #FP=gray, SP=Kernel Size, TP=Sigma X value which is 0 over here
        
    #finding the threshold
    # FP=Source Image(blur), SP=Threshold Value(20), TP=Maximum Threshold Value(255), FP=TYPE(cv2.THRESH_BINARY)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
    
    # Dilate the thresholded image to fill all the holes
    #FP=threshold version of the image, SP=Kernel Size(none), TP=Number of iterations(3)
    dilated = cv2.dilate(thresh, None, iterations=3)    
    
    # A contour is a curve joining all the continous points with the same colour intensity along the boundary.
    # Contour method is going to give two results: one is contours and the other is hierarchy
    # FP=threshold image(dilated), SP=mode(cv2.RETR_TREE, TP=method(cv2.CHAIN_APPROX_SIMPLE))
    contours, _ = cv2.findContours(dilated,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #FP=original frame(frame1), SP=contour(contours), TP=contourID(-1), FP=color((0,255,0)), FP=thickness(2)
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)                     
    # But we won't do this because we want rectangles so:
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) # Thus now we are finding the height, width, x and y coordinate of the 
                                                # contours from the image
        #ts2 = int(time.time_ns())
        #if(ts2%500==0):
        #   cv2.putText(frame1, "Contour Area: {}".format(cv2.contourArea(contour)), (10,90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)                                            
        if (cv2.contourArea(contour) < 700):
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,150,0), 2)  #(ran(list),ran(list),ran(list))
        if (cv2.contourArea(contour) < 3000 and cv2.contourArea(contour)>=0): 
            cv2.putText(frame1, "Status: {}".format('No Movement'), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        else:
            cv2.putText(frame1, "Status: {}".format('Movement'   ), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
        
    cv2.imshow("Crowd Motion Analysis",frame1)
    #Now we are going to assign the value of frame2 into frame1
    frame1 = frame2
    ret, frame2 = cap.read()
    
    # Here waitKey is the keyboard binding function which takes the input time for which we have to show the image window
    # It takes input in miliseconds, if the input given is 0 miliseconds then the window won't close until the cross button is clicked.
    # Here 27 is the ascii code for ESC key which will close the window  and the the value in waitKey(value) is for the amount of time 
    # for which the frame will be displayed
    if(cv2.waitKey(40)==27):        
        break
    
cv2.destroyAllWindows() # This simply destroy all windows created using the current running python code
cap.release()