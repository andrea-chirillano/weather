import pytz
import requests
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

app = Flask(__name__)
CORS(app)

def get_coordinates(city_name, country_name):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(f"{city_name}, {country_name}")
    return (location.latitude, location.longitude) if location else None

def get_exact_time(timestamp, city_name, country_name):
    # Create a datetime object from timestamp in UTC
    dt_utc = datetime.utcfromtimestamp(timestamp)

    # Get the coordinates (latitude and longitude) of the city
    coordinates = get_coordinates(city_name, country_name)

    if coordinates:
        # Get time zone from coordinates
        tf = TimezoneFinder()
        tz_str = tf.timezone_at(lng=coordinates[1], lat=coordinates[0])

        if tz_str:
            tz_local = pytz.timezone(tz_str)

            # Convert UTC datetime to local time zone
            dt_local = dt_utc.replace(tzinfo=pytz.utc).astimezone(tz_local)

            # Format and display local time
            formatted_time = dt_local.strftime("%A, %H:%M %p")
            return formatted_time

    # If the time zone cannot be obtained, return None or handle the case according to your needs.
    return None

def get_country(country_code):
    country_dict = {
        'AD':"Andorra",
        'AE':"United Arab Emirates",
        'AF':"Afghanistan",
        'AG':"Antigua and Barbuda",
        'AI':"Anguilla",
        'AL':"Albania",
        'AM':"Armenia",
        'AO':"Angola",
        'AQ':"Antarctica",
        'AR':"Argentina",
        'AS':"American Samoa",
        'AT':"Austria",
        'AU':"Australia",
        'AW':"Aruba",
        'AX':"Åland Islands",
        'AZ':"Azerbaijan",
        'BA':"Bosnia and Herzegovina",
        'BB':"Barbados",
        'BD':"Bangladesh",
        'BE':"Belgium",
        'BF':"Burkina Faso",
        'BG':"Bulgaria",
        'BH':"Bahrain",
        'BI':"Burundi",
        'BJ':"Benin",
        'BL':"Saint Barthélemy",
        'BM':"Bermuda",
        'BN':"Brunei Darussalam",
        'BO':"Bolivia (Plurinational State of)",
        'BQ':"Bonaire, Sint Eustatius and Saba",
        'BR':"Brazil",
        'BS':"Bahamas",
        'BT':"Bhutan",
        'BV':"Bouvet Island",
        'BW':"Botswana",
        'BY':"Belarus",
        'BZ':"Belize",
        'CA':"Canada",
        'CC':"Cocos (Keeling) Islands",
        'CD':"Congo, Democratic Republic of the",
        'CF':"Central African Republic",
        'CG':"Congo",
        'CH':"Switzerland",
        'CI':"Côte d'Ivoire",
        'CK':"Cook Islands",
        'CL':"Chile",
        'CM':"Cameroon",
        'CN':"China",
        'CO':"Colombia",
        'CR':"Costa Rica",
        'CU':"Cuba",
        'CV':"Cabo Verde",
        'CW':"Curaçao",
        'CX':"Christmas Island",
        'CY':"Cyprus",
        'CZ':"Czechia",
        'DE':"Germany",
        'DJ':"Djibouti",
        'DK':"Denmark",
        'DM':"Dominica",
        'DO':"Dominican Republic",
        'DZ':"Algeria",
        'EC':"Ecuador",
        'EE':"Estonia",
        'EG':"Egypt",
        'EH':"Western Sahara",
        'ER':"Eritrea",
        'ES':"Spain",
        'ET':"Ethiopia",
        'FI':"Finland",
        'FJ':"Fiji",
        'FK':"Falkland Islands (Malvinas)",
        'FM':"Micronesia (Federated States of)",
        'FO':"Faroe Islands",
        'FR':"France",
        'GA':"Gabon",
        'GB':"United Kingdom of Great Britain and Northern Ireland",
        'GD':"Grenada",
        'GE':"Georgia",
        'GF':"French Guiana",
        'GG':"Guernsey",
        'GH':"Ghana",
        'GI':"Gibraltar",
        'GL':"Greenland",
        'GM':"Gambia",
        'GN':"Guinea",
        'GP':"Guadeloupe",
        'GQ':"Equatorial Guinea",
        'GR':"Greece",
        'GS':"South Georgia and the South Sandwich Islands",
        'GT':"Guatemala",
        'GU':"Guam",
        'GW':"Guinea-Bissau",
        'GY':"Guyana",
        'HK':"Hong Kong",
        'HM':"Heard Island and McDonald Islands",
        'HN':"Honduras",
        'HR':"Croatia",
        'HT':"Haiti",
        'HU':"Hungary",
        'ID':"Indonesia",
        'IE':"Ireland",
        'IL':"Israel",
        'IM':"Isle of Man",
        'IN':"India",
        'IO':"British Indian Ocean Territory",
        'IQ':"Iraq",
        'IR':"Iran (Islamic Republic of)",
        'IS':"Iceland",
        'IT':"Italy",
        'JE':"Jersey",
        'JM':"Jamaica",
        'JO':"Jordan",
        'JP':"Japan",
        'KE':"Kenya",
        'KG':"Kyrgyzstan",
        'KH':"Cambodia",
        'KI':"Kiribati",
        'KM':"Comoros",
        'KN':"Saint Kitts and Nevis",
        'KP':"Korea (Democratic People's Republic of)",
        'KR':"Korea, Republic of",
        'KW':"Kuwait",
        'KY':"Cayman Islands",
        'KZ':"Kazakhstan",
        'LA':"Lao People's Democratic Republic",
        'LB':"Lebanon",
        'LC':"Saint Lucia",
        'LI':"Liechtenstein",
        'LK':"Sri Lanka",
        'LR':"Liberia",
        'LS':"Lesotho",
        'LT':"Lithuania",
        'LU':"Luxembourg",
        'LV':"Latvia",
        'LY':"Libya",
        'MA':"Morocco",
        'MC':"Monaco",
        'MD':"Moldova, Republic of",
        'ME':"Montenegro",
        'MF':"Saint Martin (French part)",
        'MG':"Madagascar",
        'MH':"Marshall Islands",
        'MK':"North Macedonia",
        'ML':"Mali",
        'MM':"Myanmar",
        'MN':"Mongolia",
        'MO':"Macao",
        'MP':"Northern Mariana Islands",
        'MQ':"Martinique",
        'MR':"Mauritania",
        'MS':"Montserrat",
        'MT':"Malta",
        'MU':"Mauritius",
        'MV':"Maldives",
        'MW':"Malawi",
        'MX':"Mexico",
        'MY':"Malaysia",
        'MZ':"Mozambique",
        'NA':"Namibia",
        'NC':"New Caledonia",
        'NE':"Niger",
        'NF':"Norfolk Island",
        'NG':"Nigeria",
        'NI':"Nicaragua",
        'NL':"Netherlands, Kingdom of the",
        'NO':"Norway",
        'NP':"Nepal",
        'NR':"Nauru",
        'NU':"Niue",
        'NZ':"New Zealand",
        'OM':"Oman",
        'PA':"Panama",
        'PE':"Peru",
        'PF':"French Polynesia",
        'PG':"Papua New Guinea",
        'PH':"Philippines",
        'PK':"Pakistan",
        'PL':"Poland",
        'PM':"Saint Pierre and Miquelon",
        'PN':"Pitcairn",
        'PR':"Puerto Rico",
        'PS':"Palestine, State of",
        'PT':"Portugal",
        'PW':"Palau",
        'PY':"Paraguay",
        'QA':"Qatar",
        'RE':"Réunion",
        'RO':"Romania",
        'RS':"Serbia",
        'RU':"Russian Federation",
        'RW':"Rwanda",
        'SA':"Saudi Arabia",
        'SB':"Solomon Islands",
        'SC':"Seychelles",
        'SD':"Sudan",
        'SE':"Sweden",
        'SG':"Singapore",
        'SH':"Saint Helena, Ascension and Tristan da Cunha",
        'SI':"Slovenia",
        'SJ':"Svalbard and Jan Mayen",
        'SK':"Slovakia",
        'SL':"Sierra Leone",
        'SM':"San Marino",
        'SN':"Senegal",
        'SO':"Somalia",
        'SR':"Suriname",
        'SS':"South Sudan",
        'ST':"Sao Tome and Principe",
        'SV':"El Salvador",
        'SX':"Sint Maarten (Dutch part)",
        'SY':"Syrian Arab Republic",
        'SZ':"Eswatini",
        'TC':"Turks and Caicos Islands",
        'TD':"Chad",
        'TF':"French Southern Territories",
        'TG':"Togo",
        'TH':"Thailand",
        'TJ':"Tajikistan",
        'TK':"Tokelau",
        'TL':"Timor-Leste",
        'TM':"Turkmenistan",
        'TN':"Tunisia",
        'TO':"Tonga",
        'TR':"Türkiye",
        'TT':"Trinidad and Tobago",
        'TV':"Tuvalu",
        'TW':"Taiwan, Province of China",
        'TZ':"Tanzania, United Republic of",
        'UA':"Ukraine",
        'UG':"Uganda",
        'UM':"United States Minor Outlying Islands",
        'US':"United States of America",
        'UY':"Uruguay",
        'UZ':"Uzbekistan",
        'VA':"Holy See",
        'VC':"Saint Vincent and the Grenadines",
        'VE':"Venezuela (Bolivarian Republic of)",
        'VG':"Virgin Islands (British)",
        'VI':"Virgin Islands (U.S.)",
        'VN':"Viet Nam",
        'VU':"Vanuatu",
        'WF':"Wallis and Futuna",
        'WS':"Samoa",
        'YE':"Yemen",
        'YT':"Mayotte",
        'ZA':"South Africa",
        'ZM':"Zambia",
        'ZW':"Zimbabwe"
    }
    return country_dict.get(country_code, 'Unknown country')

@app.route(f'/api/weather', methods=['GET'])
def get_weather():
    country_code = request.args.get('countryCode')
    city_name = request.args.get('cityInput')
    api_key = 'd0b424f9a7e664168950846de81ef193'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    country_name = get_country(data.get('sys', {}).get('country'))
    city_data_name = data.get('name')
    exact_time = get_exact_time(data.get('dt'), country_name, city_data_name)
    main_condition = data['weather'][0]['main'].lower()
    temperature_celsius = int(data['main']['temp'] - 273.15)  # Convert from Kelvin to Celsius
    wind_speed_meters_per_second = data['wind']['speed']
    precipitation_probability_percentage = data['clouds']['all']
    humidity_percentage = data['main']['humidity']
    wind_speed_kmh = int(wind_speed_meters_per_second * 3.6) #Convert wind speed from meters per second to kilometers per hour

    result = {
        'country_name': country_name,
        'city_name': city_data_name,
        'exact_time': exact_time,  
        'weather': main_condition.capitalize(),
        'temperature_celsius': temperature_celsius,
        'precipitation_probability': precipitation_probability_percentage,
        'humidity': humidity_percentage,
        'wind_speed': wind_speed_kmh,
        'datetime': data.get('dt'),
        
    }   

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
