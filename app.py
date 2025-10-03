from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, User
from flask_login import LoginManager
from auth.views import auth_bp
from summarize.views import summarize_bp

# ===============================================
# Flask
# ===============================================

app = Flask(__name__)
# 設定ファイル読み込み
app.config.from_object('config.Config')
# dbとFlaskの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)
# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskの紐づけ
login_manager.init_app(app)
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージ
login_manager.login_message = "認証していません：ログインしてください"
# # リダイレクトされる関数名を設定する（ブループリント対応）
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# blueprint登録
app.register_blueprint(auth_bp)
app.register_blueprint(summarize_bp)

# エラーページ
def show_404_page(error):
  msg = getattr(error, "description", "ページが見つかりません")
  return render_template('errors/404.html', msg=msg), 404

app.register_error_handler(404, show_404_page)

# ===============================================
# 実行
# ===============================================
if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
