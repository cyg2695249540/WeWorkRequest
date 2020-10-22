# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api.py
# @Author   : Pluto.
# @Time     : 2020/10/22 10:46
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:
    def send_requests(self,req:dict):
        return requests.request(**req)

    def base_jsonpath(self,obj,json_expression):
        return jsonpath(obj,json_expression)

    def base_jsonschema(self,instance, schema):
        return validate(instance, schema)