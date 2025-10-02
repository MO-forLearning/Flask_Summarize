from flask import Blueprint

# summarizeのBlueprint作成
summarize_bp = Blueprint('summarize', __name__, url_prefix='/summarize')

# viewsをインポートしてルーティングを登録
from . import views
