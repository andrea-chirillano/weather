#!D:\proyectos y cursos\weather\backend-weather\venv\Scripts\python.exe

import requests
from flask import Flask, request, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_exact_time(timestamp):
    # Convertir el timestamp a un objeto datetime
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    # Formatear la hora en HH:MM
    formatted_time = dt_object.strftime("%H:%M")
    return formatted_time

@app.route('/api/weather', methods=['GET'])
def get_weather():
    country_code = request.args.get('countryCode')
    city_name = request.args.get('cityInput')
    api_key = 'd0b424f9a7e664168950846de81ef193'
    ##url = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+','+country_code+'&appid='+apiId
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    # Extraer los datos específicos del JSON
    if 'main' in data and 'weather' in data and 'wind' in data:
        exact_time = get_exact_time(data.get('dt'))
        main_condition = data['weather'][0]['main'].lower()
        temperature_celsius = data['main']['temp'] - 273.15  # Convertir de Kelvin a Celsius
        wind_speed_meters_per_second = data['wind']['speed']
        precipitation_probability_percentage = data['clouds']['all']
        humidity_percentage = data['main']['humidity']
        # Convertir velocidad del viento de metros por segundo a kilómetros por hora
        wind_speed_kmh = wind_speed_meters_per_second * 3.6



        result = {
            'exact_time': exact_time,  # Asegúrate de implementar la función get_exact_time()
            'weather': main_condition,
            'temperature_celsius': temperature_celsius,
            'precipitation_probability': precipitation_probability_percentage,
            'humidity': humidity_percentage,
            'wind_speed': wind_speed_kmh
        }   

        return jsonify(result)

    return jsonify({'error': 'No se pudo obtener la información del clima'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
