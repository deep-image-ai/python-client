# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deep_image_ai_client.models.process_payload import ProcessPayload

class TestProcessPayload(unittest.TestCase):
    """ProcessPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessPayload:
        """Test ProcessPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessPayload`
        """
        model = ProcessPayload()
        if include_optional:
            return ProcessPayload(
                url = 'https://deep-image.ai/api-example2.jpg',
                target = 'storage://{storage_name}/{?path}',
                width = None,
                height = None,
                min_length = 56,
                padding = None,
                fit = None,
                enhancements = [
                    'denoise'
                    ],
                background = deep_image_ai_client.models.background_parameters.BackgroundParameters(
                    remove = 'auto', 
                    color = 'white', 
                    replace = 'https://deep-image.ai/api-example2.jpg', 
                    generate = deep_image_ai_client.models.generate_parameters.GenerateParameters(
                        description = '', 
                        item_area_percentage = 0.5, 
                        sample_num = 56, 
                        color = 'white', 
                        additional_prompt = '', 
                        negative_prompt = '', 
                        adapter_type = 'generate_background', ), ),
                preset = None,
                output_format = 'jpeg',
                max_file_size = '1MB',
                quality = 50,
                dpi = 56,
                print_size = 'a4',
                print_reorientation = True,
                denoise_parameters = deep_image_ai_client.models.denoise_parameters.DenoiseParameters(
                    type = 'v1', ),
                deblur_parameters = deep_image_ai_client.models.deblur_parameters.DeblurParameters(
                    type = 'v1', ),
                light_parameters = deep_image_ai_client.models.light_parameters.LightParameters(
                    type = 'contrast', 
                    level = 0, ),
                color_parameters = deep_image_ai_client.models.color_parameters.ColorParameters(
                    type = 'contrast', 
                    level = 0, ),
                white_balance_parameters = deep_image_ai_client.models.white_balance_parameters.WhiteBalanceParameters(
                    level = 0, )
            )
        else:
            return ProcessPayload(
        )
        """

    def testProcessPayload(self):
        """Test ProcessPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
