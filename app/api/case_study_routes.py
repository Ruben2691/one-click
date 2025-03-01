from flask import Blueprint, jsonify
from app.models.case_study import CaseStudy

case_study_routes = Blueprint("case_studies", __name__)

# get all case studies
@case_study_routes.route("/")
def get_case_studies():
    case_studies = CaseStudy.query.all()
    return {"case_studies": [case_study.to_dict() for case_study in case_studies]}


# get specific case study
@case_study_routes.route("/<int:id>")
def get_case_study(id):
    case_study = CaseStudy.query.get(id)
    return case_study.to_dict()


# get case studies by category
@case_study_routes.route("/category/<string:category>")
def get_case_studies_by_category(category):
    case_studies = CaseStudy.query.filter(CaseStudy.category == category).all()
    return {"case_studies": [case_study.to_dict() for case_study in case_studies]}
