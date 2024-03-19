# FitType

- canvas - Whole image is placed into width x height canvas, missing space is filled with background color. - crop - Image is cropped to match destination width x height canvas. Crop is content aware by default. It can be changed to be on center as well. - bounds - Image is upscaled to fit specified width x height. - cover - Image is upscaled to fully cover specified width x height. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crop** | [**CropTypes**](CropTypes.md) |  | 

## Example

```python
from deep_image_ai_client.models.fit_type import FitType

# TODO update the JSON string below
json = "{}"
# create an instance of FitType from a JSON string
fit_type_instance = FitType.from_json(json)
# print the JSON string representation of the object
print(FitType.to_json())

# convert the object into a dict
fit_type_dict = fit_type_instance.to_dict()
# create an instance of FitType from a dict
fit_type_form_dict = fit_type.from_dict(fit_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


