from flask import Blueprint
from core import db
from core.libs import assertions
from core.apis import decorators
from core.models.assignments import Assignment
from core.apis.responses import APIResponse
from .schema import AssignmentSchema

principal_assignment_resources = Blueprint('principal_assignment_resources', __name__)



@principal_assignment_resources.route('/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(headers,incoming_payload):
    """It grades the assignment"""
    assignment=Assignment.get_by_id(incoming_payload["id"])
    assertions.assert_found(assignment)
    assertions.assert_valid(assignment.state!="DRAFT","If an assignment is in Draft state, it cannot be graded by principal")
    assignment.grade=incoming_payload["grade"]
    assignment.state="GRADED"
    db.session.flush()
    db.session.commit()
    assignment=AssignmentSchema(many=False).dump(assignment)
    return APIResponse.respond(data=assignment)

@principal_assignment_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(headers):
    """Returns list of assignments"""
    assignment_list=Assignment.get_assignments()
    list=AssignmentSchema(many=True).dump(assignment_list)
    return APIResponse.respond(data=list)