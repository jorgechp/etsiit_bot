import flask, telebot
from etsiit_bot.bot import bot
from pathlib import Path

REPO_ROOT = Path(__file__).resolve(strict=True).parents[1]
app = flask.Flask(__name__)
WEBHOOK_URL_PATH = f"/{bot.token}"
index = open(REPO_ROOT.joinpath("static", "index.html")).read()


# Process index page
@app.route("/")
def root():
    return index


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)


if __name__ == "__main__":
    app.run()
