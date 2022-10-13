from flask import Flask

from models import session, GameData

app = Flask(__name__)


@app.route('/get-results')
def get_results():
    save_client = session.query(GameData).order_by(GameData.id.desc()).first()
    out_data = save_client.output_data
    return str(out_data)


if __name__ == '__main__':
    app.run()
