from app import app
from flask import request, render_template


@app.route("/")
def main():
    print("Request Ip: ", request.headers.get("X-Forwarded-For"))

    return render_template("main.html")
