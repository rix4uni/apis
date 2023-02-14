from flask import Flask, jsonify
import phonenumbers
from phonenumbers import timezone as pytz, geocoder, carrier
import rapidjson

app = Flask(__name__)

@app.route("/phone_info/<string:phone_number>", methods=["GET"])
def phone_info(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        time_zone = pytz.time_zones_for_number(number)[0]
        operator = carrier.name_for_number(number, "en")
        country = geocoder.description_for_number(number, "en")

        response = {"timezone": time_zone, "operator": operator, "country": country}
        return rapidjson.dumps(response,sort_keys=False)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

# http://localhost:5000/phone_info/+37253654136