from pydantic import BaseModel


class UserSchema(BaseModel):
    new_person: str


class UserSchemaResponse(UserSchema):
    user_id: int


class DeleteSchemaResponse(BaseModel):
    message: str


class UpdateUserSchema(BaseModel):
    new_details: str
