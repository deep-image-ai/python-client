# ProcessResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**result_url** | **str** |  | [optional] 
**job** | **str** |  | 

## Example

```python
from deep_image_ai_client.models.process_result import ProcessResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessResult from a JSON string
process_result_instance = ProcessResult.from_json(json)
# print the JSON string representation of the object
print(ProcessResult.to_json())

# convert the object into a dict
process_result_dict = process_result_instance.to_dict()
# create an instance of ProcessResult from a dict
process_result_form_dict = process_result.from_dict(process_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


