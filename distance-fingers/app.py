import cv2 as cv 
import mediapipe as mp
import math , json


mp_drowing = mp.solutions.drawing_utils
hands_mp = mp.solutions.hands
drawing_space = mp_drowing.DrawingSpec(
    thickness = 1 ,
    circle_radius= 1 , 
    color = (0, 0, 255)
)



with open("./setting.json" , "r") as settingfile : 
    setting = json.load(settingfile)


cammer = cv.VideoCapture(0)

points = list(range(0,600))
distance = 0


with hands_mp.Hands( max_num_hands=2, min_detection_confidence=0.5,min_tracking_confidence=0.5) as hand_mesh :
    while True : 
        frame , image = cammer.read()
        img = cv.cvtColor(image , cv.COLOR_BGR2RGB)
        img.flags.writeable = False
        result = hand_mesh.process(img)
        img.flags.writeable = True
        img = cv.cvtColor(img , cv.COLOR_RGB2BGR)
        if result.multi_hand_landmarks:
            index_finger_tip = {}
            for idx , hand_landmark in enumerate(result.multi_hand_landmarks):
                for point in range(0,len(hand_landmark.landmark)):
                    targte = hand_landmark.landmark[point]
                    handtextpotion = hand_landmark.landmark[setting['handlandmark']]
                    h , w , _ = img.shape
                    x , y = int(targte.x * w) , int(targte.y * h)
                    xh , yh = int((handtextpotion.x) * w) , int((handtextpotion.y) * h)
                    index_finger_tip[result.multi_handedness[idx].classification[0].label] = (xh , yh)
                    print("\033c" , end="")
                    print(index_finger_tip)
                    
                    if ("Left" in index_finger_tip) and ("Right" in index_finger_tip ) : 
                        xhl , yhl = index_finger_tip["Left"]
                        xhr , yhr = index_finger_tip['Right']
                        cv.line(img , (xhl , yhl) , (xhr , yhr) , tuple(setting['linecolor']) , 3)
                        distance = math.sqrt((xhl - yhl) ** 2 + (xhr - yhr) ** 2)
                    if setting['draw']:
                        mp_drowing.draw_landmarks(
                            image = img,
                            landmark_list = hand_landmark,
                            connections = hands_mp.FACEMESH_TESSELATION,
                            landmark_drawing_spec = drawing_space,
                            connection_drawing_spec = drawing_space
                        )
                    if setting['lildraw'] :
                        if not point == 8:
                            cv.circle(img, (x, y), 2, tuple(setting['pointcolor']), -1)
                            cv.putText(img, str(point), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    cv.putText(img , str(result.multi_handedness[idx].classification[0].label) , (xh , yh) , cv.FONT_HERSHEY_SIMPLEX, 0.5, tuple(setting['textcolor']), 1)
                    cv.putText(img , f"distance : {distance}" , (10 , 30) , cv.FONT_HERSHEY_SIMPLEX , 1 ,tuple(setting['textcolor']) , 3 )
        cv.imshow(setting['windowname'] ,  img)
        k = cv.waitKey(1)
        if k == ord("q") : 
            break

cammer.release()
cv.destroyAllWindows()
