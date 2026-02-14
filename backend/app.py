from flask import Flask, send_from_directory
import os

# Flask を dist に向けて静的配信させる
# Windows パスでも動くように相対で指定
DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'))

app = Flask(
    __name__,
    static_folder=DIST_DIR,        # /assets などの静的配信元
    static_url_path='/'            # /assets/... のURLをそのまま使えるように
)

@app.route('/')
def serve_index():
    return send_from_directory(DIST_DIR, 'index.html')

# React Router などで /foo や /bar に直接アクセスされたときのフォールバック
@app.errorhandler(404)
def spa_fallback(e):
    # /api/... の 404 はそのまま返す。フロントのルートは index.html にフォールバック
    path = getattr(e, 'description', '')
    # ここでは簡易に index.html を返して SPA ルーティングに任せる
    return send_from_directory(DIST_DIR, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)