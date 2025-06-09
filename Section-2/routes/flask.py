from flask import Flask, make_response, request, jsonify

app = Flask(__name__)
data = [
{
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    }]
# (your data stays as it is above)

@app.route("/name_search")
def name_search():
    query = request.args.get("q")  # gets the ?q=Abdel part
    if not query:
        return make_response("Query parameter 'q' is required", 400)

    # case-insensitive search
    results = [person for person in data if query.lower() in person["first_name"].lower()]
    
    if not results:
        return make_response("No match found", 404)
    
    return jsonify(results)

# terminal will show this 
/home/project$ curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.11
Date: Mon, 09 Jun 2025 15:51:29 GMT
Content-Type: application/json
Content-Length: 321
Connection: close

[
  {
    "address": "2 Lake View Point",
    "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    "city": "Shreveport",
    "country": "United States",
    "first_name": "Abdel",
    "graduation_year": 1995,
    "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
    "last_name": "Duke",
    "zip": "71105"
  }
]
