# -*- coding: utf-8 -*-

"""
自然语言处理
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
import chardet


class AipNlp(AipBase):
    """
    自然语言处理
    """

    __lexerUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'

    __lexerCustomUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer_custom'

    __depParserUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/depparser?charset=UTF-8'

    __wordEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec'

    __dnnlmCnUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn'

    __wordSimEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_sim'

    __simnetUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'

    __commentTagUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag'

    __sentimentClassifyUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'

    __keywordUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword'

    __topicUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/topic?charset=UTF-8'

    __ecnetUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet'

    __emotionUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion'

    __newsSummaryUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/news_summary'

    __addressUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/address'

    __commentTagCustomUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag_custom'
    __sentimentClassifyCustomUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify_custom'
    __coupletsUrl = 'https://aip.baidubce.com/rpc/2.0/creation/v1/couplets'
    __poemUrl = 'https://aip.baidubce.com/rpc/2.0/creation/v1/poem'
    __entityLevelSentimentUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment'
    __entityLevelSentimentAddUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment/add'
    __entityLevelSentimentDeleteUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment/delete'
    __entityLevelSentimentDeleteRepoUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment/delete_repo'
    __entityLevelSentimentListUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment/list'
    __entityLevelSentimentQueryUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_level_sentiment/query'
    __topicPhraseUrl = 'https://aip.baidubce.com/rpc/2.0/creation/v1/topic_phrase'
    __cvparserUrl = 'https://aip.baidubce.com/rpc/2.0/recruitment/v1/cvparser'
    __personPostUrl = 'https://aip.baidubce.com/rpc/2.0/recruitment/v1/person_post'
    __personasUrl = 'https://aip.baidubce.com/rpc/2.0/recruitment/v1/personas'
    __titlepredictorUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/titlepredictor'
    __depparserV2Url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/depparser'
    __blessCreationUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/bless_creation'
    __entityAnalysisUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/entity_analysis'


    def _proccessResult(self, content):
        """
            formate result
        """

        if sys.version_info.major == 2:
            if chardet.detect(content).get('encoding') == 'utf-8':
                return json.loads(content.decode('utf8', 'ignore').encode('utf8')) or {}
            return json.loads(content.decode('gbk', 'ignore').encode('utf8')) or {}
        else:
            if chardet.detect(content).get('encoding') == 'utf-8':
                return json.loads(str(content, 'utf8')) or {}
            return json.loads(str(content, 'gbk')) or {}

    def _proccessRequest(self, url, params, data, headers):
        """
            _proccessRequest
        """

        if sys.version_info.major == 2:
            if 'UTF-8' in url:
                return json.dumps(data, ensure_ascii=False)
            return json.dumps(data, ensure_ascii=False).decode('utf8').encode('gbk', 'ignore')
        else:
            if 'UTF-8' in url:
                return json.dumps(data, ensure_ascii=False).encode('utf8')
            return json.dumps(data, ensure_ascii=False).encode('gbk', 'ignore')

    def lexer(self, text, options=None):
        """
            词法分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__lexerUrl, data)

    def lexerCustom(self, text, options=None):
        """
            词法分析（定制版）
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__lexerCustomUrl, data)

    def depParser(self, text, options=None):
        """
            依存句法分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__depParserUrl, data,
                             {'Content-Type': 'application/json;charset=utf-8'})

    def wordEmbedding(self, word, options=None):
        """
            词向量表示
        """
        options = options or {}

        data = {}
        data['word'] = word

        data.update(options)

        return self._request(self.__wordEmbeddingUrl, data)

    def dnnlm(self, text, options=None):
        """
            DNN语言模型
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__dnnlmCnUrl, data)

    def wordSimEmbedding(self, word_1, word_2, options=None):
        """
            词义相似度
        """
        options = options or {}

        data = {}
        data['word_1'] = word_1
        data['word_2'] = word_2

        data.update(options)

        return self._request(self.__wordSimEmbeddingUrl, data)

    def simnet(self, text_1, text_2, options=None):
        """
            短文本相似度
        """
        options = options or {}

        data = {}
        data['text_1'] = text_1
        data['text_2'] = text_2

        data.update(options)

        return self._request(self.__simnetUrl, data)

    def commentTag(self, text, options=None):
        """
            评论观点抽取
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__commentTagUrl, data)

    def sentimentClassify(self, text, options=None):
        """
            情感倾向分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__sentimentClassifyUrl, data)

    def keyword(self, title, content, options=None):
        """
            文章标签
        """
        options = options or {}

        data = {}
        data['title'] = title
        data['content'] = content

        data.update(options)

        return self._request(self.__keywordUrl, data)

    def topic(self, title, content, options=None):
        """
            文章分类
        """
        options = options or {}

        data = {}
        data['title'] = title
        data['content'] = content

        data.update(options)

        return self._request(self.__topicUrl, data)

    def ecnet(self, text, options=None):
        """
            文本纠错
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__ecnetUrl, data)

    def emotion(self, text, options=None):
        """
            对话情绪识别接口
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__emotionUrl, data)

    def newsSummary(self, content, max_summary_len, options=None):
        """
            新闻摘要接口
        """
        options = options or {}

        data = {}
        data['content'] = content
        data['max_summary_len'] = max_summary_len

        data.update(options)

        return self._request(self.__newsSummaryUrl, data)

    def address(self, text, options=None):
        """
            地址识别接口
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__addressUrl, data)

    def commentTagCustom(self, text, options=None):
        """
            评论观点抽取（定制）
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/ok6z52g8q
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__commentTagCustomUrl, data)

    def sentimentClassifyCustom(self, text, options=None):
        """
            情感倾向分析（定制）
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/zk6z52hds
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__sentimentClassifyCustomUrl, data)

    def couplets(self, text, options=None):
        """
            智能春联
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Ok53wb6dh
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__coupletsUrl, data)

    def poem(self, text, options=None):
        """
            智能写诗
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/ak53wc3o3
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__poemUrl, data)

    def entityLevelSentiment(self, title, content, type, options=None):
        """
            实体抽取与情感倾向分析
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04
        """
        options = options or {}

        data = {}
        data['title'] = title
        data['content'] = content
        data['type'] = type

        data.update(options)

        return self._request(self.__entityLevelSentimentUrl, data)

    def entityLevelSentimentAdd(self, repository, entities, options=None):
        """
            增加实体/实体库新增
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04#%E5%AE%9E%E4%BD%93%E5%BA%93%E6%96%B0%E5%A2%9E%E6%8E%A5%E5%8F%A3
        """
        options = options or {}

        data = {}
        data['repository'] = repository
        data['entities'] = entities

        data.update(options)

        return self._request(self.__entityLevelSentimentAddUrl, data)

    def entityLevelSentimentDelete(self, repository, entities, options=None):
        """
            删除实体/实体名单删除
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04#%E5%AE%9E%E4%BD%93%E5%90%8D%E5%8D%95%E5%88%A0%E9%99%A4%E6%8E%A5%E5%8F%A3
        """
        options = options or {}

        data = {}
        data['repository'] = repository
        data['entities'] = entities

        data.update(options)

        return self._request(self.__entityLevelSentimentDeleteUrl, data)

    def entityLevelSentimentDeleteRepo(self, repositories, options=None):
        """
            删除实体库/实体库删除
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04#%E5%AE%9E%E4%BD%93%E5%BA%93%E5%88%A0%E9%99%A4%E6%8E%A5%E5%8F%A3
        """
        options = options or {}

        data = {}
        data['repositories'] = repositories

        data.update(options)

        return self._request(self.__entityLevelSentimentDeleteRepoUrl, data)

    def entityLevelSentimentList(self, options=None):
        """
            实体库列表/实体库查询
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04#%E5%AE%9E%E4%BD%93%E5%BA%93%E6%9F%A5%E8%AF%A2%E6%8E%A5%E5%8F%A3
        """
        options = options or {}
        data = {}
        data.update(options)

        return self._request(self.__entityLevelSentimentListUrl, data)

    def entityLevelSentimentQuery(self, repository, options=None):
        """
            查询实体/实体名单查询
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Fk6z52g04#%E5%AE%9E%E4%BD%93%E5%90%8D%E5%8D%95%E6%9F%A5%E8%AF%A2%E6%8E%A5%E5%8F%A3
        """
        options = options or {}

        data = {}
        data['repository'] = repository

        data.update(options)

        return self._request(self.__entityLevelSentimentQueryUrl, data)

    def topicPhrase(self, title, summary, options=None):
        """
            文章主题短语生成
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/9k53w3qob
        """
        options = options or {}

        data = {}
        data['title'] = title
        data['summary'] = summary

        data.update(options)

        return self._request(self.__topicPhraseUrl, data)

    def recruitmentCvparser(self, resume, options=None):
        """
            智能招聘-简历解析
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Xkahvfeqa
        """
        options = options or {}

        data = {}
        data['resume'] = resume

        data.update(options)

        return self._request(self.__cvparserUrl, data)

    def recruitmentPersonPost(self, resume, job_description, options=None):
        """
            智能招聘-人岗匹配
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/Pkahwzux5
        """
        options = options or {}

        data = {}
        data['resume'] = resume
        data['job_description'] = job_description

        data.update(options)

        return self._request(self.__personPostUrl, data)

    def recruitmentPersonas(self, resume, options=None):
        """
            智能招聘-简历画像
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/5kc1kmz3w
        """
        options = options or {}

        data = {}
        data['resume'] = resume

        data.update(options)

        return self._request(self.__personasUrl, data)

    def titlepredictor(self, doc, options=None):
        """
            文章标题生成
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/0kvc1u1eg
        """
        options = options or {}

        data = {}
        data['doc'] = doc

        data.update(options)

        return self._request(self.__titlepredictorUrl, data)
        
    def depParserV2(self, text, options=None):
        """
            依存句法分析V2
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/nk6z52eu6
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__depparserV2Url, data)

    def blessCreation(self, text, options=None):
        """
            祝福语生成
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/sl4cg75jk
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__blessCreationUrl, data)

    def entityAnalysis(self, text, options=None):
        """
            实体分析
            接口文档链接: https://ai.baidu.com/ai-doc/NLP/al631z295
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__entityAnalysisUrl, data)

