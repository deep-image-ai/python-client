# Height

- string f.e. - \"200%\" - it will upscale image by factor 2. - integer f.e. - 200 - it will upscale/downscale image to have height 200 pixels. If the width is not given it will be calculated to match image ratio. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deep_image_ai_client.models.height import Height

# TODO update the JSON string below
json = "{}"
# create an instance of Height from a JSON string
height_instance = Height.from_json(json)
# print the JSON string representation of the object
print(Height.to_json())

# convert the object into a dict
height_dict = height_instance.to_dict()
# create an instance of Height from a dict
height_form_dict = height.from_dict(height_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


