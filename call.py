from flask import Flask,request
import requests
import urllib 
import json
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def hello():
	URL = "http://127.0.0.1:5500/"
	PARAMS = {"q":"Mr. Shubham"}
	#print(PARAMS)
	print("\n\n\n\ncalling")
	print("\n\n\n\ncallingn\nn\nn\n")
	# r = requests.post(url = URL, data = {'q':"shivam"}) 
	# # data = r.json()
	# # print (r.json())
	# print("\n\n\n\ncalled")
	# return r.text
	req = urllib.request.Request(URL)
	req.add_header('Content-Type', 'application/json; charset=utf-8' )
	jsondata = json.dumps(PARAMS)
	jsondataasbytes = jsondata.encode('utf-8')
	res = urllib.request.urlopen(req,jsondataasbytes)
	avs=(json.loads(res.read())["results"])
	print(avs)
	# return res.read()
	return avs

if __name__ == '__main__':
	app.run(debug= True,port=5501,host='0.0.0.0')


