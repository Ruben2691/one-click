from flask import Blueprint, jsonify
from app.models.service import Services

service_routes = Blueprint("services", __name__)

# get services
@service_routes.route("/")
def get_services():
    services = Services.query.all()
    return {"services": [service.to_dict() for service in services]}

# get details of a specific service
@service_routes.route("/<int:id>")
def get_service(id):
    service = Services.query.get(id)
    return service.to_dict()

# get case studies relevant to a service
@service_routes.route("/<int:id>/case_studies")
def get_service_case_studies(id):
    service = Services.query.get(id)
    return {"case_studies": [case_study.to_dict() for case_study in service.case_studies]}


# get client testimonials
@service_routes.route("/<int:id>/client_testimonials")
def get_service_client_testimonials(id):
    service = Services.query.get(id)
    return {"client_testimonials": [client_testimonial.to_dict() for client_testimonial in service.client_testimonials]}
