# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2020/10/21 14:34


from department_requests.api.baseapi import BaseApi


class WeWork(BaseApi):
    def get_token(self, corpsecret):
        corpid = "ww0ae123b953d2b956"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": token_url
        }
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
