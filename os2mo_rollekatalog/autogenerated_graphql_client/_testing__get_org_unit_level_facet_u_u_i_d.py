from typing import List
from uuid import UUID

from .base_model import BaseModel


class TestingGetOrgUnitLevelFacetUUID(BaseModel):
    facets: "TestingGetOrgUnitLevelFacetUUIDFacets"


class TestingGetOrgUnitLevelFacetUUIDFacets(BaseModel):
    objects: List["TestingGetOrgUnitLevelFacetUUIDFacetsObjects"]


class TestingGetOrgUnitLevelFacetUUIDFacetsObjects(BaseModel):
    uuid: UUID


TestingGetOrgUnitLevelFacetUUID.update_forward_refs()
TestingGetOrgUnitLevelFacetUUIDFacets.update_forward_refs()
TestingGetOrgUnitLevelFacetUUIDFacetsObjects.update_forward_refs()
