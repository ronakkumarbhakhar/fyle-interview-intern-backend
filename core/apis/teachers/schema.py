from marshmallow import post_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.apis.decorators import add_headers
from core.models.teachers import Teacher

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model =Teacher

    @post_dump
    @add_headers
    def add_userId(headers,data,many):
        data["user_id"]=headers["user_id"]
        return data