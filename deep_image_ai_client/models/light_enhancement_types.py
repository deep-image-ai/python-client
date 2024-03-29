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


class LightEnhancementTypes(str, Enum):
    """
    LightEnhancementTypes
    """

    """
    allowed enum values
    """
    CONTRAST = 'contrast'
    HDR_LIGHT = 'hdr_light'
    HDR_LIGHT_ADVANCED = 'hdr_light_advanced'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LightEnhancementTypes from a JSON string"""
        return cls(json.loads(json_str))


