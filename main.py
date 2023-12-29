import cv2
from cvzone.PoseModule import PoseDetector
import requests
import send
from datetime import datetime
import base64

detector = PoseDetector()
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
l = []
flag = True

key_imgbb = '4fe779be881dda501085a372ba3679cd'

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    imlist, bbox = detector.findPosition(img)

    if len(imlist) > 0:
        print("Human Detected")
        l.append(1)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
        filename = f"intruders/intruder_{timestamp}.jpg"  
        cv2.imwrite(filename, img) 

    if len(l) > 50 and flag:
        flag = False
        send.sendSms()  
        print("Uploading the image...")

        with open(filename, "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": key_imgbb,
                "image": base64.b64encode(file.read()).decode('utf-8'),
            }
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                uploaded_url = response.json()["data"]["url"]
                print("Image uploaded to ImgBB:", uploaded_url)
            else:
                print("Failed to upload image to ImgBB. Error:", response.json())

        flag = False 
        break

    cv2.imshow("Output", img)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
