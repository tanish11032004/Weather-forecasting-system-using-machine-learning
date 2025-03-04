# Import necessary libraries
import requests  # For making API requests
import pandas as pd  # For data handling (not used in this code)
import numpy as np  # For numerical operations (not used in this code)
import os  # For file handling
import joblib  # For loading ML models
import tkinter as tk  # For GUI development
from tkinter import messagebox  # For displaying error messages
from sklearn.model_selection import train_test_split  # ML-related (not used here)
from sklearn.preprocessing import LabelEncoder  # ML-related (not used here)
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor  # ML models (not used here)
from sklearn.metrics import mean_squared_error  # For evaluating ML models (not used here)

# API Configuration
API_KEY = '9f39358739a87c32ca64c4a33f26f292'  # Replace with your actual API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/'

def get_current_weather(city):
    """
    Fetches current weather data for a given city using OpenWeatherMap API.
    
    Parameters:
    city (str): The name of the city to fetch weather for.
    
    Returns:
    dict: A dictionary containing weather details such as temperature, humidity, and description.
    """
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch weather data for {city}. Status Code: {response.status_code}"}
    
    data = response.json()
    return {
        'city': data.get('name', 'Unknown'),
        'current_temp': round(data.get('main', {}).get('temp', 0)),  # Current temperature
        'feels_like': round(data.get('main', {}).get('feels_like', 0)),  # Feels-like temperature
        'temp_min': round(data.get('main', {}).get('temp_min', 0)),  # Minimum temperature
        'temp_max': round(data.get('main', {}).get('temp_max', 0)),  # Maximum temperature
        'humidity': round(data.get('main', {}).get('humidity', 0)),  # Humidity percentage
        'description': data.get('weather', [{}])[0].get('description', 'No description'),  # Weather description
        'country': data.get('sys', {}).get('country', 'Unknown')  # Country code
    }

def load_model(filename):
    """
    Loads a pre-trained machine learning model from a file if it exists.
    
    Parameters:
    filename (str): Path to the saved model file.
    
    Returns:
    model: Loaded model or None if the file does not exist.
    """
    if os.path.exists(filename):
        return joblib.load(filename)
    return None

def fetch_weather():
    """
    Fetches weather information based on user input and displays it in the GUI.
    """
    city = city_entry.get()  # Get city name from the user input field
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")  # Show error if input is empty
        return
    
    weather_data = get_current_weather(city)  # Fetch weather data from API
    if "error" in weather_data:
        messagebox.showerror("Error", weather_data['error'])  # Show error if API request fails
        return
    
    # Format and display weather data in the GUI
    output_text.set(f"City: {weather_data['city']}, {weather_data['country']}\n"
                    f"Temperature: {weather_data['current_temp']}°C (Feels like {weather_data['feels_like']}°C)\n"
                    f"Min Temp: {weather_data['temp_min']}°C, Max Temp: {weather_data['temp_max']}°C\n"
                    f"Humidity: {weather_data['humidity']}%\n"
                    f"Description: {weather_data['description']}")

# GUI Setup
root = tk.Tk()
root.title("Weather Prediction GUI")  # Set window title
root.geometry("400x400")  # Set window size

# Label for entering city name
label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
label.pack(pady=5)

# Entry field for user to input city name
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

# Button to fetch weather data
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, font=("Arial", 12))
fetch_button.pack(pady=10)

# Label to display weather information
output_text = tk.StringVar()  # Variable to hold output text
output_label = tk.Label(root, textvariable=output_text, font=("Arial", 12), wraplength=350, justify="left")
output_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
