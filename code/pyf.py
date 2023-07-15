import cv2
import os
import time
import imutils
import pytesseract
from PIL import Image

# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\HARSHAVA-B024DC\\Downloads\\WhatsApp Video 2022-12-21 at 1.40.12 AM.mp4")


try:
      
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
 
# frame
currentframe = 0
i=0
while(True):

    # reading from frame
    ret,frame = cam.read()
   # how much you spent on calling functions above
   
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        # if video is still left continue creating images
        if (currentframe==30*i):
            cv2.imwrite(name, frame)
            i=i+1
            
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1

    
    
    else:
        break

img=Image.open("C:\\Users\\HARSHAVA-B024DC\\Desktop\\s.hackathon\\data\\frame300.jpg")
b=(0,0,500,700)
c_i=img.crop(box=b)
b=(320,470,600,700)
c_i=img.crop(box=b)
c_i.show()


# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\HARSHAVA-B024DC\\AppData\\Local\\Programs\\Python\\Python310'
image = cv2.imread('C:\\Users\\HARSHAVA-B024DC\\Desktop\\s.hackathon\\p.jpg')
image = imutils.resize(image, width=300 )
cv2.imshow("original image", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
cv2.waitKey(0)
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17) 
cv2.imshow("smoothened image", gray_image)
cv2.waitKey(0)
edged = cv2.Canny(gray_image, 30, 200) 
cv2.imshow("edged image", edged)
cv2.waitKey(0)
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)
cv2.waitKey(0)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
screenCnt = None
image2 = image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
cv2.waitKey(0)
i=7
for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
                screenCnt = approx
        x,y,w,h = cv2.boundingRect(c) 
        new_img=image[y:y+h,x:x+w]
        cv2.imwrite('./'+str(i)+'.png',new_img)
        i+=1
        break

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)
Cropped_loc = './7.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
#print("Number plate is:", plate)
cv2.waitKey(0)
cv2.destroyAllWindows()


