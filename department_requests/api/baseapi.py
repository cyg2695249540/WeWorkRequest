# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : baseapi.py
# @Author   : Pluto.
# @Time     : 2020/10/21 15:21
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:
    # requests二次封装
    def send_requests(self, req: dict):
        # 不定长关键字传参
        # 字典解包进行关键字传参
        return requests.request(**req)

    def base_jsonpath(self, obj, json_expression):
        return jsonpath(obj, json_expression)

    def base_jsonschema(self,instance, schema):
        return validate(instance, schema)
