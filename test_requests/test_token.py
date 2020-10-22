# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_token.py
# @Author   : Pluto.
# @Time     : 2020/10/20 15:28
import requests


class TestToken():
    _corpid = "ww0ae123b953d2b956"
    _corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
    _url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

    # 获取token第一种方式
    def test_get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._corpid}&corpsecret={self._corpsecret}"
        r = requests.get(url=url)
        print(r.json())

    # 获取token第二种方式
    def test_get_token_params(self):
        params = {
            "corpid": self._corpid,
            "corpsecret": self._corpsecret
        }
        r = requests.get(url=self._url, params=params)
        print(r.json())
