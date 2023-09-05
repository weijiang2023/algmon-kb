
# -*- coding: utf-8 -*-

"""
人脸识别
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

class AipFace(AipBase):

    """
    人脸识别
    """

    __detectUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'

    __searchUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/search'

    __multiSearchUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/multi-search'

    __userAddUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add'

    __userUpdateUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update'

    __faceDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete'

    __userGetUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get'

    __faceGetlistUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist'

    __groupGetusersUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers'

    __userCopyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/copy'

    __userDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete'

    __groupAddUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add'

    __groupDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete'

    __groupGetlistUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist'

    __personVerifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/person/verify'

    __videoSessioncodeUrl = 'https://aip.baidubce.com/rest/2.0/face/v1/faceliveness/sessioncode'

    __verifyUrl = "https://aip.baidubce.com/rest/2.0/face/v4/mingjing/verify"

    __faceMatchUrlV4 = 'https://aip.baidubce.com/rest/2.0/face/v4/mingjing/match'

    __onlinePictureLiveV4 = 'https://aip.baidubce.com/rest/2.0/face/v4/faceverify'

    __facelivenessVerifyV1Url = 'https://aip.baidubce.com/rest/2.0/face/v1/faceliveness/verify'
    __facePersonIdmatchV3Url = 'https://aip.baidubce.com/rest/2.0/face/v3/person/idmatch'
    __faceMergeV1Url = 'https://aip.baidubce.com/rest/2.0/face/v1/merge'
    __faceSkinSmoothV1Url = 'https://aip.baidubce.com/rest/2.0/face/v1/editattr'
    __faceLandmarkV1Url = 'https://aip.baidubce.com/rest/2.0/face/v1/landmark'
    __faceSceneFacesetUserAddUrl = 'https://aip.baidubce.com/rest/2.0/face/scene/faceset/user/add'
    __faceSceneFacesetUserUpdateUrl = 'https://aip.baidubce.com/rest/2.0/face/scene/faceset/user/update'
    __faceSceneFacesetGroupAddUrl = 'https://aip.baidubce.com/rest/2.0/face/scene/faceset/group/add'
    __faceCaptureSearchUrl = 'https://aip.baidubce.com/rest/2.0/face/capture/search'
    __faceFaceverifyV4Url = 'https://aip.baidubce.com/rest/2.0/face/v4/faceverify'
    __faceMingjingVerifyV4Url = 'https://aip.baidubce.com/rest/2.0/face/v4/mingjing/verify'
    __faceMingjingMatchV4Url = 'https://aip.baidubce.com/rest/2.0/face/v4/mingjing/match'
    __faceIdmatchDateV4Url = 'https://aip.baidubce.com/rest/2.0/face/v4/idmatch_date'
    __faceVerifyDateV4Url = 'https://aip.baidubce.com/rest/2.0/face/v4/verify_date'


    def detect(self, image, image_type, options=None):
        """
            人脸检测
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type

        data.update(options)
        return self._request(self.__detectUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def search(self, image, image_type, group_id_list, options=None):
        """
            人脸搜索
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id_list'] = group_id_list

        data.update(options)
        return self._request(self.__searchUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def multiSearch(self, image, image_type, group_id_list, options=None):
        """
            人脸搜索 M:N 识别
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id_list'] = group_id_list

        data.update(options)
        return self._request(self.__multiSearchUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def addUser(self, image, image_type, group_id, user_id, options=None):
        """
            人脸注册
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)
        return self._request(self.__userAddUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def updateUser(self, image, image_type, group_id, user_id, options=None):
        """
            人脸更新
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)
        return self._request(self.__userUpdateUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def faceDelete(self, user_id, group_id, face_token, options=None):
        """
            人脸删除
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id
        data['face_token'] = face_token

        data.update(options)
        return self._request(self.__faceDeleteUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def getUser(self, user_id, group_id, options=None):
        """
            用户信息查询
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id

        data.update(options)
        return self._request(self.__userGetUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def faceGetlist(self, user_id, group_id, options=None):
        """
            获取用户人脸列表
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id

        data.update(options)
        return self._request(self.__faceGetlistUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def getGroupUsers(self, group_id, options=None):
        """
            获取用户列表
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)
        return self._request(self.__groupGetusersUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def userCopy(self, user_id, options=None):
        """
            复制用户
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id

        data.update(options)
        return self._request(self.__userCopyUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def deleteUser(self, group_id, user_id, options=None):
        """
            删除用户
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)
        return self._request(self.__userDeleteUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def groupAdd(self, group_id, options=None):
        """
            创建用户组
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)
        return self._request(self.__groupAddUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def groupDelete(self, group_id, options=None):
        """
            删除用户组
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)
        return self._request(self.__groupDeleteUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def getGroupList(self, options=None):
        """
            组列表查询
        """
        options = options or {}

        data = {}

        data.update(options)
        return self._request(self.__groupGetlistUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def personVerify(self, image, image_type, id_card_number, name, options=None):
        """
            身份验证
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['id_card_number'] = id_card_number
        data['name'] = name

        data.update(options)
        return self._request(self.__personVerifyUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    
    def videoSessioncode(self, options=None):
        """
            语音校验码接口
        """
        options = options or {}

        data = {}

        data.update(options)
        return self._request(self.__videoSessioncodeUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })
    

    __faceverifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify'

    def faceverify(self, images):
        """
            在线活体检测
        """

        return self._request(self.__faceverifyUrl, json.dumps(images, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    __matchUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/match'

    def match(self, images):
        """
            人脸比对
        """

        return self._request(self.__matchUrl, json.dumps(images, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceMingJingVerify(self, id_card_number, name, image, options=None):
        """
            人脸 - 人脸实名认证V4
        """
        options = options or {}

        data = {}
        data['id_card_number'] = id_card_number
        data['name'] = name
        data['image'] = image

        data.update(options)
        return self._request(self.__verifyUrl, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})

    def faceMingJingMatch(self, image, imageType, registerImage, registerImageType, options=None):
        """
            人脸 - 人脸对比V4
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = imageType
        data['register_image'] = registerImage
        data['register_image_type'] = registerImageType

        data.update(options)
        return self._request(self.__faceMatchUrlV4, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})

    def onlinePictureLiveV4(self, sdkVersion, options=None):
        """
            人脸 - 在线图片活体V4
        """
        options = options or {}

        data = {}
        data['sdk_version'] = sdkVersion

        data.update(options)
        return self._request(self.__onlinePictureLiveV4, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})


    def facelivenessVerifyV1(self, video_base64, options=None):
        """
            H5视频活体检测
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Ikrycq2k2#12-%E8%A7%86%E9%A2%91%E6%B4%BB%E4%BD%93%E6%A3%80%E6%B5%8B%E6%8E%A5%E5%8F%A3
        """
        options = options or {}
        data = {}
        data['video_base64'] = video_base64
        data.update(options)
        return self._request(self.__facelivenessVerifyV1Url, data)

    def facePersonIdmatchV3(self, id_card_number, name, options=None):
        """
            身份证与名字比对
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Tkqahnjtk
        """
        options = options or {}
        data = {}
        data['id_card_number'] = id_card_number
        data['name'] = name
        data.update(options)
        return self._request(self.__facePersonIdmatchV3Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceMergeV1(self, image_template, image_target, options=None):
        """
            人脸融合
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/5k37c1ti0
        """
        options = options or {}
        data = {}
        data['image_template'] = image_template
        data['image_target'] = image_target
        data.update(options)
        return self._request(self.__faceMergeV1Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceSkinSmoothV1(self, image, image_type, action_type, options=None):
        """
            人脸属性编辑
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/vk6rm5lj5
        """
        options = options or {}
        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['action_type'] = action_type
        data.update(options)
        return self._request(self.__faceSkinSmoothV1Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceLandmarkV1(self, image, image_type, options=None):
        """
            人脸关键点检测
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/sk8a5xewt
        """
        options = options or {}
        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data.update(options)
        return self._request(self.__faceLandmarkV1Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceSceneFacesetUserAdd(self, image, image_type, group_id, user_id, scene_type, options=None):
        """
            场景化（人脸注册）
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Aknhmx6hi#%E4%BA%BA%E8%84%B8%E5%BA%93%E7%AE%A1%E7%90%86%EF%BC%88%E5%9C%BA%E6%99%AF%E5%8C%96%EF%BC%89-%E4%BA%BA%E8%84%B8%E6%B3%A8%E5%86%8C
        """
        options = options or {}
        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id
        data['scene_type'] = scene_type
        data.update(options)
        return self._request(self.__faceSceneFacesetUserAddUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceSceneFacesetUserUpdate(self, image, image_type, group_id, user_id, scene_type, options=None):
        """
            场景化（人脸更新）
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Aknhmx6hi#%E4%BA%BA%E8%84%B8%E5%BA%93%E7%AE%A1%E7%90%86%EF%BC%88%E5%9C%BA%E6%99%AF%E5%8C%96%EF%BC%89-%E4%BA%BA%E8%84%B8%E6%9B%B4%E6%96%B0
        """
        options = options or {}
        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id
        data['scene_type'] = scene_type
        data.update(options)
        return self._request(self.__faceSceneFacesetUserUpdateUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceSceneFacesetGroupAdd(self, group_id, scene_type, options=None):
        """
            场景化（创建用户组）
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Aknhmx6hi#%E4%BA%BA%E8%84%B8%E5%BA%93%E7%AE%A1%E7%90%86%EF%BC%88%E5%9C%BA%E6%99%AF%E5%8C%96%EF%BC%89-%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7%E7%BB%84
        """
        options = options or {}
        data = {}
        data['group_id'] = group_id
        data['scene_type'] = scene_type
        data.update(options)
        return self._request(self.__faceSceneFacesetGroupAddUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceCaptureSearch(self, image, image_type, group_id_list, options=None):
        """
            场景化（1：N识别）
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/Aknhmx6hi
        """
        options = options or {}
        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id_list'] = group_id_list
        data.update(options)
        return self._request(self.__faceCaptureSearchUrl, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceIdmatchDateV4(self, name, id_card_number, start_date, end_date, options=None):
        """
            身份证信息及有效期核验接口
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/elav5puig
        """
        options = options or {}
        data = {}
        data['name'] = name
        data['id_card_number'] = id_card_number
        data['start_date'] = start_date
        data['end_date'] = end_date
        data.update(options)
        return self._request(self.__faceIdmatchDateV4Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })

    def faceVerifyDateV4(self, name, id_card_number, start_date, end_date, image, image_type, options=None):
        """
            人脸实名信息及有效期核验
            接口使用说明文档: https://ai.baidu.com/ai-doc/FACE/qlav5rwms
        """
        options = options or {}
        data = {}
        data['name'] = name
        data['id_card_number'] = id_card_number
        data['start_date'] = start_date
        data['end_date'] = end_date
        data['image'] = image
        data['image_type'] = image_type
        data.update(options)
        return self._request(self.__faceVerifyDateV4Url, json.dumps(data, ensure_ascii=False), {
            'Content-Type': 'application/json',
        })




