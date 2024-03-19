# Width

- string f.e. - \"200%\" - it will upscale image by factor 2. - integer f.e. - 200 - it will upscale/downscale image to have width 200 pixels. If the height is not given it will be calculated to match image ratio. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deep_image_ai_client.models.width import Width

# TODO update the JSON string below
json = "{}"
# create an instance of Width from a JSON string
width_instance = Width.from_json(json)
# print the JSON string representation of the object
print(Width.to_json())

# convert the object into a dict
width_dict = width_instance.to_dict()
# create an instance of Width from a dict
width_form_dict = width.from_dict(width_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


