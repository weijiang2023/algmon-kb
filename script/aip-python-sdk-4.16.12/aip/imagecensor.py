# -*- coding: utf-8 -*-

import re
import sys
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote


class AipImageCensor(AipBase):
    """
        Aip ImageCensor
    """

    __imageCensorUserDefinedUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined'

    __textCensorUserDefinedUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined'

    __voiceCensorUserDefinedUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/voice_censor/v3/user_defined"

    __videoCensorUserDefinedUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v2/user_defined"

    __videoCensorSubmitUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v1/video/submit"

    __videoCensorPullUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v1/video/pull"

    __asyncVoiceSubmitUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/async_voice/submit"

    __asyncVoicePullUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/async_voice/pull"

    __liveConfigSaveUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/live/v1/config/save"

    __liveConfigStopUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/live/v1/config/stop"

    __liveConfigViewUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/live/v1/config/view"

    __liveAuditPullUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/live/v1/audit/pull"

    def imageCensorUserDefined(self, image):
        """
            imageCensorUserDefined
        """

        data = {}

        isUrl = image[0:4] == 'http'
        if not isUrl:
            data['image'] = base64.b64encode(image).decode()
        else:
            data['imgUrl'] = image

        return self._request(self.__imageCensorUserDefinedUrl, data)

    def textCensorUserDefined(self, text):
        """
            textCensorUserDefined
        """

        data = {}

        data['text'] = text

        return self._request(self.__textCensorUserDefinedUrl, data)

    def voiceCensorUserDefined(self, voice, rate, fmt, options=None):
        """
            voiceCensorUserDefined
        """
        data = {}
        options = options or {}
        data['base64'] = base64.b64encode(voice).decode()
        data['fmt'] = fmt
        data['rate'] = rate
        data.update(options)
        return self._request(self.__voiceCensorUserDefinedUrl, data)

    def voiceUrlCensorUserDefined(self, voice, rate, fmt, options=None):
        """
            voiceCensorUserDefined
        """
        data = {}
        options = options or {}
        data['url'] = voice
        data['fmt'] = fmt
        data['rate'] = rate
        data.update(options)
        return self._request(self.__voiceCensorUserDefinedUrl, data)

    def videoCensorUserDefined(self, name, videoUrl, extId, options=None):
        """
            videoCensorUserDefined
        """
        data = {}
        options = options or {}
        data['name'] = name
        data['videoUrl'] = videoUrl
        data['extId'] = extId
        data.update(options)
        return self._request(self.__videoCensorUserDefinedUrl, data)

    def videoCensorSubmit(self, url, extId, options=None):
        """
            videoCensorSubmit
        """
        data = {}
        options = options or {}
        data['url'] = url
        data['extId'] = extId
        data.update(options)
        return self._request(self.__videoCensorSubmitUrl, data)

    def videoCensorPull(self, taskId, options=None):
        """
            videoCensorPull
        """
        data = {}
        options = options or {}
        data['taskId'] = taskId
        data.update(options)
        return self._request(self.__videoCensorPullUrl, data)

    def asyncVoiceSubmit(self, url, fmt, rate, options=None):
        """
            asyncVoiceSubmit
        """
        data = {}
        options = options or {}
        data['url'] = url
        data['fmt'] = fmt
        data['rate'] = rate
        data.update(options)
        return self._request(self.__asyncVoiceSubmitUrl, data)

    def asyncVoiceTaskPull(self, taskId, options=None):
        """
            asyncVoiceTaskPull
        """
        data = {}
        options = options or {}
        data['taskId'] = taskId
        data.update(options)
        return self._request(self.__asyncVoicePullUrl, data)

    def asyncVoiceAudioPull(self, audioId, options=None):
        """
            asyncVoiceAudioPull
        """
        data = {}
        options = options or {}
        data['audioId'] = audioId
        data.update(options)
        return self._request(self.__asyncVoicePullUrl, data)

    def liveConfigSave(self, streamUrl, streamType, extId, startTime, endTime, streamName, options=None):
        """
            liveConfigSave
        """
        data = {}
        options = options or {}
        data['streamUrl'] = streamUrl
        data['streamType'] = streamType
        data['extId'] = extId
        data['startTime'] = startTime
        data['endTime'] = endTime
        data['streamName'] = streamName
        data.update(options)
        return self._request(self.__liveConfigSaveUrl, data)

    def liveConfigStop(self, taskId, options=None):
        """
            liveConfigStop
        """
        data = {}
        options = options or {}
        data['taskId'] = taskId
        data.update(options)
        return self._request(self.__liveConfigStopUrl, data)

    def liveConfigView(self, taskId, options=None):
        """
            liveConfigView
        """
        data = {}
        options = options or {}
        data['taskId'] = taskId
        data.update(options)
        return self._request(self.__liveConfigViewUrl, data)

    def liveAuditPull(self, taskId, options=None):
        """
            liveAuditPull
        """
        data = {}
        options = options or {}
        data['taskId'] = taskId
        data.update(options)
        return self._request(self.__liveAuditPullUrl, data)
