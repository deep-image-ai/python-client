# GenerateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**item_area_percentage** | **float** |  | [optional] [default to 1]
**sample_num** | **int** |  | [optional] 
**color** | **str** | E.g. rgb(red, green, blue), #rrggbbaa, hsl(hue, saturation%, lightness%), hsv(hue, saturation%, value%) and common HTML color names. | [optional] 
**additional_prompt** | **str** |  | [optional] 
**negative_prompt** | **str** |  | [optional] 
**adapter_type** | [**GenerateAdapterTypes**](GenerateAdapterTypes.md) |  | [optional] 

## Example

```python
from deep_image_ai_client.models.generate_parameters import GenerateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateParameters from a JSON string
generate_parameters_instance = GenerateParameters.from_json(json)
# print the JSON string representation of the object
print(GenerateParameters.to_json())

# convert the object into a dict
generate_parameters_dict = generate_parameters_instance.to_dict()
# create an instance of GenerateParameters from a dict
generate_parameters_form_dict = generate_parameters.from_dict(generate_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


