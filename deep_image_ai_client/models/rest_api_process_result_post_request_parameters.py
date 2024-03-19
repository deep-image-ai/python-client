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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from deep_image_ai_client.models.background_parameters import BackgroundParameters
from deep_image_ai_client.models.color_parameters import ColorParameters
from deep_image_ai_client.models.deblur_parameters import DeblurParameters
from deep_image_ai_client.models.denoise_parameters import DenoiseParameters
from deep_image_ai_client.models.enhancement_types import EnhancementTypes
from deep_image_ai_client.models.fit_type import FitType
from deep_image_ai_client.models.height import Height
from deep_image_ai_client.models.light_parameters import LightParameters
from deep_image_ai_client.models.output_format import OutputFormat
from deep_image_ai_client.models.padding import Padding
from deep_image_ai_client.models.preset import Preset
from deep_image_ai_client.models.print_size import PrintSize
from deep_image_ai_client.models.white_balance_parameters import WhiteBalanceParameters
from deep_image_ai_client.models.width import Width
from typing import Optional, Set
from typing_extensions import Self

class RestApiProcessResultPostRequestParameters(BaseModel):
    """
    RestApiProcessResultPostRequestParameters
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="Image url, Base64 encoded image or storage url (storage://{storage_name}/{?path})")
    target: Optional[StrictStr] = None
    width: Optional[Width] = None
    height: Optional[Height] = None
    min_length: Optional[StrictInt] = Field(default=None, description="Integer f.e. - 200 - it will upscale/downscale image to have minimum 200 pixels width or height. That will also be applied to identified item/content when removing background.")
    padding: Optional[Padding] = None
    fit: Optional[FitType] = None
    enhancements: Optional[List[EnhancementTypes]] = None
    background: Optional[BackgroundParameters] = None
    preset: Optional[Preset] = None
    output_format: Optional[OutputFormat] = None
    max_file_size: Optional[StrictStr] = Field(default=None, description="Integer or string value with maximum file size. It supports \"kb\", \"mb\" and \"gb\" units. It is used with output_format equals jpeg or webp. When specified, Deep Image API tries to match highest possible jpeg quality and specified max_file_size.")
    quality: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=85, description="Integer value for the level of jpeg or webp compression.")
    dpi: Optional[StrictInt] = Field(default=300, description="To use the dpi effectively, the ***print_size*** needs to be sent along with it. ")
    print_size: Optional[PrintSize] = None
    print_reorientation: Optional[StrictBool] = Field(default=True, description="true/false - swap target width and height values to match paper size orientation.")
    denoise_parameters: Optional[DenoiseParameters] = None
    deblur_parameters: Optional[DeblurParameters] = None
    light_parameters: Optional[LightParameters] = None
    color_parameters: Optional[ColorParameters] = None
    white_balance_parameters: Optional[WhiteBalanceParameters] = None
    __properties: ClassVar[List[str]] = ["url", "target", "width", "height", "min_length", "padding", "fit", "enhancements", "background", "preset", "output_format", "max_file_size", "quality", "dpi", "print_size", "print_reorientation", "denoise_parameters", "deblur_parameters", "light_parameters", "color_parameters", "white_balance_parameters"]

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
        """Create an instance of RestApiProcessResultPostRequestParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of width
        if self.width:
            _dict['width'] = self.width.to_dict()
        # override the default output from pydantic by calling `to_dict()` of height
        if self.height:
            _dict['height'] = self.height.to_dict()
        # override the default output from pydantic by calling `to_dict()` of padding
        if self.padding:
            _dict['padding'] = self.padding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fit
        if self.fit:
            _dict['fit'] = self.fit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of background
        if self.background:
            _dict['background'] = self.background.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preset
        if self.preset:
            _dict['preset'] = self.preset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of denoise_parameters
        if self.denoise_parameters:
            _dict['denoise_parameters'] = self.denoise_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deblur_parameters
        if self.deblur_parameters:
            _dict['deblur_parameters'] = self.deblur_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of light_parameters
        if self.light_parameters:
            _dict['light_parameters'] = self.light_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of color_parameters
        if self.color_parameters:
            _dict['color_parameters'] = self.color_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of white_balance_parameters
        if self.white_balance_parameters:
            _dict['white_balance_parameters'] = self.white_balance_parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestApiProcessResultPostRequestParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "target": obj.get("target"),
            "width": Width.from_dict(obj["width"]) if obj.get("width") is not None else None,
            "height": Height.from_dict(obj["height"]) if obj.get("height") is not None else None,
            "min_length": obj.get("min_length"),
            "padding": Padding.from_dict(obj["padding"]) if obj.get("padding") is not None else None,
            "fit": FitType.from_dict(obj["fit"]) if obj.get("fit") is not None else None,
            "enhancements": obj.get("enhancements"),
            "background": BackgroundParameters.from_dict(obj["background"]) if obj.get("background") is not None else None,
            "preset": Preset.from_dict(obj["preset"]) if obj.get("preset") is not None else None,
            "output_format": obj.get("output_format"),
            "max_file_size": obj.get("max_file_size"),
            "quality": obj.get("quality") if obj.get("quality") is not None else 85,
            "dpi": obj.get("dpi") if obj.get("dpi") is not None else 300,
            "print_size": obj.get("print_size"),
            "print_reorientation": obj.get("print_reorientation") if obj.get("print_reorientation") is not None else True,
            "denoise_parameters": DenoiseParameters.from_dict(obj["denoise_parameters"]) if obj.get("denoise_parameters") is not None else None,
            "deblur_parameters": DeblurParameters.from_dict(obj["deblur_parameters"]) if obj.get("deblur_parameters") is not None else None,
            "light_parameters": LightParameters.from_dict(obj["light_parameters"]) if obj.get("light_parameters") is not None else None,
            "color_parameters": ColorParameters.from_dict(obj["color_parameters"]) if obj.get("color_parameters") is not None else None,
            "white_balance_parameters": WhiteBalanceParameters.from_dict(obj["white_balance_parameters"]) if obj.get("white_balance_parameters") is not None else None
        })
        return _obj


