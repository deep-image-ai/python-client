# ColorParameters

To use the color parameters effectively, the ***[color](https://documentation.deep-image.ai/image-processing/enhance-lighting-and-colors)*** enhancement needs to be sent along with it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ColorEnhancementTypes**](ColorEnhancementTypes.md) |  | [optional] 
**level** | **float** |  | [optional] [default to 1]

## Example

```python
from deep_image_ai_client.models.color_parameters import ColorParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ColorParameters from a JSON string
color_parameters_instance = ColorParameters.from_json(json)
# print the JSON string representation of the object
print(ColorParameters.to_json())

# convert the object into a dict
color_parameters_dict = color_parameters_instance.to_dict()
# create an instance of ColorParameters from a dict
color_parameters_form_dict = color_parameters.from_dict(color_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


