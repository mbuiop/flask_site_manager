from app import app

@app.route("/")
def index():
    return "سلام از فلاسک!"
