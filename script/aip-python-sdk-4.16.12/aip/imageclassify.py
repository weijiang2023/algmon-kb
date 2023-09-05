
# -*- coding: utf-8 -*-

"""
图像识别
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



class AipImageClassify(AipBase):

    """
    图像识别&车辆分析
    """

    #  组合接口API
    __combinationUrl = "https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"

    # 通用物体和场景识别
    __advancedGeneralUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'

    # 图像单主体检测
    __objectDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect'

    # 动物识别
    __animalDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal'

    # 植物识别
    __plantDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant'

    # logo识别
    __logoSearchUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/logo'

    # logo识别—入库
    __logoAddUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/add'

    # logo识别—删除
    __logoDeleteUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/delete'

    # 果蔬识别
    __ingredientUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient'

    # 自定义菜品-入库
    __customDishAddUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/add"

    # 自定义菜品-检索
    __customDishSearchUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/search"

    # 自定义菜品-删除
    __customDishDeleteUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/delete"

    # 菜品识别
    __dishDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'

    # 红酒识别
    __redwineUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine'

    # 货币识别
    __currencyUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/currency'

    # 地标识别
    __landmarkUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark'

    # 图像多主体检测
    __multiObjectDetectUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/multi_object_detect"

    # 自定义红酒-入库
    __customRedwineAddUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/redwine/add"

    # 自定义红酒-检索
    __customRedwineSearchUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/redwine/search"

    # 自定义红酒-删除
    __customRedwineDeleteUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/redwine/delete"

    # 自定义红酒-更新
    __customRedwineUpdateUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/redwine/update"

    # 花卉识别-已下线
    __flowerUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/flower'


    # 车型识别
    __carDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'

    # 车辆检测
    __vehicleDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect'

    # 车辆外观损伤识别
    __vehicleDamageUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_damage'

    # 车流统计
    __traffic_flowUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/traffic_flow"

    # 车辆属性识别
    __vehicle_attrUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_attr"

    # 车辆检测-高空版
    __vehicle_detect_highUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect_high"

    # 车辆分割
    __vehicle_seg_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_seg";

    __carClassifyV1Url = 'https://aip.baidubce.com/rest/2.0/vis-classify/v1/car'
    __vehicleAttrClassifyV2Url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/vehicle_attr'


    def combinationByImage(self, image, scenes, options=None):
        """
        组合接口
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['scenes'] = scenes
        data.update(options)
        return self._request(self.__combinationUrl, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})


    def combinationByImageUrl(self, imageUrl, scenes, options=None):
        """
        组合接口_url图片方式
        """
        options = options or {}
        data = {}
        data['imgUrl'] = imageUrl
        data['scenes'] = scenes
        data.update(options)
        return self._request(self.__combinationUrl, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})

    def advancedGeneral(self, image, options=None):
        """
            通用物体和场景识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__advancedGeneralUrl, data)

    def advancedGeneralUrl(self, url, options=None):
        """
            通用物体和场景识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__advancedGeneralUrl, data)

    def objectDetect(self, image, options=None):
        """
            图像单主体检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__objectDetectUrl, data)

    def animalDetect(self, image, options=None):
        """
            动物识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__animalDetectUrl, data)

    def animalDetectUrl(self, url, options=None):
        """
            动物识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__animalDetectUrl, data)

    def plantDetect(self, image, options=None):
        """
            植物识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__plantDetectUrl, data)

    def plantDetectUrl(self, url, options=None):
        """
            植物识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__plantDetectUrl, data)

    def logoSearch(self, image, options=None):
        """
            logo识别-检索
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__logoSearchUrl, data)

    def logoSearchUrl(self, url, options=None):
        """
            logo识别-检索_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__logoSearchUrl, data)

    def logoAdd(self, image, brief, options=None):
        """
            logo识别—入库
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['brief'] = brief

        data.update(options)

        return self._request(self.__logoAddUrl, data)

    def logoAddUrl(self, url, brief, options=None):
        """
            logo识别—入库_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url
        data['brief'] = brief

        data.update(options)

        return self._request(self.__logoAddUrl, data)

    def logoDeleteByImage(self, image, options=None):
        """
            logo识别—删除_image图片方式
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__logoDeleteUrl, data)

    def logoDeleteBySign(self, cont_sign, options=None):
        """
            logo识别—删除_cont_sign签名方式
        """
        options = options or {}

        data = {}
        data['cont_sign'] = cont_sign

        data.update(options)

        return self._request(self.__logoDeleteUrl, data)

    def ingredient(self, image, options=None):
        """
            果蔬识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__ingredientUrl, data)

    def ingredientUrl(self, url, options=None):
        """
            果蔬识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__ingredientUrl, data)

    def customDishesAddImage(self, image, brief, options=None):
        """
            自定义菜品识别—入库
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['brief'] = brief
        data.update(options)
        return self._request(self.__customDishAddUrl, data)

    def customDishesAddUrl(self, url, brief, options=None):
        """
            自定义菜品识别—入库_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data['brief'] = brief
        data.update(options)
        return self._request(self.__customDishAddUrl, data)

    def customDishesSearch(self, image, options=None):
        """
            自定义菜品识别—检索
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customDishSearchUrl, data)

    def customDishesSearchUrl(self, url, options=None):
        """
            自定义菜品识别—检索_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__customDishSearchUrl, data)

    def customDishesDeleteImage(self, image, options=None):
        """
            自定义菜品识别—删除_image图片方式
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customDishDeleteUrl, data)

    def customDishesDeleteUrl(self, url, options=None):
        """
            自定义菜品识别—删除_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__customDishDeleteUrl, data)

    def customDishesDeleteContSign(self, cont_sign, options=None):
        """
            自定义菜品识别—删除_cont_sign签名方式
        """
        options = options or {}
        data = {}
        data['cont_sign'] = cont_sign
        data.update(options)
        return self._request(self.__customDishDeleteUrl, data)

    def dishDetect(self, image, options=None):
        """
            菜品识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__dishDetectUrl, data)

    def dishDetectUrl(self, url, options=None):
        """
            菜品识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__dishDetectUrl, data)

    def redwine(self, image, options=None):
        """
            红酒识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__redwineUrl, data)

    def redwineUrl(self, url, options=None):
        """
            红酒识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__redwineUrl, data)

    def currency(self, image, options=None):
        """
            货币识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__currencyUrl, data)

    def currencyUrl(self, url, options=None):
        """
            货币识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__currencyUrl, data)

    def landmark(self, image, options=None):
        """
            地标识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__landmarkUrl, data)

    def landmarkUrl(self, url, options=None):
        """
            地标识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__landmarkUrl, data)

    def multiObjectDetect(self, image, options=None):
        """
            图像多主体检测
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__multiObjectDetectUrl, data)

    def multiObjectDetectUrl(self, url, options=None):
        """
            图像多主体检测_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__multiObjectDetectUrl, data)

    def customRedwineAddImage(self, image, brief, options=None):
        """
            自定义红酒—入库
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['brief'] = brief
        data.update(options)
        return self._request(self.__customRedwineAddUrl, data)

    def customRedwineAddUrl(self, url, brief, options=None):
        """
            自定义红酒—入库_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data['brief'] = brief
        data.update(options)
        return self._request(self.__customRedwineAddUrl, data)

    def customRedwineSearch(self, image, options=None):
        """
            自定义红酒—检索
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customRedwineSearchUrl, data)

    def customRedwineSearchUrl(self, url, options=None):
        """
            自定义红酒—检索_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__customRedwineSearchUrl, data)

    def customRedwineDeleteImage(self, image, options=None):
        """
            自定义红酒—删除_image图片方式
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customRedwineDeleteUrl, data)

    def customRedwineDeleteContSign(self, cont_sign_list, options=None):
        """
            自定义红酒—删除_cont_sign签名方式
        """
        options = options or {}
        data = {}
        data['cont_sign_list'] = cont_sign_list
        data.update(options)
        return self._request(self.__customRedwineDeleteUrl, data)

    def customRedwineUpdate(self, image, options=None):
        """
            自定义红酒—更新
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customRedwineUpdateUrl, data)

    def customRedwineUpdateUrl(self, url, options=None):
        """
            自定义红酒—更新_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__customRedwineUpdateUrl, data)

    def flower(self, image, options=None):
        """
            花卉识别-已下线
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__flowerUrl, data)



    def carDetect(self, image, options=None):
        """
            车型识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__carDetectUrl, data)

    def carDetectUrl(self, url, options=None):
        """
            车型识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__carDetectUrl, data)

    def vehicleDetect(self, image, options=None):
        """
            车辆检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleDetectUrl, data)

    def vehicleDetectUrl(self, url, options=None):
        """
            车辆检测_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicleDetectUrl, data)

    def vehicleDamage(self, image, options=None):
        """
            车辆外观损伤识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleDamageUrl, data)

    def vehicleDamageUrl(self, url, options=None):
        """
            车辆外观损伤识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicleDamageUrl, data)

    def trafficFlow(self, image, case_id, case_init, area, options=None):
        """
            车流统计
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['case_id'] = case_id
        data['case_init'] = case_init
        data['area'] = area

        data.update(options)

        return self._request(self.__traffic_flowUrl, data)

    def trafficFlowUrl(self, url, case_id, case_init, area, options=None):
        """
            车流统计_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url
        data['case_id'] = case_id
        data['case_init'] = case_init
        data['area'] = area

        data.update(options)

        return self._request(self.__traffic_flowUrl, data)

    def vehicleAttr(self, image, options=None):
        """
            车辆属性识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicle_attrUrl, data)

    def vehicleAttrUrl(self, url, options=None):
        """
            车辆属性识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__vehicle_attrUrl, data)

    def vehicleDetectHigh(self, image, options=None):
        """
            车辆检测-高空版
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicle_detect_highUrl, data)

    def vehicleDetectHighUrl(self, url, options=None):
        """
            车辆检测-高空版_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicle_detect_highUrl, data)

    def vehicleSeg(self, image, options=None):
        """
            车辆分割
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicle_seg_url, data)

    def vehicleSegUrl(self, url, options=None):
        """
            车辆分割: url方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicle_seg_url, data)

    def vehicleAttrClassifyV2Image(self, image, options=None):
        """
            车辆属性识别
            接口使用说明: https://ai.baidu.com/ai-doc/VEHICLE/mk3hb3fde
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__vehicleAttrClassifyV2Url, data)

    def vehicleAttrClassifyV2Url(self, url, options=None):
        """
            车辆属性识别
            接口使用说明: https://ai.baidu.com/ai-doc/VEHICLE/mk3hb3fde
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__vehicleAttrClassifyV2Url, data)


