from flask import Flask, render_template, request
import urllib.request
import urllib.error
import json

app = Flask(__name__)


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

    except urllib.error.HTTPError:
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    user = None
    error = None

    if request.method == "POST":
        username = request.form["username"].strip()

        user = get_github_user(username)

        if user is None:
            error = "GitHub user not found."

    return render_template(
        "index.html",
        user=user,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
