# deep_image_ai_client.DefaultApi

All URIs are relative to *https://deep-image.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_api_process_post**](DefaultApi.md#rest_api_process_post) | **POST** /rest_api/process | Schedules a job to perform selected enhancement options.
[**rest_api_process_result_post**](DefaultApi.md#rest_api_process_result_post) | **POST** /rest_api/process_result | Schedules a job to perform selected enhancement options and waits for the result.
[**rest_api_result_hash_get**](DefaultApi.md#rest_api_result_hash_get) | **GET** /rest_api/result/{hash} | Returns processing job result.


# **rest_api_process_post**
> ProcessResult rest_api_process_post(process_payload)

Schedules a job to perform selected enhancement options.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import deep_image_ai_client
from deep_image_ai_client.models.process_payload import ProcessPayload
from deep_image_ai_client.models.process_result import ProcessResult
from deep_image_ai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://deep-image.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_image_ai_client.Configuration(
    host = "https://deep-image.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_image_ai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_image_ai_client.DefaultApi(api_client)
    process_payload = {"url":"https://deep-image.ai/api-example2.jpg","width":"200%","height":"200%"} # ProcessPayload | 

    try:
        # Schedules a job to perform selected enhancement options.
        api_response = api_instance.rest_api_process_post(process_payload)
        print("The response of DefaultApi->rest_api_process_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rest_api_process_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_payload** | [**ProcessPayload**](ProcessPayload.md)|  | 

### Return type

[**ProcessResult**](ProcessResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns processing result |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Job Processing Failed |  -  |
**5XX** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_api_process_result_post**
> ProcessResult rest_api_process_result_post(process_payload)

Schedules a job to perform selected enhancement options and waits for the result.

It's convenient method that returns the url to the result immediately if the processing time is less than 25 seconds. Otherwise it will return a job hash and the result will be available via \"result\" method.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import deep_image_ai_client
from deep_image_ai_client.models.process_payload import ProcessPayload
from deep_image_ai_client.models.process_result import ProcessResult
from deep_image_ai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://deep-image.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_image_ai_client.Configuration(
    host = "https://deep-image.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_image_ai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_image_ai_client.DefaultApi(api_client)
    process_payload = {"url":"https://deep-image.ai/api-example2.jpg","width":"200%","height":"200%"} # ProcessPayload | 

    try:
        # Schedules a job to perform selected enhancement options and waits for the result.
        api_response = api_instance.rest_api_process_result_post(process_payload)
        print("The response of DefaultApi->rest_api_process_result_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rest_api_process_result_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_payload** | [**ProcessPayload**](ProcessPayload.md)|  | 

### Return type

[**ProcessResult**](ProcessResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns processing result |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Job Processing Failed |  -  |
**5XX** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_api_result_hash_get**
> ProcessResult rest_api_result_hash_get(hash)

Returns processing job result.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import deep_image_ai_client
from deep_image_ai_client.models.process_result import ProcessResult
from deep_image_ai_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://deep-image.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_image_ai_client.Configuration(
    host = "https://deep-image.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_image_ai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_image_ai_client.DefaultApi(api_client)
    hash = 'hash_example' # str | 

    try:
        # Returns processing job result.
        api_response = api_instance.rest_api_result_hash_get(hash)
        print("The response of DefaultApi->rest_api_result_hash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rest_api_result_hash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  | 

### Return type

[**ProcessResult**](ProcessResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns processing result |  -  |
**404** | Not Found |  -  |
**500** | Job Processing Failed |  -  |
**5XX** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

