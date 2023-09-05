# -*- coding: utf-8 -*-

"""
人体分析
"""

import re
import sys
import math
import time
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote

class AipBodyAnalysis(AipBase):

    """
    人体分析
    """

    __bodyAnalysisUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis'

    __bodyAttrUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr'

    __bodyNumUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num'

    __gestureUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture'

    __bodySegUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg'

    __driverBehaviorUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior'

    __bodyTrackingUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking'

    __handAnalysisUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/hand_analysis'

    __bodyDangerV1Url = 'https://aip.baidubce.com/rest/2.0/video-classify/v1/body_danger'
    __fingertipV1Url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/fingertip'
    
    def bodyAnalysis(self, image, options=None):
        """
            人体关键点识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyAnalysisUrl, data)
    
    def bodyAttr(self, image, options=None):
        """
            人体检测与属性识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyAttrUrl, data)
    
    def bodyNum(self, image, options=None):
        """
            人流量统计
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyNumUrl, data)
    
    def gesture(self, image, options=None):
        """
            手势识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__gestureUrl, data)
    
    def bodySeg(self, image, options=None):
        """
            人像分割
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodySegUrl, data)
    
    def driverBehavior(self, image, options=None):
        """
            驾驶行为分析
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__driverBehaviorUrl, data)
    
    def bodyTracking(self, image, dynamic, options=None):
        """
            人流量统计-动态版
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['dynamic'] = dynamic

        data.update(options)

        return self._request(self.__bodyTrackingUrl, data)
    
    def handAnalysis(self, image, options=None):
        """
            手部关键点识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__handAnalysisUrl, data)
    
    def bodyDangerV1(self, videoData, options=None):
        """
            危险行为识别
            接口使用说明文档: https://ai.baidu.com/ai-doc/BODY/uk3cpywke
        """
        options = options or {}
        data = {}
        data['data'] = base64.b64encode(videoData).decode()
        data.update(options)
        return self._request(self.__bodyDangerV1Url, data)

    def fingertipV1(self, image, options=None):
        """
            指尖检测
            接口使用说明文档: https://ai.baidu.com/ai-doc/BODY/Jk7ir38ut
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__fingertipV1Url, data)
