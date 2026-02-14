from flask import Flask, send_from_directory
import os
DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'))

app = Flask(
    __name__,
    static_folder=DIST_DIR,
    static_url_path='/'
)

@app.route('/')
def serve_index():
    return send_from_directory(DIST_DIR, 'index.html')


@app.errorhandler(404)
def spa_fallback(e):
    path = getattr(e, 'description', '')
    return send_from_directory(DIST_DIR, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
