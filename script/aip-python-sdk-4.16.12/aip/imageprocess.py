# -*- coding: utf-8 -*-

"""
图像处理
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

class AipImageProcess(AipBase):

    """
    图像处理
    """

    __imageQualityEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/image_quality_enhance'

    __dehazeUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze'

    __contrastEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/contrast_enhance'

    __colourizeUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/colourize'

    __stretchRestoreUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/stretch_restore'

    __styleTrans = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"

    __inpainting = "https://aip.baidubce.com/rest/2.0/image-process/v1/inpainting"

    __imageDefinitionEnhance = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"

    __selfieAnime = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"

    __skySeg = "https://aip.baidubce.com/rest/2.0/image-process/v1/sky_seg"

    __colorEnhances = "https://aip.baidubce.com/rest/2.0/image-process/v1/color_enhance"

    __removeMoireV1Url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/remove_moire'
    __customizeStylizationV1Url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/customize_stylization'
    __docRepairV1Url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/doc_repair'
    __denoiseV1Url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/denoise'



    def imageQualityEnhance(self, image, options=None):
        """
            图像无损放大
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__imageQualityEnhanceUrl, data)
    
    def dehaze(self, image, options=None):
        """
            图像去雾
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__dehazeUrl, data)
    
    def contrastEnhance(self, image, options=None):
        """
            图像对比度增强
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__contrastEnhanceUrl, data)
    
    def colourize(self, image, options=None):
        """
            黑白图像上色
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__colourizeUrl, data)
    
    def stretchRestore(self, image, options=None):
        """
            拉伸图像恢复
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__stretchRestoreUrl, data)


    def selfieAnime(self, image, options=None):
        """
            人像动漫化
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__selfieAnime, data)

    def imageDefinitionEnhance(self, image, options=None):
        """
            图像清晰度增强
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__imageDefinitionEnhance, data)

    def styleTrans(self, image, options=None):
        """
            图像风格转换
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__styleTrans, data)


    def skySeg(self, image, options=None):
        """
            天空分割
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__skySeg, data)

    def inpaintingByMask(self, image, rectangle, options=None):
        """
            图像修复
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['rectangle'] = rectangle
        data.update(options)
        return self._request(self.__inpainting, data)


    def removeMoireV1(self, image, options=None):
        """
            图片去摩尔纹
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/ql4wdlnc0
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__removeMoireV1Url, data)

    def removeMoireV1Url(self, url, options=None):
        """
            图片去摩尔纹 - url
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/ql4wdlnc0
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__removeMoireV1Url, data)

    def removeMoireV1Pdf(self, pdf, options=None):
        """
            图片去摩尔纹 - pdf
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/ql4wdlnc0
        """
        options = options or {}
        data = {}
        data['pdf_file'] = base64.b64encode(pdf).decode()
        data.update(options)
        return self._request(self.__removeMoireV1Url, data)

    def customizeStylizationV1(self, image, options=None):
        """
            图像风格自定义
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/al50vf6bq
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customizeStylizationV1Url, data)

    def customizeStylizationV1Url(self, url, options=None):
        """
            图像风格自定义 - url
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/al50vf6bq
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__customizeStylizationV1Url, data)

    def docRepairV1(self, image, options=None):
        """
            文档图片去底纹
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/Nl6os53ab
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__docRepairV1Url, data)

    def docRepairV1Url(self, url, options=None):
        """
            文档图片去底纹 - url
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/Nl6os53ab
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__docRepairV1Url, data)

    def denoiseV1(self, image, option, options=None):
        """
            图像去噪
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/Tl78sby7g
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['option'] = option
        data.update(options)
        return self._request(self.__denoiseV1Url, data)

    def denoiseV1Url(self, url, option, options=None):
        """
            图像去噪 - url
            接口使用说明文档: https://ai.baidu.com/ai-doc/IMAGEPROCESS/Tl78sby7g
        """
        options = options or {}
        data = {}
        data['url'] = url
        data['option'] = option
        data.update(options)
        return self._request(self.__denoiseV1Url, data)
