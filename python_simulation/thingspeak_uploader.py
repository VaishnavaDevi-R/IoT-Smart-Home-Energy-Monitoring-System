import requests

WRITE_API_KEY = "HRXKXH3APFUKONWP"

THINGSPEAK_URL = "https://api.thingspeak.com/update"


def upload_to_thingspeak(
    voltage,
    current,
    power,
    energy,
    cost,
    alert
):

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": voltage,
        "field2": current,
        "field3": power,
        "field4": energy,
        "field5": cost,
        "field6": alert
    }

    try:

        response = requests.post(
            THINGSPEAK_URL,
            data=payload,
            timeout=10
        )

        if response.status_code == 200:
            print("✅ Data uploaded to ThingSpeak")

        else:
            print(f"❌ Upload failed: {response.status_code}")

    except Exception as e:

        print(f"❌ ThingSpeak Error: {e}")