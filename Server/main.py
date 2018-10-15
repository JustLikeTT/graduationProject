# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]

from base64 import b64decode
import io
import logging
import os

from flask import Flask,request

from package.search import google_search_engineering
from package.translate import translate_text
from package.vision import vision_analytics

API_key = open("key/api_key.txt","r").read()
engineering_ID = "015664378164063206829:iu-niupqc9i"

app = Flask(__name__)
search_engineering = google_search_engineering(API_key, engineering_ID)


@app.route("/search/<keyword>", methods=['GET'])
def search(keyword):
    '''Return google search response'''
    return search_engineering.searching(keyword)

@app.route("/translation/<text>", methods=['GET'])
def tranlate(text):
    
    target_languagze = 'zh' # the languagze code reference ISO-639-1
    
    result = translate_text(text, target_languagze)
    return result

@app.route("/vision",methods=['POST','GET'])
def receive_img():
	
    if request.method == 'POST':
        #print("form:",request.form)
        img_b64 = request.form['content']
        img_content = b64decode(img_b64) 
        resurlt_str = vision_analytics(img_content)
        return resurlt_str
    else :
        return "request is get but it is nothing"
        
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500    

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    #result = vision_analytics()
    app.run(host='0.0.0.0', port=5000, debug=False)
# [END app]
