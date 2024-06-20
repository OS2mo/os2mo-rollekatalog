# Generated by ariadne-codegen on 2024-06-20 16:41
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class TestingCreateOrgUnitRoot(BaseModel):
    org_unit_create: "TestingCreateOrgUnitRootOrgUnitCreate"


class TestingCreateOrgUnitRootOrgUnitCreate(BaseModel):
    uuid: UUID


TestingCreateOrgUnitRoot.update_forward_refs()
TestingCreateOrgUnitRootOrgUnitCreate.update_forward_refs()
