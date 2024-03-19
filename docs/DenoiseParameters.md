# DenoiseParameters

To use the denoise parameters effectively, the ***[denoise](https://documentation.deep-image.ai/image-processing/enhance-details)*** enhancement needs to be sent along with it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DenoiseEnhancementModelTypes**](DenoiseEnhancementModelTypes.md) |  | [optional] 

## Example

```python
from deep_image_ai_client.models.denoise_parameters import DenoiseParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DenoiseParameters from a JSON string
denoise_parameters_instance = DenoiseParameters.from_json(json)
# print the JSON string representation of the object
print(DenoiseParameters.to_json())

# convert the object into a dict
denoise_parameters_dict = denoise_parameters_instance.to_dict()
# create an instance of DenoiseParameters from a dict
denoise_parameters_form_dict = denoise_parameters.from_dict(denoise_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


