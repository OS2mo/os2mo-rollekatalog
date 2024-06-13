# Generated by ariadne-codegen on 2024-06-13 11:33
# Source: queries.graphql

from typing import List, Optional
from uuid import UUID

from .base_model import BaseModel


class GetTitles(BaseModel):
    classes: "GetTitlesClasses"


class GetTitlesClasses(BaseModel):
    objects: List["GetTitlesClassesObjects"]


class GetTitlesClassesObjects(BaseModel):
    current: Optional["GetTitlesClassesObjectsCurrent"]


class GetTitlesClassesObjectsCurrent(BaseModel):
    user_key: str
    uuid: UUID


GetTitles.update_forward_refs()
GetTitlesClasses.update_forward_refs()
GetTitlesClassesObjects.update_forward_refs()
GetTitlesClassesObjectsCurrent.update_forward_refs()
