# -*- coding: utf-8 -*-

"""
文字识别HTTP SDK

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


class AipOcr(AipBase):
    """
    文字识别
    """

    """通用场景文字识别"""

    # 通用文字识别（高精度版）
    __accurateBasicUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'

    # 通用文字识别（高精度含位置版）
    __accurateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate'

    # 通用文字识别（标准版）
    __generalBasicUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

    # 通用文字识别（标准含位置版）
    __generalUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general'

    # 办公文档识别
    __doc_analysis_officeUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis_office'

    # 网络图片文字识别
    __webImageUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'

    # 网络图片文字识别（含位置版）
    __webimageLoc = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage_loc"

    # 表格文字识别（同步接口）
    __formUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/form'

    # 印章识别
    __sealUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/seal'

    # 表格文字识别（异步接口）--提交请求
    __tableRecognizeUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request'

    # 表格文字识别（异步接口）--获取结果
    __tableResultGetUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'

    # 手写文字识别
    __handwritingUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting'

    # 表格文字识别V2
    __tableUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/table'

    # 数字识别
    __numbersUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'

    # 二维码识别
    __qrcodeUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/qrcode'

    # 图文转换器（接口版）--提交请求
    __docConvertRequestUrl= 'https://aip.baidubce.com/rest/2.0/ocr/v1/doc_convert/request'

    # 图文转换器（接口版）--获取结果
    __docConvertResultUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/doc_convert/get_request_result'

    # 通用文字识别（含生僻字版）已停止更新
    __generalEnhancedUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_enhanced'

    """卡证文字识别"""

    # 身份证识别
    __idcardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard'

    # 身份证混贴识别
    __multi_idcardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/multi_idcard'

    # 身份证识别（金融加密版）
    # 无

    # 银行卡识别
    __bankcardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard'

    # 营业执照识别
    __businessLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/business_license'

    # 名片识别
    __businessCardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/business_card'

    # 护照识别
    __passportUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/passport'

    # 社保卡识别
    __social_security_cardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/social_security_card'

    # 港澳通行证识别
    __HKMacauExitentrypermitUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/HK_Macau_exitentrypermit'

    # 台湾通行证识别
    __taiwanExitentrypermitUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/taiwan_exitentrypermit'

    # 户口本识别
    __householdRegisterUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/household_register'

    # 出生医学证明识别
    __birthCertificateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/birth_certificate'

    # 多卡证类别检测
    __multi_card_classifyUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/multi_card_classify'

    """交通场景文字识别"""

    # 行驶证识别
    __vehicleLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license'

    # 驾驶证识别
    __drivingLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license'

    # 车辆证照混贴识别（公测）
    __mixed_multi_vehicleUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/mixed_multi_vehicle"

    # 车牌识别
    __licensePlateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'

    # VIN码识别
    __vinCodeUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vin_code'

    # 机动车销售发票识别
    __vehicleInvoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_invoice'

    # 二手车销售发票识别
    __used_vehicle_invoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/used_vehicle_invoice'

    # 车辆合格证识别
    __vehicleCertificateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_certificate'

    # 机动车登记证书识别
    __vehicle_registration_certificateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_registration_certificate'

    # 磅单识别
    __weight_noteUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/weight_note"

    # 快递面单识别
    __waybillUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/waybill'

    # 道路运输证识别
    __road_transport_certificateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/road_transport_certificate'

    """财务票据文字识别"""

    # 智能财务票据识别
    __multipleInvoiceUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/multiple_invoice"

    # 增值税发票识别
    __vatInvoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice'

    # 增值税发票验真
    __vat_invoice_verificationUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice_verification"

    # 定额发票识别
    __quotaInvoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/quota_invoice'

    # 通用机打发票识别
    __invoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/invoice'

    # 火车票识别
    __trainTicketUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/train_ticket'

    # 出租车票识别
    __taxiReceiptUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/taxi_receipt'

    # 飞机行程单识别
    __airTicketUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/air_ticket'

    # 汽车票识别
    __bus_ticketUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bus_ticket'

    # 过路过桥费发票识别
    __toll_invoiceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/toll_invoice'

    # 船票识别
    __ferry_ticketUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/ferry_ticket'

    # 网约车行程单识别
    __online_taxi_itineraryUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/online_taxi_itinerary"

    # 通用票据识别
    __receiptUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/receipt'

    # 购物小票识别
    __shopping_receiptUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/shopping_receipt'

    """医疗票据文字识别"""

    # 医疗发票识别
    __medicalInvoiceUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_invoice"

    # 医疗费用明细识别
    __medical_detailUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_detail"

    # 医疗费用结算单识别
    __medical_statementUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_statement'

    # 医疗检验报告单识别
    __medical_report_detectionUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_report_detection'

    # 医疗诊断报告单识别
    __health_reportUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/health_report'

    # 病案首页识别
    __medical_recordUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_record'

    # 出院小结识别
    __medical_summaryUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_summary'

    # 诊断证明识别
    __medical_summary_diagnosisUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_summary_diagnosis'

    # 门诊病历识别
    __medical_outpatientUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_outpatient'

    # 处方笺识别
    __medical_prescriptionUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_prescription'

    # 医疗票据类别检测
    __medical_recipts_classifyUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_recipts_classify'

    # 保险单识别
    __insuranceDocumentsUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/insurance_documents'

    """防疫场景文字识别"""

    # 通信行程卡识别
    __travel_cardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/travel_card'

    # 健康码识别
    __health_codeUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/health_code'

    # 核酸证明识别
    __covid_testUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/covid_test'

    """教育场景文字识别"""

    # 试卷分析与识别
    __docAnalysis = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis"

    # 公式识别
    __formulaUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"

    """其他场景文字识别"""

    # 仪器仪表盘读数识别
    __meter = "https://aip.baidubce.com/rest/2.0/ocr/v1/meter"

    # 彩票识别
    __lotteryUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/lottery'

    # 门脸文字识别
    __facadeUrl = "https://aip.baidubce.com/rest/2.0/ocr/v1/facade"

    # 智能结构化识别
    __intelligent_ocrUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/intelligent_ocr'

    """文档图像处理"""

    # 文档矫正增强
    __doc_crop_enhanceUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/doc_crop_enhance'

    # 文档去手写
    __remove_handwritingUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/remove_handwriting'

    """iOCR自定义模板文字识别"""

    # iOCR通用版
    __customUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise'

    # iOCR财会版
    __custom_financeUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise/finance'

    def basicAccurate(self, image, options=None):
        """
            通用文字识别（高精度版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__accurateBasicUrl, data)

    def basicAccurateUrl(self, url, options=None):
        """
            通用文字识别（高精度版）_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__accurateBasicUrl, data)

    def basicAccuratePdf(self, pdf_file, options=None):
        """
            通用文字识别（高精度版）_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__accurateBasicUrl, data)

    def accurate(self, image, options=None):
        """
            通用文字识别（高精度含位置版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__accurateUrl, data)

    def accurateUrl(self, url, options=None):
        """
            通用文字识别（高精度含位置版）_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__accurateUrl, data)

    def accuratePdf(self, pdf_file, options=None):
        """
            通用文字识别（高精度含位置版）_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__accurateUrl, data)

    def basicGeneral(self, image, options=None):
        """
            通用文字识别（标准版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalBasicUrl, data)

    def basicGeneralUrl(self, url, options=None):
        """
            通用文字识别（标准版）_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalBasicUrl, data)

    def basicGeneralPdf(self, pdf_file, options=None):
        """
            通用文字识别（标准版）_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__generalBasicUrl, data)

    def general(self, image, options=None):
        """
            通用文字识别（标准含位置版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalUrl, data)

    def generalUrl(self, url, options=None):
        """
            通用文字识别（标准含位置版）_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalUrl, data)

    def generalPdf(self, pdf_file, options=None):
        """
            通用文字识别（标准含位置版）_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__generalUrl, data)

    def doc_analysis_office(self, image, options=None):
        """
            办公文档识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__doc_analysis_officeUrl, data)

    def doc_analysis_officeUrl(self, url, options=None):
        """
            办公文档识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__doc_analysis_officeUrl, data)

    def doc_analysis_officePdf(self, pdf_file, options=None):
        """
            办公文档识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__doc_analysis_officeUrl, data)

    def webImage(self, image, options=None):
        """
            网络图片文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__webImageUrl, data)

    def webImageUrl(self, url, options=None):
        """
            网络图片文字识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__webImageUrl, data)

    def webImagePdf(self, pdf_file, options=None):
        """
            网络图片文字识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__webImageUrl, data)

    def webimageLoc(self, image, options=None):
        """
            网络图片文字识别（含位置版）
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__webimageLoc, data)

    def webimageLocUrl(self, url, options=None):
        """
            网络图片文字识别（含位置版）_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)
        return self._request(self.__webimageLoc, data)

    def webimageLocPdf(self, pdf_file, options=None):
        """
            网络图片文字识别（含位置版）_pdf文件方式
        """
        options = options or {}
        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()
        data.update(options)
        return self._request(self.__webimageLoc, data)

    def form(self, image, options=None):
        """
            表格文字识别（同步接口）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__formUrl, data)

    def formUrl(self, url, options=None):
        """
            表格文字识别（同步接口）_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__formUrl, data)

    def seal(self, image, options=None):
        """
            印章识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__sealUrl, data)

    def sealUrl(self, url, options=None):
        """
            印章识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__sealUrl, data)

    def sealPdf(self, pdf_file, options=None):
        """
            印章识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__sealUrl, data)

    def tableRecognitionAsync(self, image, options=None):
        """
            表格文字识别(异步接口)--提交请求
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__tableRecognizeUrl, data)

    def getTableRecognitionResult(self, request_id, options=None):
        """
            表格识别结果(异步接口)--获取结果
        """
        options = options or {}

        data = {}
        data['request_id'] = request_id

        data.update(options)

        return self._request(self.__tableResultGetUrl, data)

    def tableRecognition(self, image, options=None, timeout=10000):
        """
            tableRecognition
        """

        result = self.tableRecognitionAsync(image)

        if 'error_code' in result:
            return result

        requestId = result['result'][0]['request_id']
        for i in range(int(math.ceil(timeout / 1000.0))):
            result = self.getTableRecognitionResult(requestId, options)

            # 完成
            if int(result['result']['ret_code']) == 3:
                break
            time.sleep(1)

        return result

    def handwriting(self, image, options=None):
        """
            手写文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__handwritingUrl, data)

    def handwritingUrl(self, url, options=None):
        """
            手写文字识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__handwritingUrl, data)

    def handwritingPdf(self, pdf_file, options=None):
        """
            手写文字识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__handwritingUrl, data)

    def table(self, image, options=None):
        """
            表格文字识别V2
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__tableUrl, data)

    def tableUrl(self, url, options=None):
        """
            表格文字识别V2_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__tableUrl, data)

    def tablePdf(self, pdf_file, options=None):
        """
            表格文字识别V2_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__tableUrl, data)

    def numbers(self, image, options=None):
        """
            数字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__numbersUrl, data)

    def numbersUrl(self, url, options=None):
        """
            数字识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__numbersUrl, data)

    def qrcode(self, image, options=None):
        """
            二维码识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__qrcodeUrl, data)

    def qrcodeUrl(self, url, options=None):
        """
            二维码识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__qrcodeUrl, data)

    def docConvertRequestV1(self, image, options=None):
        """
            图文转换器（接口版）--提交请求
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__docConvertRequestUrl, data)

    def docConvertRequestV1Url(self, url, options=None):
        """
            图文转换器（接口版）--提交请求_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__docConvertRequestUrl, data)

    def docConvertRequestV1Pdf(self, pdf_file, options=None):
        """
            图文转换器（接口版）--提交请求_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__docConvertRequestUrl, data)

    def docConvertResultV1(self, task_id, options=None):
        """
            图文转换器（接口版）--获取结果
        """
        options = options or {}

        data = {}
        data['task_id'] = task_id

        data.update(options)

        return self._request(self.__docConvertResultUrl, data)

    def enhancedGeneral(self, image, options=None):
        """
            通用文字识别（含生僻字版）已停止更新
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalEnhancedUrl, data)

    def enhancedGeneralUrl(self, url, options=None):
        """
            通用文字识别（含生僻字版）_url图片方式已停止更新
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalEnhancedUrl, data)

    def idcard(self, image, id_card_side, options=None):
        """
            身份证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['id_card_side'] = id_card_side

        data.update(options)

        return self._request(self.__idcardUrl, data)

    def idcardUrl(self, url, id_card_side, options=None):
        """
            身份证识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url
        data['id_card_side'] = id_card_side

        data.update(options)

        return self._request(self.__idcardUrl, data)

    def multi_idcard(self, image, options=None):
        """
            身份证混贴识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__multi_idcardUrl, data)

    def multi_idcardUrl(self, url, options=None):
        """
            身份证混贴识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__multi_idcardUrl, data)

    def bankcard(self, image, options=None):
        """
            银行卡识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bankcardUrl, data)

    def bankcardUrl(self, url, options=None):
        """
            银行卡识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__bankcardUrl, data)

    def businessLicense(self, image, options=None):
        """
            营业执照识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__businessLicenseUrl, data)

    def businessLicenseUrl(self, url, options=None):
        """
            营业执照识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__businessLicenseUrl, data)

    def businessCard(self, image, options=None):
        """
            名片识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__businessCardUrl, data)

    def passport(self, image, options=None):
        """
            护照识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__passportUrl, data)

    def passportUrl(self, url, options=None):
        """
            护照识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__passportUrl, data)

    def social_security_card(self, image, options=None):
        """
            社保卡识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__social_security_cardUrl, data)

    def social_security_cardUrl(self, url, options=None):
        """
           社保卡识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__social_security_cardUrl, data)

    def HKMacauExitentrypermit(self, image, options=None):
        """
            港澳通行证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__HKMacauExitentrypermitUrl, data)

    def taiwanExitentrypermit(self, image, options=None):
        """
            台湾通行证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__taiwanExitentrypermitUrl, data)

    def householdRegister(self, image, options=None):
        """
            户口本识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__householdRegisterUrl, data)

    def householdRegisterUrl(self, url, options=None):
        """
            户口本识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__householdRegisterUrl, data)

    def birthCertificate(self, image, options=None):
        """
            出生医学证明识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__birthCertificateUrl, data)

    def birthCertificateUrl(self, url, options=None):
        """
            出生医学证明识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__birthCertificateUrl, data)

    def multi_card_classify(self, image, options=None):
        """
            多卡证类别检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__multi_card_classifyUrl, data)

    def multi_card_classifyUrl(self, url, options=None):
        """
            多卡证类别检测_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__multi_card_classifyUrl, data)

    def vehicleLicense(self, image, options=None):
        """
            行驶证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleLicenseUrl, data)

    def vehicleLicenseUrl(self, url, options=None):
        """
            行驶证识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicleLicenseUrl, data)

    def drivingLicense(self, image, options=None):
        """
            驾驶证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__drivingLicenseUrl, data)

    def drivingLicenseUrl(self, url, options=None):
        """
            驾驶证识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__drivingLicenseUrl, data)

    def licensePlate(self, image, options=None):
        """
            车牌识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__licensePlateUrl, data)

    def licensePlateUrl(self, url, options=None):
        """
            车牌识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__licensePlateUrl, data)

    def mixed_multi_vehicle(self, image, options=None):
        """
            车辆证照混贴识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__mixed_multi_vehicleUrl, data)

    def mixed_multi_vehicleUrl(self, url, options=None):
        """
            车辆证照混贴识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__mixed_multi_vehicleUrl, data)

    def vinCode(self, image, options=None):
        """
            VIN码识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__vinCodeUrl, data)

    def vinCodeUrl(self, image, options=None):
        """
            VIN码识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = image

        data.update(options)
        return self._request(self.__vinCodeUrl, data)

    def vehicleInvoice(self, image, options=None):
        """
            机动车销售发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleInvoiceUrl, data)

    def vehicleInvoiceUrl(self, url, options=None):
        """
            机动车销售发票_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicleInvoiceUrl, data)

    def used_vehicle_invoice(self, image, options=None):
        """
            二手车销售发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__used_vehicle_invoiceUrl, data)

    def used_vehicle_invoiceUrl(self, url, options=None):
        """
            二手车销售发票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__used_vehicle_invoiceUrl, data)

    def vehicleCertificate(self, image, options=None):
        """
            车辆合格证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleCertificateUrl, data)

    def vehicleCertificateUrl(self, url, options=None):
        """
            车辆合格证识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicleCertificateUrl, data)

    def vehicle_registration_certificate(self, image, options=None):
        """
            机动车登记证书识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicle_registration_certificateUrl, data)

    def vehicle_registration_certificateUrl(self, url, options=None):
        """
            机动车登记证书识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicle_registration_certificateUrl, data)

    def weightNote(self, image, options=None):
        """
            磅单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__weight_noteUrl, data)

    def weightNoteUrl(self, url, options=None):
        """
            磅单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__weight_noteUrl, data)

    def weightNotePdf(self, pdf_file, options=None):
        """
            磅单识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__weight_noteUrl, data)

    def waybill(self, image, options=None):
        """
            快递面单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__waybillUrl, data)

    def waybillUrl(self, url, options=None):
        """
            快递面单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__waybillUrl, data)

    def road_transport_certificate(self, image, options=None):
        """
            道路运输证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__road_transport_certificateUrl, data)

    def road_transport_certificateUrl(self, url, options=None):
        """
            道路运输证识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__road_transport_certificateUrl, data)

    def road_transport_certificatePdf(self, pdf_file, options=None):
        """
            道路运输证识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__road_transport_certificateUrl, data)

    def multipleInvoice(self, image, options=None):
        """
            智能财务票据识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__multipleInvoiceUrl, data)

    def multipleInvoiceUrl(self, url, options=None):
        """
            智能财务票据识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__multipleInvoiceUrl, data)

    def multipleInvoicePdf(self, pdf_file, options=None):
        """
            智能财务票据识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__multipleInvoiceUrl, data)

    def vatInvoice(self, image, options=None):
        """
            增值税发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vatInvoiceUrl, data)

    def vatInvoiceUrl(self, image, options=None):
        """
            增值税发票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = image

        data.update(options)

        return self._request(self.__vatInvoiceUrl, data)

    def vatInvoicePdf(self, pdf_file, options=None):
        """
            增值税发票识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__vatInvoiceUrl, data)

    def vat_invoice_verification(self, options=None):
        """
            增值税发票验真
        """
        options = options or {}

        data = {}
        # data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vat_invoice_verificationUrl, data)

    def quotaInvoice(self, image, options=None):
        """
            定额发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__quotaInvoiceUrl, data)

    def invoice(self, image, options=None):
        """
            通用机打发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__invoiceUrl, data)

    def invoiceUrl(self, url, options=None):
        """
            通用机打发票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__invoiceUrl, data)

    def invoicePdf(self, pdf_file, options=None):
        """
            通用机打发票识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__invoiceUrl, data)

    def trainTicket(self, image, options=None):
        """
            火车票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__trainTicketUrl, data)

    def trainTicketUrl(self, image, options=None):
        """
            火车票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = image

        data.update(options)

        return self._request(self.__trainTicketUrl, data)

    def trainTicketPdf(self, pdf_file, options=None):
        """
            火车票识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__trainTicketUrl, data)

    def taxiReceipt(self, image, options=None):
        """
            出租车票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__taxiReceiptUrl, data)

    def taxiReceiptUrl(self, image, options=None):
        """
            出租车票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = image

        data.update(options)

        return self._request(self.__taxiReceiptUrl, data)

    def taxiReceiptPdf(self, pdf_file, options=None):
        """
            出租车票识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__taxiReceiptUrl, data)

    def airTicket(self, image, options=None):
        """
            飞机行程单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__airTicketUrl, data)

    def airTicketUrl(self, url, options=None):
        """
            飞机行程单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__airTicketUrl, data)

    def airTicketPdf(self, pdf_file, options=None):
        """
            飞机行程单识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__airTicketUrl, data)

    def bus_ticket(self, image, options=None):
        """
            汽车票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bus_ticketUrl, data)

    def bus_ticketUrl(self, url, options=None):
        """
            汽车票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__bus_ticketUrl, data)

    def toll_invoice(self, image, options=None):
        """
            过路过桥费发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__toll_invoiceUrl, data)

    def toll_invoiceUrl(self, url, options=None):
        """
            过路过桥费发票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__toll_invoiceUrl, data)

    def ferry_ticket(self, image, options=None):
        """
            船票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__ferry_ticketUrl, data)

    def ferry_ticketUrl(self, url, options=None):
        """
            船票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__ferry_ticketUrl, data)

    def onlineTaxiItinerary(self, image):
        """
            网约车行程单识别
        """
        data = {}
        data['image'] = base64.b64encode(image).decode()

        return self._request(self.__online_taxi_itineraryUrl, data)

    def onlineTaxiItineraryUrl(self, url):
        """
            网约车行程单识别_url图片方式
        """

        data = {}
        data['url'] = url
        return self._request(self.__online_taxi_itineraryUrl, data)

    def onlineTaxiItineraryPdf(self, pdf_file, options=None):
        """
            网约车行程单识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__online_taxi_itineraryUrl, data)

    def receipt(self, image, options=None):
        """
            通用票据识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__receiptUrl, data)

    def receiptUrl(self, url, options=None):
        """
            通用票据识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__receiptUrl, data)

    def shopping_receipt(self, image, options=None):
        """
            购物小票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__shopping_receiptUrl, data)

    def shopping_receiptUrl(self, url, options=None):
        """
            购物小票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__shopping_receiptUrl, data)

    def shopping_receiptPdf(self, pdf_file, options=None):
        """
            购物小票识别_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__shopping_receiptUrl, data)

    def medicalInvoice(self, image, options=None):
        """
            医疗发票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)
        return self._request(self.__medicalInvoiceUrl, data)

    def medicalInvoiceUrl(self, url, options=None):
        """
            医疗发票识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medicalInvoiceUrl, data)

    def medicalDetail(self, image, options=None):
        """
            医疗费用明细识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_detailUrl, data)

    def medicalDetailUrl(self, url, options=None):
        """
            医疗费用明细识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_detailUrl, data)

    def medical_statement(self, image, options=None):
        """
            医疗费用结算单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_statementUrl, data)

    def medical_statementUrl(self, url, options=None):
        """
            医疗费用结算单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_statementUrl, data)

    def medical_report_detection(self, image, options=None):
        """
            医疗检验报告单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_report_detectionUrl, data)

    def medical_report_detectionUrl(self, url, options=None):
        """
            医疗检验报告单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_report_detectionUrl, data)

    def health_report(self, image, options=None):
        """
            医疗诊断报告单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__health_reportUrl, data)

    def health_reportUrl(self, url, options=None):
        """
            医疗诊断报告单识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__health_reportUrl, data)

    def medical_record(self, image, options=None):
        """
            病案首页识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_recordUrl, data)

    def medical_recordUrl(self, url, options=None):
        """
            病案首页识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_recordUrl, data)

    def medical_summary(self, image, options=None):
        """
            出院小结识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_summaryUrl, data)

    def medical_summaryUrl(self, url, options=None):
        """
            出院小结识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_summaryUrl, data)

    def medical_summary_diagnosis(self, image, options=None):
        """
            诊断证明识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_summary_diagnosisUrl, data)

    def medical_summary_diagnosisUrl(self, url, options=None):
        """
            诊断证明识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_summary_diagnosisUrl, data)

    def medical_outpatient(self, image, options=None):
        """
            门诊病历识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_outpatientUrl, data)

    def medical_outpatientUrl(self, url, options=None):
        """
            门诊病历识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_outpatientUrl, data)

    def medical_prescription(self, image, options=None):
        """
            处方笺识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_prescriptionUrl, data)

    def medical_prescriptionUrl(self, url, options=None):
        """
            处方笺识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_prescriptionUrl, data)

    def medical_recipts_classify(self, image, options=None):
        """
           医疗票据类别检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__medical_recipts_classifyUrl, data)

    def medical_recipts_classifyUrl(self, url, options=None):
        """
            医疗票据类别检测_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__medical_recipts_classifyUrl, data)

    def insuranceDocuments(self, image, options=None):
        """
            保险单识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__insuranceDocumentsUrl, data)

    def travel_card(self, image, options=None):
        """
            通信行程卡识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__travel_cardUrl, data)

    def health_code(self, image, options=None):
        """
            健康码识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__health_codeUrl, data)

    def covid_test(self, image, options=None):
        """
            核酸证明识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__covid_testUrl, data)

    def docAnalysis(self, image, options=None):
        """
            试卷分析与识别
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__docAnalysis, data)

    def docAnalysisUrl(self, url, options=None):
        """
            试卷分析与识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__docAnalysis, data)

    def docAnalysisPdf(self, pdf_file, options=None):
        """
            试卷分析与识别_pdf文件方式
        """
        options = options or {}
        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__docAnalysis, data)

    def formula(self, image, options=None):
        """
            公式识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__formulaUrl, data)

    def formulaUrl(self, url, options=None):
        """
            公式识别_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__formulaUrl, data)

    def meter(self, image, options=None):
        """
            仪器仪表盘读数识别
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)

        return self._request(self.__meter, data)

    def meterUrl(self, url, options=None):
        """
            仪器仪表盘读数识别_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__meter, data)

    def lottery(self, image, options=None):
        """
            彩票识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__lotteryUrl, data)

    def facade(self, image, options=None):
        """
            门脸文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__facadeUrl, data)

    def intelligent_ocr(self, image, options=None):
        """
            智能结构化识别
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)

        return self._request(self.__intelligent_ocrUrl, data)

    def intelligent_ocrUrl(self, url, options=None):
        """
            智能结构化识别_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__intelligent_ocrUrl, data)

    def doc_crop_enhance(self, image, options=None):
        """
            文档矫正增强
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)

        return self._request(self.__doc_crop_enhanceUrl, data)

    def doc_crop_enhanceUrl(self, url, options=None):
        """
            文档矫正增强_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__doc_crop_enhanceUrl, data)

    def doc_crop_enhancePdf(self, pdf_file, options=None):
        """
            文档矫正增强_pdf文件方式
        """
        options = options or {}
        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()
        data.update(options)

        return self._request(self.__doc_crop_enhanceUrl, data)

    def remove_handwriting(self, image, options=None):
        """
            文档去手写
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)

        return self._request(self.__remove_handwritingUrl, data)

    def remove_handwritingUrl(self, url, options=None):
        """
            文档去手写_url图片方式
        """
        options = options or {}
        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__remove_handwritingUrl, data)

    def remove_handwritingPdf(self, pdf_file, options=None):
        """
            文档去手写_pdf文件方式
        """
        options = options or {}
        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()
        data.update(options)

        return self._request(self.__remove_handwritingUrl, data)

    def custom(self, image, options=None):
        """
            iOCR通用版
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__customUrl, data)

    def customUrl(self, url, options=None):
        """
            iOCR通用版_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__customUrl, data)

    def customPdf(self, pdf_file, options=None):
        """
            iOCR通用版_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__customUrl, data)

    def custom_finance(self, image, options=None):
        """
            iOCR财会版
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__custom_financeUrl, data)

    def custom_financeUrl(self, url, options=None):
        """
            iOCR财会版_url图片方式
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__custom_financeUrl, data)

    def custom_financePdf(self, pdf_file, options=None):
        """
            iOCR财会版_pdf文件方式
        """
        options = options or {}

        data = {}
        data['pdf_file'] = base64.b64encode(pdf_file).decode()

        data.update(options)

        return self._request(self.__custom_financeUrl, data)
