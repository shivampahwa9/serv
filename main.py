from flask import Flask,request
import json
import requests
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
	p = {'q':"shivam"}
	req = request.get_json()
	print(req)
	# print(req)

	r=json.loads(json.dumps(req))
	print(r)
	ss="hello " + r["q"]
	print(ss)
	s = {"results":ss}

	return json.dumps(s)


if __name__ == '__main__':
	app.run(debug= True,port=5500,host='0.0.0.0')