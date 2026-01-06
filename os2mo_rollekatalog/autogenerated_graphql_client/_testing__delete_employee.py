from uuid import UUID

from .base_model import BaseModel


class TestingDeleteEmployee(BaseModel):
    employee_delete: "TestingDeleteEmployeeEmployeeDelete"


class TestingDeleteEmployeeEmployeeDelete(BaseModel):
    uuid: UUID


TestingDeleteEmployee.update_forward_refs()
TestingDeleteEmployeeEmployeeDelete.update_forward_refs()
