from uuid import UUID

from .base_model import BaseModel


class TestingUpdateItUserPerson(BaseModel):
    ituser_update: "TestingUpdateItUserPersonItuserUpdate"


class TestingUpdateItUserPersonItuserUpdate(BaseModel):
    uuid: UUID


TestingUpdateItUserPerson.update_forward_refs()
TestingUpdateItUserPersonItuserUpdate.update_forward_refs()
