# ProcessPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Image url, Base64 encoded image or storage url (storage://{storage_name}/{?path}) | [optional] 
**target** | **str** |  | [optional] 
**width** | [**Width**](Width.md) |  | [optional] 
**height** | [**Height**](Height.md) |  | [optional] 
**min_length** | **int** | Integer f.e. - 200 - it will upscale/downscale image to have minimum 200 pixels width or height. That will also be applied to identified item/content when removing background. | [optional] 
**padding** | [**Padding**](Padding.md) |  | [optional] 
**fit** | [**FitType**](FitType.md) |  | [optional] 
**enhancements** | [**List[EnhancementTypes]**](EnhancementTypes.md) |  | [optional] 
**background** | [**BackgroundParameters**](BackgroundParameters.md) |  | [optional] 
**preset** | [**Preset**](Preset.md) |  | [optional] 
**output_format** | [**OutputFormat**](OutputFormat.md) |  | [optional] 
**max_file_size** | **str** | Integer or string value with maximum file size. It supports \&quot;kb\&quot;, \&quot;mb\&quot; and \&quot;gb\&quot; units. It is used with output_format equals jpeg or webp. When specified, Deep Image API tries to match highest possible jpeg quality and specified max_file_size. | [optional] 
**quality** | **int** | Integer value for the level of jpeg or webp compression. | [optional] [default to 85]
**dpi** | **int** | To use the dpi effectively, the ***print_size*** needs to be sent along with it.  | [optional] [default to 300]
**print_size** | [**PrintSize**](PrintSize.md) |  | [optional] 
**print_reorientation** | **bool** | true/false - swap target width and height values to match paper size orientation. | [optional] [default to True]
**denoise_parameters** | [**DenoiseParameters**](DenoiseParameters.md) |  | [optional] 
**deblur_parameters** | [**DeblurParameters**](DeblurParameters.md) |  | [optional] 
**light_parameters** | [**LightParameters**](LightParameters.md) |  | [optional] 
**color_parameters** | [**ColorParameters**](ColorParameters.md) |  | [optional] 
**white_balance_parameters** | [**WhiteBalanceParameters**](WhiteBalanceParameters.md) |  | [optional] 

## Example

```python
from deep_image_ai_client.models.process_payload import ProcessPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessPayload from a JSON string
process_payload_instance = ProcessPayload.from_json(json)
# print the JSON string representation of the object
print(ProcessPayload.to_json())

# convert the object into a dict
process_payload_dict = process_payload_instance.to_dict()
# create an instance of ProcessPayload from a dict
process_payload_form_dict = process_payload.from_dict(process_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


