from flask import Blueprint, jsonify, request
from app.models.page import Page

page_routes = Blueprint("pages", __name__)

@page_routes.route("/")
def home_page():
    pages = Page.query.all()
