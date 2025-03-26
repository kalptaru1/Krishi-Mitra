<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Free Weather API (OpenWeatherMap)
WEATHER_API_KEY = "b03b6419bffb6e462b76ebf6611e3231"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home():
    language = request.form['language']
    return render_template('home.html', language=language)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/loan')
def loan():
    return render_template('loan.html')

# Get Weather Data (Using OpenWeatherMap API)
@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Delhi')  # Default city
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(WEATHER_API_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"})
    
    data = response.json()
    if "list" in data:
        forecast_data = []
        for i in range(0, min(len(data["list"]), 30), 8):  # Simulating 30-day forecast
            weather_info = data["list"][i]
            forecast = {
                "date": weather_info.get("dt_txt", "N/A"),
                "temperature": weather_info.get("main", {}).get("temp", "N/A"),
                "description": weather_info.get("weather", [{}])[0].get("description", "N/A"),
                "humidity": weather_info.get("main", {}).get("humidity", "N/A"),
                "wind_speed": weather_info.get("wind", {}).get("speed", "N/A")
            }
            forecast_data.append(forecast)
        return jsonify({"forecast": forecast_data})
    return jsonify({"error": "Weather data not found"})

# Enhanced Loan Calculation using Land Area and Crop Type
CROP_YIELD = {  # Estimated yield per hectare (kg/ha)
    "wheat": 3000,
    "rice": 4000,
    "maize": 3500,
    "sugarcane": 60000
}
CROP_PRICE = {  # Price per kg in INR
    "wheat": 22,
    "rice": 25,
    "maize": 18,
    "sugarcane": 3
}

@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    try:
        land_area = float(request.form['land_area'])  # in hectares
        crop_type = request.form['crop_type'].lower()
        
        if crop_type not in CROP_YIELD:
            return jsonify({"error": "Invalid crop type"})
        
        yield_amount = land_area * CROP_YIELD[crop_type]  # Calculate total yield
        income = yield_amount * CROP_PRICE[crop_type]  # Calculate income
        loan_amount = income * 0.6  # Loan is 60% of total income
        
        return jsonify({"yield": yield_amount, "income": income, "loan": loan_amount})
    except ValueError:
        return jsonify({"error": "Invalid input"})

# Free Translation API (Google Translate without API Key)
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_lang = request.form['lang']
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
    response = requests.get(url)
    translated_text = response.json()[0][0][0]
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Free Weather API (OpenWeatherMap)
WEATHER_API_KEY = "b03b6419bffb6e462b76ebf6611e3231"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home():
    language = request.form['language']
    return render_template('home.html', language=language)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/loan')
def loan():
    return render_template('loan.html')

# Get Weather Data (Using OpenWeatherMap API)
@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Delhi')  # Default city
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(WEATHER_API_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"})
    
    data = response.json()
    if "list" in data:
        forecast_data = []
        for i in range(0, min(len(data["list"]), 30), 8):  # Simulating 30-day forecast
            weather_info = data["list"][i]
            forecast = {
                "date": weather_info.get("dt_txt", "N/A"),
                "temperature": weather_info.get("main", {}).get("temp", "N/A"),
                "description": weather_info.get("weather", [{}])[0].get("description", "N/A"),
                "humidity": weather_info.get("main", {}).get("humidity", "N/A"),
                "wind_speed": weather_info.get("wind", {}).get("speed", "N/A")
            }
            forecast_data.append(forecast)
        return jsonify({"forecast": forecast_data})
    return jsonify({"error": "Weather data not found"})

# Enhanced Loan Calculation using Land Area and Crop Type
CROP_YIELD = {  # Estimated yield per hectare (kg/ha)
    "wheat": 3000,
    "rice": 4000,
    "maize": 3500,
    "sugarcane": 60000
}
CROP_PRICE = {  # Price per kg in INR
    "wheat": 22,
    "rice": 25,
    "maize": 18,
    "sugarcane": 3
}

@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    try:
        land_area = float(request.form['land_area'])  # in hectares
        crop_type = request.form['crop_type'].lower()
        
        if crop_type not in CROP_YIELD:
            return jsonify({"error": "Invalid crop type"})
        
        yield_amount = land_area * CROP_YIELD[crop_type]  # Calculate total yield
        income = yield_amount * CROP_PRICE[crop_type]  # Calculate income
        loan_amount = income * 0.6  # Loan is 60% of total income
        
        return jsonify({"yield": yield_amount, "income": income, "loan": loan_amount})
    except ValueError:
        return jsonify({"error": "Invalid input"})

# Free Translation API (Google Translate without API Key)
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_lang = request.form['lang']
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
    response = requests.get(url)
    translated_text = response.json()[0][0][0]
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> f8b7ddb (Initial commit)
