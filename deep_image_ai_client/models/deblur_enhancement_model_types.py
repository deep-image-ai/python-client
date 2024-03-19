# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DeblurEnhancementModelTypes(str, Enum):
    """
    DeblurEnhancementModelTypes
    """

    """
    allowed enum values
    """
    V1 = 'v1'
    V2 = 'v2'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeblurEnhancementModelTypes from a JSON string"""
        return cls(json.loads(json_str))


