from flask import Blueprint
from core.models.teachers import Teacher
from core.apis import decorators
from .schema import TeacherSchema
from core.apis.responses import APIResponse

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(headers):
    teachers_list=Teacher.get_all_teachers()
    data= TeacherSchema(many=True).dump(teachers_list)
    return APIResponse.respond(data=data)
