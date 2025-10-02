from flask import Blueprint

# authのBlueprint作成
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# viewsをインポートしてルーティングを登録
from . import views
