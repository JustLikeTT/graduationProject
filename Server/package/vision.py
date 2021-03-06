from google.cloud import vision
from google.cloud.vision import types
from base64 import b64decode

def vision_analytics(img_content):
    '''Post request to google cloud vision api
    return AnnotateImageResponse '''
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    max_results = 5
    request = {
      "image" : {
        "content" : img_content,
        },
      "features" : [
        {
          "type" : vision.enums.Feature.Type.LABEL_DETECTION ,
          "max_results": max_results,
        },
        {
          "type" : vision.enums.Feature.Type.LANDMARK_DETECTION ,
          "max_results": max_results,
        },
        {
          "type" : vision.enums.Feature.Type.LOGO_DETECTION ,
          "max_results": max_results,
        },
        {
          "type" : vision.enums.Feature.Type.TEXT_DETECTION ,
          # text detection, document text detection and crop hint do not apply "max_results".
        },
        {
          "type" : vision.enums.Feature.Type.WEB_DETECTION ,
          "max_results": max_results,
        },
      ]
        
    }
    # Performs label detection on the image file
    response = client.annotate_image(request)
    return response
    

if __name__ == '__main__':

    '''from base64 import b64encode
    with open("../picture.PNG","rb") as img:
        print(vision_analytics(b64encode(img.read())))'''
    from base64 import b64encode
    import requests
    url = "https://graduation-107.appspot.com/vision"
    url_local = "http://127.0.0.1:5000/vision"

    with open("../picture.PNG","rb") as img:
       b_img = b64encode(img.read())
    data = {'content': b_img}
    r = requests.post(url_local,data=data)
    print(r.text)
