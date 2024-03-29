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


class PrintSize(str, Enum):
    """
    Name of the paper size format, f.e. A4, B0, letter, etc.
    """

    """
    allowed enum values
    """
    A0 = 'a0'
    A1 = 'a1'
    A2 = 'a2'
    A3 = 'a3'
    A4 = 'a4'
    A5 = 'a5'
    A6 = 'a6'
    A7 = 'a7'
    A8 = 'a8'
    A9 = 'a9'
    A10 = 'a10'
    B0 = 'b0'
    B1 = 'b1'
    B2 = 'b2'
    B3 = 'b3'
    B4 = 'b4'
    B5 = 'b5'
    B6 = 'b6'
    B7 = 'b7'
    B8 = 'b8'
    B9 = 'b9'
    B10 = 'b10'
    A2EXTRA = 'a2extra'
    A3EXTRA = 'a3extra'
    A3SUPER = 'a3super'
    SUPERA3 = 'supera3'
    A4EXTRA = 'a4extra'
    A4SUPER = 'a4super'
    SUPERA4 = 'supera4'
    A4LONG = 'a4long'
    A5EXTRA = 'a5extra'
    SOB5EXTRA = 'sob5extra'
    LETTER = 'letter'
    LEGAL = 'legal'
    EXECUTIVE = 'executive'
    TABLOID = 'tabloid'
    STATEMENT = 'statement'
    HALFLETTER = 'halfletter'
    FOLIO = 'folio'
    FLSA = 'flsa'
    FLSE = 'flse'
    NOTE = 'note'
    ENUM_11X17 = '11x17'
    ENUM_10X14 = '10x14'
    C0 = 'c0'
    C1 = 'c1'
    C2 = 'c2'
    C3 = 'c3'
    C4 = 'c4'
    C5 = 'c5'
    C6 = 'c6'
    C7 = 'c7'
    C8 = 'c8'
    C9 = 'c9'
    C10 = 'c10'
    JUNIORLEGAL = 'juniorlegal'
    MEMO = 'memo'
    GOVERNMENTLETTER = 'governmentletter'
    GOVERNMENTLEGAL = 'governmentlegal'
    LEDGER = 'ledger'
    ARCH1 = 'arch1'
    ARCH2 = 'arch2'
    ARCH3 = 'arch3'
    ARCH4 = 'arch4'
    ARCH5 = 'arch5'
    ARCH6 = 'arch6'
    ARCHA = 'archa'
    ARCHB = 'archb'
    ARCHC = 'archc'
    ARCHD = 'archd'
    ARCHE1 = 'arche1'
    ARCHE = 'arche'
    ARCHE2 = 'arche2'
    ARCHE3 = 'arche3'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrintSize from a JSON string"""
        return cls(json.loads(json_str))


