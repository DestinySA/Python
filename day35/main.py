import requests
from twilio.rest import Client

MY_LAT = 19.45669
MY_LNG = -99.23441
API_KEY = "PUT YOUR KEY"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
TWILIO_WHATSAPP_NUMBER="CHANGE NUMBER"
YOUR_TWILIO_VERIFIED_NUMBER="CHANGE NUMBER"
TWILIO_SMS_NUMBER="CHANGE NUMBER"

account_sid = "PUT YOUR SID"
auth_token = "PUT YOUR AUTH"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": {MY_LAT},
    "lon": {MY_LNG},
    "appid": {API_KEY},
    "cnt": 4
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

    whatsapp_message = client.messages.create(
        from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
        body="It's going to rain today. Remember to bring an umbrella",
        to=f"whatsapp:{YOUR_TWILIO_VERIFIED_NUMBER}"
    )

    sms_message = client.messages.create(
        from_=f"{TWILIO_SMS_NUMBER}",
        body="Bring an umbrella.",
        to=f"{YOUR_TWILIO_VERIFIED_NUMBER}"
    )
