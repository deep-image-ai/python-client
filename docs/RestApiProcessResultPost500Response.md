# RestApiProcessResultPost500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | 
**job** | **str** |  | 

## Example

```python
from deep_image_ai_client.models.rest_api_process_result_post500_response import RestApiProcessResultPost500Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestApiProcessResultPost500Response from a JSON string
rest_api_process_result_post500_response_instance = RestApiProcessResultPost500Response.from_json(json)
# print the JSON string representation of the object
print(RestApiProcessResultPost500Response.to_json())

# convert the object into a dict
rest_api_process_result_post500_response_dict = rest_api_process_result_post500_response_instance.to_dict()
# create an instance of RestApiProcessResultPost500Response from a dict
rest_api_process_result_post500_response_form_dict = rest_api_process_result_post500_response.from_dict(rest_api_process_result_post500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


