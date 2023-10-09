from flask import Flask
from controllers import img_blueprint, data_blueprint, music_blueprint, sound_blueprint, openai_blueprint
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(img_blueprint, url_prefix="/img")
app.register_blueprint(data_blueprint, url_prefix="/data")
app.register_blueprint(sound_blueprint, url_prefix="/sound")
app.register_blueprint(music_blueprint, url_prefix="/music")
app.register_blueprint(openai_blueprint, url_prefix="/openai")

if __name__ == "__main__":
    app.run(debug=True)