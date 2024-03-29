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


class OutputFormat(str, Enum):
    """
    The format of the output image.
    """

    """
    allowed enum values
    """
    JPEG = 'jpeg'
    JPG = 'jpg'
    PNG = 'png'
    WEBP = 'webp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OutputFormat from a JSON string"""
        return cls(json.loads(json_str))


