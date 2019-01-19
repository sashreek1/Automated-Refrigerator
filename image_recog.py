import json
from watson_developer_cloud import VisualRecognitionV3, \
    WatsonApiException
visual_recognition = VisualRecognitionV3(
    '2018-03-19', iam_apikey='zpgZhvMTq0nNWqe17lsGxMXOMmTaETMzxziKFFGeQzX2')
with open('C:/Users/sashr_000/Desktop/tomato.png', 'rb') as images_zip:
    try:
        response = visual_recognition.classify(images_zip, threshold=0.0, classifier_ids='food')
        final = (json.dumps(response.result, indent=1))
        print(final)
    except WatsonApiException as ex:
        print ("Status code: {}\nError message: {}\nError info: \n{}").format(ex.code, ex.message, json.dumps(ex.info, indent=1))