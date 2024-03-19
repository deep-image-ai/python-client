# BackgroundParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove** | [**BackgroundRemoveTypes**](BackgroundRemoveTypes.md) |  | [optional] 
**color** | **str** | E.g. rgb(red, green, blue), #rrggbbaa, hsl(hue, saturation%, lightness%), hsv(hue, saturation%, value%) and common HTML color names. | [optional] 
**replace** | **str** | Image url, Base64 encoded image or storage url (storage://{storage_name}/{?path}) | [optional] 
**generate** | [**GenerateParameters**](GenerateParameters.md) |  | [optional] 

## Example

```python
from deep_image_ai_client.models.background_parameters import BackgroundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundParameters from a JSON string
background_parameters_instance = BackgroundParameters.from_json(json)
# print the JSON string representation of the object
print(BackgroundParameters.to_json())

# convert the object into a dict
background_parameters_dict = background_parameters_instance.to_dict()
# create an instance of BackgroundParameters from a dict
background_parameters_form_dict = background_parameters.from_dict(background_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


