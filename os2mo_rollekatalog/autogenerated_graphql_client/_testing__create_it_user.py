# Generated by ariadne-codegen on 2024-06-20 16:41
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class TestingCreateItUser(BaseModel):
    ituser_create: "TestingCreateItUserItuserCreate"


class TestingCreateItUserItuserCreate(BaseModel):
    uuid: UUID


TestingCreateItUser.update_forward_refs()
TestingCreateItUserItuserCreate.update_forward_refs()
