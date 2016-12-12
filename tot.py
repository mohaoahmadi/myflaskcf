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

@app.route("/")
def index():


    gmap = gmplot.GoogleMapPlotter(22.060191, 39.216372, 14)
    lats = [22.137180, 22.079267, 22.060191, 22.053628, 22.137240, 22.079127, 22.040121, 22.053478, 22.133280,
            22.0796467, 22.060591, 22.058728, 22.137540, 22.077527, 22.045321, 22.064478]
    lngs = [39.186157, 39.194130, 39.216372, 39.224843, 39.186657, 39.194820, 39.216752, 39.224342, 39.186157,
            39.194130, 39.216372, 39.224843, 39.186657, 39.194820, 39.216752, 39.224342]
    # gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)
    # gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
    # gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
    gmap.heatmap(lats, lngs)

    #gmap.draw("templates/index.html")
    return render_template('index.html')



port = os.getenv('PORT', '5001')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=port)
