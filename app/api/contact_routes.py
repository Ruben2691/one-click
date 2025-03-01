from app.models.contact_message import ContactMessage
from flask import Blueprint, jsonify, request

contact_routes = Blueprint("contact", __name__)

# submit general inquiry
@contact_routes.route("/", methods=["POST"])
def submit_contact_message():
    data = request.get_json()
    new_contact_message = ContactMessage(
        name=data["name"],
        email=data["email"],
        message=data["message"]
    )
    new_contact_message.save()
    return new_contact_message.to_dict()

# get general contact info
@contact_routes.route("/", methods=["GET"])
def get_contact_message():
    contact_messages = ContactMessage.query.all()
    return {"contact_messages": [contact_message.to_dict() for contact_message in contact_messages]}


# schedule a consultation
@contact_routes.route("/consultation", methods=["POST"])
def schedule_consultation():
    data = request.get_json()
    new_contact_message = ContactMessage(
        name=data["name"],
        email=data["email"],
        message=data["message"]
    )
    new_contact_message.save()
    return new_contact_message.to_dict()


# get details of a scheduled consultation
@contact_routes.route("/consultation", methods=["GET"])
def get_consultation():
    contact_messages = ContactMessage.query.all()
    return {"contact_messages": [contact_message.to_dict() for contact_message in contact_messages]}
