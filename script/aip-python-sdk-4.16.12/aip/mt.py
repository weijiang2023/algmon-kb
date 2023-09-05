
# -*- coding: utf-8 -*-

"""
机器翻译
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

class AipMt(AipBase):
    """
    机器翻译
    """

    __pictransV1Url = 'https://aip.baidubce.com/file/2.0/mt/pictrans/v1'
    __texttransV1Url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1'
    __texttransWithDictV1Url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans-with-dict/v1'
    __docTranslationCreateV2Url = 'https://aip.baidubce.com/rpc/2.0/mt/v2/doc-translation/create'
    __docTranslationQueryV2Url = 'https://aip.baidubce.com/rpc/2.0/mt/v2/doc-translation/query'
    __speechTranslationV2Url = 'https://aip.baidubce.com/rpc/2.0/mt/v2/speech-translation'


    def texttransV1(self, languageFrom, to, q, options=None):
        """
            文本翻译-通用版
            接口使用说明文档: https://ai.baidu.com/ai-doc/MT/4kqryjku9
        """
        options = options or {}
        data = {}
        data['from'] = languageFrom
        data['to'] = to
        data['q'] = q
        data.update(options)
        return self._request(self.__texttransV1Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def texttransWithDictV1(self, languageFrom, to, q, options=None):
        """
            文本翻译-词典版
            接口使用说明文档: https://ai.baidu.com/ai-doc/MT/nkqrzmbpc
        """
        options = options or {}
        data = {}
        data['from'] = languageFrom
        data['to'] = to
        data['q'] = q
        data.update(options)
        return self._request(self.__texttransWithDictV1Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def docTranslationCreateV2(self, languageFrom, to, input, options=None):
        """
            文档翻译
            接口使用说明文档: https://ai.baidu.com/ai-doc/MT/Xky9x5xub
        """
        options = options or {}
        data = {}
        data['languageFrom'] = languageFrom
        data['to'] = to
        data['input'] = input
        data.update(options)
        return self._request(self.__docTranslationCreateV2Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def docTranslationQueryV2(self, id, options=None):
        """
            文档翻译-文档状态查询
            接口使用说明文档: https://ai.baidu.com/ai-doc/MT/Xky9x5xub
        """
        options = options or {}
        data = {}
        data['id'] = id
        data.update(options)
        return self._request(self.__docTranslationQueryV2Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def speechTranslationV2(self, languageFrom, to, voice, format, options=None):
        """
            语音翻译
            接口使用说明文档: https://ai.baidu.com/ai-doc/MT/el4cmi76f
        """
        options = options or {}
        data = {}
        data['from'] = languageFrom
        data['to'] = to
        data['voice'] = base64.b64encode(voice).decode()
        data['format'] = format
        data.update(options)
        return self._request(self.__speechTranslationV2Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    