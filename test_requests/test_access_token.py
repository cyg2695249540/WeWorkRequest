# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_access_token.py
# @Author   : Pluto.
# @Time     : 2020/10/20 17:00
import pytest
import requests

#token验证
class TestAccessToken():

    @pytest.mark.parametrize("corpid,corpsecret,errmsg",
                             [("ww0ae123b953d2b956", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "ok"),
                              ("", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "corpid missing"),
                              ("ww0ae123b953d2b956", "", "corpsecret missing")],
                             ids={"get token ok", "no corpid", "no corpsecret"})
    def test_token(self, corpid, corpsecret,errmsg):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        _corpid = "ww0ae123b953d2b956"
        _corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        r = requests.get(url=url)
        assert r.json()["errmsg"] == errmsg
