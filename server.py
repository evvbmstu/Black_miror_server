
# coding: utf-8
from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import functions


# Initialize the Flask application
app = Flask(__name__)
face_casc = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    faces = face_casc.detectMultiScale(img, 1.3, 5)
    for idx, (x, y, w, h) in enumerate(faces):
        max_area = area(faces)
        if idx == max_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_face = img[y:y + h, x:x + w]
    cv2.imshow('img', roi_face)
    cv2.waitKey(30)
     #cv2.imwrite('example.png', roi_gray)
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == "__main__":
    # start flask app
    app.run(host="0.0.0.0", port=5000)




