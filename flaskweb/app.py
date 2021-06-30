from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')  # 루트 경로
def index():
    return render_template("templet.html")

if __name__ == "__main__":
    app.run()