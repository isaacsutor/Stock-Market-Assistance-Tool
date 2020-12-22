import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Stock Market Tool API Website</h1>"

@app.route('/timeseries', methods=['POST'])
def timeSeries():
    return False

@app.route('/sentimentAnalysis', methods=['POST'])
def sentimentAnalysis():
    return False

@app.route('/pdfGeneration', methods=['POST'])
def pdfGeneration():
    return False

@app.route('/webScraping', methods=['POST'])
def webScraping():
    return False

@app.route('/technicalAnalysis', methods=['POST'])
def technicalAnalysis():
    return False

@app.route('/ratios', methods=['POST'])
def ratios():
    return False

app.run()