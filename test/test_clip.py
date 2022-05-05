"""
    Shotstack

    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON and a RESTful API.  You arrange and configure an edit and POST it to the API which will render your media and provide a file  location when complete.  For more details visit [shotstack.io](https://shotstack.io) or checkout our [getting started](https://shotstack.gitbook.io/docs/guides/getting-started) documentation. There are two main API's, one for editing and generating assets (Edit API) and one for managing hosted assets (Serve API).  The Edit API base URL is: <b>https://api.shotstack.io/{version}</b>  The Serve API base URL is: <b>https://api.shotstack.io/serve/{version}</b>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import shotstack_sdk
from shotstack_sdk.model.audio_asset import AudioAsset
from shotstack_sdk.model.html_asset import HtmlAsset
from shotstack_sdk.model.image_asset import ImageAsset
from shotstack_sdk.model.luma_asset import LumaAsset
from shotstack_sdk.model.offset import Offset
from shotstack_sdk.model.title_asset import TitleAsset
from shotstack_sdk.model.transformation import Transformation
from shotstack_sdk.model.transition import Transition
from shotstack_sdk.model.video_asset import VideoAsset
globals()['AudioAsset'] = AudioAsset
globals()['HtmlAsset'] = HtmlAsset
globals()['ImageAsset'] = ImageAsset
globals()['LumaAsset'] = LumaAsset
globals()['Offset'] = Offset
globals()['TitleAsset'] = TitleAsset
globals()['Transformation'] = Transformation
globals()['Transition'] = Transition
globals()['VideoAsset'] = VideoAsset
from shotstack_sdk.model.clip import Clip


class TestClip(unittest.TestCase):
    """Clip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClip(self):
        """Test Clip"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Clip()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
