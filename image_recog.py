import json
import cv2
import ast
from watson_developer_cloud import VisualRecognitionV3, \
    WatsonApiException
visual_recognition = VisualRecognitionV3(
    '2018-03-19', iam_apikey='zpgZhvMTq0nNWqe17')#your Api key here
def pic_cap():#capturing pictures
    cam = cv2.VideoCapture(1)
    ret, frame = cam.read()
    cv2.imwrite("test.jpg", frame)
    cv2.imshow('recog', frame)
    k = cv2.waitKey(1)
    cam.release()
def decode(img_file):
    with open(img_file, 'rb') as images_zip:
        try:
            response = visual_recognition.classify(images_zip, threshold=0.0, classifier_ids='food')
            final = str(json.dumps(response.result, indent=1))
            item=(ast.literal_eval(final)['images'][0]["classifiers"][0]['classes'][0]["class"])
            #print(item)
            return(item)
            
        except WatsonApiException as ex:
            print ("Status code: {}\nError message: {}\nError info: \n{}").format(ex.code, ex.message, json.dumps(ex.info, indent=1))
def scanner():
    pic_cap()
    decode('test.jpg')
#print(scanner())