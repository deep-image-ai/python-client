# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from deep_image_ai_client.models.generate_adapter_types import GenerateAdapterTypes
from typing import Optional, Set
from typing_extensions import Self

class GenerateParameters(BaseModel):
    """
    GenerateParameters
    """ # noqa: E501
    description: Optional[StrictStr] = None
    item_area_percentage: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = 1
    sample_num: Optional[StrictInt] = None
    color: Optional[StrictStr] = Field(default=None, description="E.g. rgb(red, green, blue), #rrggbbaa, hsl(hue, saturation%, lightness%), hsv(hue, saturation%, value%) and common HTML color names.")
    additional_prompt: Optional[StrictStr] = None
    negative_prompt: Optional[StrictStr] = None
    adapter_type: Optional[GenerateAdapterTypes] = None
    __properties: ClassVar[List[str]] = ["description", "item_area_percentage", "sample_num", "color", "additional_prompt", "negative_prompt", "adapter_type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GenerateParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenerateParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "item_area_percentage": obj.get("item_area_percentage") if obj.get("item_area_percentage") is not None else 1,
            "sample_num": obj.get("sample_num"),
            "color": obj.get("color"),
            "additional_prompt": obj.get("additional_prompt"),
            "negative_prompt": obj.get("negative_prompt"),
            "adapter_type": obj.get("adapter_type")
        })
        return _obj

