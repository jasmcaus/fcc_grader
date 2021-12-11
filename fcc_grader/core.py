from flask import Flask, json, jsonify, request, Response
import requests 
import numpy as np

app = Flask(__name__)

def _grade(curriculum : str, lesson : str, answer):
    response = post(curriculum, lesson, answer)

    if response.status_code == 200:
        print("Ola 🎉! Your answer is correct")
    else:
        print("Oops 😕! Please review your answer and try again")


# @app.route("/post", methods=["GET"])
# def post(curriculum : str, lesson : str, answer):
#     headers={
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'X-Client-Version': '0.8.8'
#     }

#     resp = requests.post(
#         "http://127.0.0.1:5000/listen",
#         json={
#             "curriculum": curriculum,
#             "lesson": lesson,
#             "answer": answer
#         }, 
#         headers=headers
#     )
#     return resp


@app.route("/listen", methods=["POST"])
def listen():
    data = request.json
    curriculum = data["curriculum"]
    lesson = data["lesson"]
    answer = data["answer"]

    if curriculum == "scientific-computing":
        if lesson == "lesson1":
            if answer == "2":
                return True
        
        elif lesson == "lesson2":
            if answer == "45":
                return True
        
        elif lesson == "lesson3":
            if answer == "4":
                return True

        ...
    
    return Response("invalid", status=500, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)