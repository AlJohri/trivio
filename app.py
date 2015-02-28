import os
from flask import Flask, request, redirect
from flask import Response
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond():
    resp = twilio.twiml.Response()
    resp.message("Your (%s) question was, %s." % (request.values.get('From'), request.values.get('Body')))
    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
