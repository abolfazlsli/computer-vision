import mediapipe as mp 
import cv2 as cv
import json , math



with open("./setting.json" , "r") as file : 
    setting = json.load(file)






mp_drawing = mp.solutions.drawing_utils
hand_mp = mp.solutions.hands


camera = cv.VideoCapture(0)


with hand_mp.Hands(max_num_hands=1 , min_detection_confidence = 0.5 , min_tracking_confidence = 0.5) as hand_mesh:
    while True :
        frame, image = camera.read()
        img = cv.cvtColor(image , cv.COLOR_BGR2RGB)
        img.flags.writeable = False
        res = hand_mesh.process(img)
        img.flags.writeable = True
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        if res.multi_hand_landmarks:
            h , w , _ = img.shape
            for hand_landmark in res.multi_hand_landmarks:
                point1 = hand_landmark.landmark[setting['point1']]
                point2 = hand_landmark.landmark[setting['point2']]
                cv.line(img , (int(point1.x * w) , int(point1.y * h)) , (int(point2.x * w) ,int(point2.y * h)) , tuple(setting['linecolor']) , 3)
                distance = math.sqrt((int(point1.x * w) - int(point2.x * w)) **2 + (int(point1.y * h) - int(point2.y * h)) **2)
                rad = int(distance / 2)
                fcenterx , fcentery = (int(point1.x * w) + int(point2.x * w)) // 2 , (int(point1.y * h) + int(point2.y * h)) // 2
                cv.circle(img , (150 , 250) , rad , (0 , 255 ,0 ) , -1)
                print((point1.x , point1.y) , (point2.y , point2.x) )
                if setting['lildraw'] : 
                    for point in range(0 , len(hand_landmark.landmark)):
                        target = hand_landmark.landmark[point]
                        x , y = int(target.x * w) , int(target.y * h)
                        cv.circle(img , (x, y), 2 , tuple(setting['pointcolor']) , -1)
                    cv.putText(img, str(distance), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv.imshow(setting['windowname'] , img)
        k = cv.waitKey(1)
        if ord("q") == k:
            break





camera.release()
cv.destroyAllWindows()




