# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deep_image_ai_client.models.color_parameters import ColorParameters

class TestColorParameters(unittest.TestCase):
    """ColorParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ColorParameters:
        """Test ColorParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ColorParameters`
        """
        model = ColorParameters()
        if include_optional:
            return ColorParameters(
                type = 'contrast',
                level = 0
            )
        else:
            return ColorParameters(
        )
        """

    def testColorParameters(self):
        """Test ColorParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()