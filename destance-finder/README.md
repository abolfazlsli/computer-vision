### **🔥 Hand Tracking & Dynamic Circle Drawing 🔥**  
This Python script uses **MediaPipe** and **OpenCV** to detect a hand and dynamically draw a circle whose size adapts based on the distance between two specified hand landmarks. 🚀  

---

## **✨ Features:**  
✅ **Real-time Hand Tracking** 🎯  
✅ **Draws a Line** Between Two Specified Landmarks (e.g., Index Finger & Thumb) ✍️  
✅ **Dynamic Circle Resizing** Based on Finger Distance 🔵  
✅ **Customizable Settings via `setting.json`** 📜  

---

## **⚙️ How It Works?**  
1️⃣ **Captures video** from the webcam 🎥  
2️⃣ **Detects a single hand** using MediaPipe 🤚  
3️⃣ **Extracts two key points** (`point1` & `point2`) from the detected hand 🖐️  
4️⃣ **Calculates the Euclidean distance** between them 📏  
5️⃣ **Dynamically adjusts a circle’s radius** based on this distance 🔄  
6️⃣ **Draws landmarks & lines** (if enabled in settings) 🖊️  

---

## **🔧 How to Customize?**  
Modify **`setting.json`** to change the behavior:  

```json
{
    "draw": false,
    "lildraw": true,
    "pointcolor": [0, 255, 0],
    "windowname": "show distance",
    "point1": 8,
    "point2": 4,
    "linecolor": [0, 255, 0]
}
```

💡 **Explanation of Configurations:**  
- `"point1"` & `"point2"` → Define which hand landmarks are used to calculate distance 📌  
- `"linecolor"` → Color of the line connecting these points 🎨  
- `"lildraw"` → If `true`, draws all detected hand points 🖊️  
- `"windowname"` → Title of the OpenCV window 🖥️  

---

## **🎯 Perfect For:**  
🔥 **Gesture-based UI controls**  
🔥 **Hand movement visualization**  
🔥 **Interactive computer vision applications**  

---

**Press `Q` to exit.** 🛑  


https://github.com/user-attachments/assets/a2700658-5d2e-4dea-9c91-712021d4ea41

