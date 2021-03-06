# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, render_template, abort
import gmplot

app = Flask(__name__)
class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/index")
def mainpage():
    return render_template('index.html', schools=schools)

@app.route("/")
def index():
    return render_template('index.html', schools=schools)

@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)


@app.route("/graph_example")
def graph(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', pageType='graph',chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


port = os.getenv('PORT', '5001')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=port)
