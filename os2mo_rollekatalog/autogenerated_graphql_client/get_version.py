# Generated by ariadne-codegen on 2024-06-11 11:37
# Source: queries.graphql

from typing import Optional

from .base_model import BaseModel


class GetVersion(BaseModel):
    version: "GetVersionVersion"


class GetVersionVersion(BaseModel):
    mo_version: Optional[str]


GetVersion.update_forward_refs()
GetVersionVersion.update_forward_refs()
