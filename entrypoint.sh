#!/bin/sh

# マイグレーションファイルの初期化（初回のみ）
flask db init || echo "Migration directory already exists or init failed."

# マイグレーションの実行
flask db migrate -m "Automatic migration on startup"

# DBのアップグレード
flask db upgrade

# アプリケーションの起動
exec python app.py