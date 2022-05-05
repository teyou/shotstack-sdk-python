"""
    Shotstack

    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON and a RESTful API.  You arrange and configure an edit and POST it to the API which will render your media and provide a file  location when complete.  For more details visit [shotstack.io](https://shotstack.io) or checkout our [getting started](https://shotstack.gitbook.io/docs/guides/getting-started) documentation. There are two main API's, one for editing and generating assets (Edit API) and one for managing hosted assets (Serve API).  The Edit API base URL is: <b>https://api.shotstack.io/{version}</b>  The Serve API base URL is: <b>https://api.shotstack.io/serve/{version}</b>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import shotstack_sdk
from shotstack_sdk.model.shotstack_destination import ShotstackDestination


class TestShotstackDestination(unittest.TestCase):
    """ShotstackDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testShotstackDestination(self):
        """Test ShotstackDestination"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ShotstackDestination()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
