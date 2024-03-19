# LightParameters

To use the light parameters effectively, the ***[light](https://documentation.deep-image.ai/image-processing/enhance-lighting-and-colors)*** enhancement needs to be sent along with it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LightEnhancementTypes**](LightEnhancementTypes.md) |  | [optional] 
**level** | **float** |  | [optional] [default to 1]

## Example

```python
from deep_image_ai_client.models.light_parameters import LightParameters

# TODO update the JSON string below
json = "{}"
# create an instance of LightParameters from a JSON string
light_parameters_instance = LightParameters.from_json(json)
# print the JSON string representation of the object
print(LightParameters.to_json())

# convert the object into a dict
light_parameters_dict = light_parameters_instance.to_dict()
# create an instance of LightParameters from a dict
light_parameters_form_dict = light_parameters.from_dict(light_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


