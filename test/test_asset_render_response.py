"""
    Shotstack

    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON and a RESTful API.  You arrange and configure an edit and POST it to the API which will render your media and provide a file  location when complete.  For more details visit [shotstack.io](https://shotstack.io) or checkout our [getting started](https://shotstack.gitbook.io/docs/guides/getting-started) documentation. There are two main API's, one for editing and generating assets (Edit API) and one for managing hosted assets (Serve API).  The Edit API base URL is: <b>https://api.shotstack.io/{version}</b>  The Serve API base URL is: <b>https://api.shotstack.io/serve/{version}</b>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import shotstack_sdk
from shotstack_sdk.model.asset_response_data import AssetResponseData
globals()['AssetResponseData'] = AssetResponseData
from shotstack_sdk.model.asset_render_response import AssetRenderResponse


class TestAssetRenderResponse(unittest.TestCase):
    """AssetRenderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAssetRenderResponse(self):
        """Test AssetRenderResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AssetRenderResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
