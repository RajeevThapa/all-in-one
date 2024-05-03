# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "d76f4f83eb54b081fe88fbf54a9061df"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
        if weather:
            return render_template("weather.html", weather=weather)
        else:
            error_message = "Failed to fetch weather data. Please try again."
            return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
