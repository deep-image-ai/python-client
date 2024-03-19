# WhiteBalanceParameters

To use the white balance parameters effectively, the ***[white_balance](https://documentation.deep-image.ai/image-processing/enhance-lighting-and-colors)*** enhancement needs to be sent along with it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** |  | [optional] [default to 1]

## Example

```python
from deep_image_ai_client.models.white_balance_parameters import WhiteBalanceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteBalanceParameters from a JSON string
white_balance_parameters_instance = WhiteBalanceParameters.from_json(json)
# print the JSON string representation of the object
print(WhiteBalanceParameters.to_json())

# convert the object into a dict
white_balance_parameters_dict = white_balance_parameters_instance.to_dict()
# create an instance of WhiteBalanceParameters from a dict
white_balance_parameters_form_dict = white_balance_parameters.from_dict(white_balance_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


