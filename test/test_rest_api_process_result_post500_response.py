# coding: utf-8

"""
    Deep Image

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deep_image_ai_client.models.rest_api_process_result_post500_response import RestApiProcessResultPost500Response

class TestRestApiProcessResultPost500Response(unittest.TestCase):
    """RestApiProcessResultPost500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestApiProcessResultPost500Response:
        """Test RestApiProcessResultPost500Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestApiProcessResultPost500Response`
        """
        model = RestApiProcessResultPost500Response()
        if include_optional:
            return RestApiProcessResultPost500Response(
                message = '',
                status = '',
                job = ''
            )
        else:
            return RestApiProcessResultPost500Response(
                status = '',
                job = '',
        )
        """

    def testRestApiProcessResultPost500Response(self):
        """Test RestApiProcessResultPost500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
