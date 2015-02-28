import os, csv
from flask import Flask, request, redirect
from flask import Response
import twilio.twiml

app = Flask(__name__)

jmap = {}

with open("jeopardy.csv") as f:
	reader = csv.DictReader(f)
	for row in reader:
		jmap[row['clue'] + "."] = row['answer']

@app.route("/", methods=['GET', 'POST'])
def respond():
	resp = twilio.twiml.Response()

	if request.values.get('Body'):
		question = request.values.get('Body').split("\n")[-1]
	else:
		raise Exception("question cannot be parsed: %s" % request.values.get('Body'))

	if jmap.get(question) == None:
		raise Exception("question not found in jeopardy: %s" % question)
	else:
		resp.message("What is %s?" % (jmap[question]))
		return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
