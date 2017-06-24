# Integration with Microsoft Cognitive Services
# Program recognizes faces and inserts a pic on their places

import requests as req
from PIL import Image

key = 'c352ae59f7cc48a6b622448016287116'

headers = {
	"Content-Type": "application/octet-stream",
	"Ocp-Apim-Subscription-Key": key
}

url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'

with open('fed.jpg', 'rb') as file:
	res = req.post(url, file.read(), headers=headers)

faces = res.json()
im = Image.open('fed.jpg').convert('RGBA')
for face in faces:
    print("Coordinates:"),
    print(face["faceRectangle"]['left']),
    print(face["faceRectangle"]['top'])

    print("Size:"),
    print(face["faceRectangle"]['width']),
    print(face["faceRectangle"]['height'])

    emotions_list = list(face["scores"].items())
    sorted_emotions = sorted(emotions_list, key=lambda x:x[1], reverse=True)

    print("Emotion:"),
    print(sorted_emotions[0][0])
    face_width = face["faceRectangle"]['width']
    face_height = face["faceRectangle"]['height']
    face_x = face["faceRectangle"]['left']
    face_y = face["faceRectangle"]['top']


    ### Part of changing the face ###


    
    smile = Image.open('smile.gif').convert('RGBA')

    smile = smile.resize((face_width, face_height))
    print(face_x, face_y, face_width, face_height)
    im.paste(smile, (face_x, face_y, face_x+face_width, face_y+face_height), smile)

im.show()





