# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deep_image_ai_client.models.light_parameters import LightParameters

class TestLightParameters(unittest.TestCase):
    """LightParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LightParameters:
        """Test LightParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LightParameters`
        """
        model = LightParameters()
        if include_optional:
            return LightParameters(
                type = 'contrast',
                level = 0
            )
        else:
            return LightParameters(
        )
        """

    def testLightParameters(self):
        """Test LightParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
