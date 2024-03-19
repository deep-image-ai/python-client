# DeblurParameters

To use the deblur parameters effectively, the ***[deblur](https://documentation.deep-image.ai/image-processing/enhance-details)*** enhancement needs to be sent along with it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeblurEnhancementModelTypes**](DeblurEnhancementModelTypes.md) |  | [optional] 

## Example

```python
from deep_image_ai_client.models.deblur_parameters import DeblurParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeblurParameters from a JSON string
deblur_parameters_instance = DeblurParameters.from_json(json)
# print the JSON string representation of the object
print(DeblurParameters.to_json())

# convert the object into a dict
deblur_parameters_dict = deblur_parameters_instance.to_dict()
# create an instance of DeblurParameters from a dict
deblur_parameters_form_dict = deblur_parameters.from_dict(deblur_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


