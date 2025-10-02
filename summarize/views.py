from flask import render_template, redirect, url_for, flash, request
from models import db, User
from flask_login import login_required
from transformers import pipeline
from . import summarize_bp

summarizer = None

# ===============================================
# ルーティング
# ===============================================
@summarize_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
  global summarizer
  summary = None
  text = ""
  if request.method == "POST":
    text = request.form.get("text", "")
    if text.strip():
      if summarizer is None:
        # 要約パイプライン
        summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
      result = summarizer(text, max_length=100, min_length=20, do_sample=False)
      summary = result[0]["summary_text"]
  return render_template("summarize/index.html", summary=summary, text=text)
