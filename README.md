
---

### **README.md**

# Hand Distance Detector  

This Python script uses **OpenCV** and **MediaPipe** to detect hands and measure the distance between the index fingertips of the left and right hands. It also provides visualization options such as drawing landmarks, showing hand labels, and displaying distances in real time.

## **Requirements**
Make sure you have the following libraries installed before running the script:

```bash
pip install opencv-python mediapipe
```

## **How It Works**
1. The script accesses the webcam using `cv.VideoCapture(0)`.
2. It processes the video feed to detect hands using **MediaPipe Hands**.
3. If two hands are detected, it finds the **index fingertip landmark (point 8)** for both.
4. It calculates the **Euclidean distance** between the index fingertips.
5. The distance is displayed on the screen, and a **line is drawn** between the two fingertips.
6. Additional visual elements can be enabled/disabled using the `setting.json` file.

## **Settings (`setting.json`)**
The script loads configuration settings from a JSON file. Below is an example:

```json
{
    "handlandmark": 8,
    "lildraw": false,
    "draw": false,
    "linecolor": [0, 255, 0],
    "textcolor": [0, 255, 0],
    "pointcolor": [0, 0, 255],
    "windowname": "distance detector"
}
```

### **Explanation of Settings:**
| Key           | Type    | Description |
|--------------|--------|-------------|
| `handlandmark` | `int` | The landmark index to track (default: 8, index fingertip). |
| `lildraw`    | `bool`  | If `true`, draws small circles on each hand landmark. |
| `draw`       | `bool`  | If `true`, draws hand landmarks using **MediaPipe's** built-in drawing utility. |
| `linecolor`  | `[R, G, B]` | Color of the line connecting fingertips. |
| `textcolor`  | `[R, G, B]` | Color of the displayed text. |
| `pointcolor` | `[R, G, B]` | Color of small circles drawn on hand landmarks. |
| `windowname` | `str` | The name of the OpenCV window. |

## **How to Run**
1. Make sure the `setting.json` file is in the same directory as the script.
2. Run the script:

   ```bash
   python hand_distance_detector.py
   ```
3. Press **'Q'** to exit the program.

---

## **Out put ** : 



https://github.com/user-attachments/assets/cf947c02-6848-4953-b737-d097f00097a9



