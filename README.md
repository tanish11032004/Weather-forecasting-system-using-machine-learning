**Weather Prediction GUI using OpenWeatherMap API**

### **Overview:**
This Python program is a **Weather Prediction GUI Application** that fetches real-time weather data from the **OpenWeatherMap API**. The application provides weather details such as temperature, humidity, and description based on the user's input (city name). The GUI is built using **Tkinter**, and the weather data is retrieved using the **Requests** library. 

The program also includes a function to load **machine learning models** (though unused in this version), indicating a possible extension of the project to predict weather trends.

---

### **Working of the Program:**
1. The user enters the city name in the input field of the GUI.
2. When the "Fetch Weather" button is clicked, the program sends a request to the **OpenWeatherMap API**.
3. The API responds with weather data such as **temperature, humidity, and weather description**.
4. The fetched data is displayed on the GUI.
5. If an invalid city name is entered or the API request fails, an error message is shown.

---

### **Libraries Used:**
1. **requests** - To fetch data from the API.
2. **pandas & numpy** - Imported but not used (can be useful for data analysis in extended versions).
3. **os** - To check if a file (ML model) exists.
4. **joblib** - To load pre-trained machine learning models.
5. **tkinter** - To create the graphical user interface.
6. **sklearn** - Imported but not used (useful for machine learning model integration).

---

### **Key Functions Explained:**

#### **1. `get_current_weather(city)`**
- Takes a **city name** as input.
- Sends a **GET request** to the OpenWeatherMap API.
- Extracts **weather details** (temperature, humidity, description, etc.).
- Returns the extracted data as a **dictionary**.
- If the request fails, it returns an error message.

#### **2. `load_model(filename)`**
- Checks if a saved machine learning model file exists.
- Loads the model using `joblib` if the file is found.
- Returns `None` if no model file is found.

#### **3. `fetch_weather()`**
- Gets the city name entered by the user.
- Calls `get_current_weather(city)` to retrieve weather details.
- Displays the fetched weather data on the GUI.
- Shows an error message if no city is entered or if the API request fails.

---

### **Graphical User Interface (GUI) Implementation:**
- **`Tk()`**: Initializes the main window.
- **Label & Entry Field**: Allows users to input the city name.
- **Button (`Fetch Weather`)**: Calls `fetch_weather()` when clicked.
- **Output Label**: Displays the weather details retrieved from the API.
- **`mainloop()`**: Keeps the GUI running until the user closes it.

---

### **Example Output:**
If the user enters "Mumbai," the output might be:
```
City: Mumbai, IN
Temperature: 30°C (Feels like 32°C)
Min Temp: 28°C, Max Temp: 32°C
Humidity: 70%
Description: Clear sky
```

If an incorrect city is entered:
```
Error: Failed to fetch weather data for XYZ. Status Code: 404
```

---

### **How to Run the Code:**

#### **Prerequisites:**
- Install Python (if not already installed).
- Install required libraries using the following command:
  ```bash
  pip install requests joblib tkinter
  ```
- Obtain an **API key** from [OpenWeatherMap](https://openweathermap.org/api) and replace `API_KEY` in the script.

#### **Running the Program:**
1. Save the script as `weather_gui.py`.
2. Open a terminal or command prompt in the same directory.
3. Run the following command:
   ```bash
   python weather_gui.py
   ```
4. The **Weather Prediction GUI** window will open.
5. Enter a city name and click "Fetch Weather" to see the results.

---

### **Possible Improvements:**
1. **Remove Unused Imports**: `pandas`, `numpy`, `sklearn` can be removed unless required.
2. **Exception Handling**: Use `try-except` blocks for API requests to handle unexpected errors.
3. **GUI Enhancements**:
   - Improve layout (use frames, colors, fonts for better UI).
   - Add an option to choose between Celsius and Fahrenheit.
4. **Cache Results**: Store recently searched cities to reduce API calls.
5. **ML Model Integration**: Use machine learning to predict future weather trends.

---

### **Conclusion:**
This program effectively demonstrates how to **fetch real-time weather data** and display it in a **user-friendly GUI**. With additional improvements, it can be expanded into a **more advanced weather prediction system** using machine learning.

---

