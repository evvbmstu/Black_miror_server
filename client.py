
# coding: utf-8

import requests
import json
import cv2

if __name__ == "__main__":

    host = 'http://localhost:5000'
    test_url = host + '/api/test'

    # Prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}
    cap = cv2.VideoCapture(1)
    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, img_encoded = cv2.imencode('.jpg', gray)
        response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        cv2.imshow("Client image", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Условия выхода
            break
    cap.release()
    print(json.loads(response.text))


