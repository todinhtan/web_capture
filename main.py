from selenium import webdriver
from flask import Flask, request, abort

app = Flask(__name__)

def getScreenshot(url):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(url)

    imgBytes = driver.get_screenshot_as_png()
    driver.quit()

    return imgBytes

@app.route('/health', methods=['GET'])
def health():
    return 'running'

@app.route('/', methods=['POST'])
def index():
    if not request.json or not 'url' in request.json:
        abort(400)
    url = request.json.get('url', '')

    imgBytes = getScreenshot(url)

    return imgBytes

if __name__ == '__main__':
    app.run(debug=False)