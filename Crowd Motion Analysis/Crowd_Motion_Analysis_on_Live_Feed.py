import cv2
import random

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

list = [0,255]
def ran(list):
    return (list[random.randint(0,len(list)-1)])    

diff1        = cv2.absdiff     (frame1  , frame2)
gray1        = cv2.cvtColor    (diff1   , cv2.COLOR_BGR2GRAY)
blur1        = cv2.GaussianBlur(gray1   , (5,5)             , 0)
_, thresh1   = cv2.threshold   (blur1   , 20                , 255, cv2.THRESH_BINARY)
dilated1     = cv2.dilate      (thresh1 , None              , iterations=3)
contours1, _ = cv2.findContours(dilated1, cv2.RETR_TREE     , cv2.CHAIN_APPROX_SIMPLE)
conare1 = 0
for contour in contours1:
    conare1 = conare1 + cv2.contourArea(contour)

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)  
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)   
    blur = cv2.GaussianBlur(gray, (5,5), 0) 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
    dilated = cv2.dilate(thresh, None, iterations=3)    
    contours, _ = cv2.findContours(dilated,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    conare2 = 0
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) 
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)  
        #cv2.putText(frame1, "Contour Area: {}".format(cv2.contourArea(contour)), (10,90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
        conare2 = conare2 + cv2.contourArea(contour)
    cv2.drawContours(frame1, contours, -1, (ran(list),ran(list),ran(list)), 2)                         
    difference = abs(conare1-conare2)
    conare1 = conare2
        
    if (difference==0): 
        cv2.putText(frame1, "Status: {}".format('No Movement'), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    else:
        cv2.putText(frame1, "Status: {}".format('Movement'   ), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    
    cv2.namedWindow("Crowd Motion Analysis",      cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Crowd Motion Analysis",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Crowd Motion Analysis",frame1)
    
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if(cv2.waitKey(40)==27):        
        break
    
cv2.destroyAllWindows() 
cap.release()       