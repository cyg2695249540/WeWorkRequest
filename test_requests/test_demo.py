# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/10/21 14:09
import requests


class Testdemo():
    def setup(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(url=token_url, params=params)
        self.token = r.json()["access_token"]
        self.id = 4

    def teardown(self):
        pass

    def test_create_department(self):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token": self.token
        }
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 3,
            "id": self.id
        }
        r = requests.post(url=create_url, params=params, json=data)
        assert r.json()["errmsg"] == "created"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list"
        list = requests.get(url=get_department_list_url, params=params)
        assert list.json()["department"][self.id - 1]["name"] == "技术部"

    def test_update_department(self):
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        params = {
            "access_token": self.token
        }
        data = {
            "id": self.id,
            "name": "测试研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, params=params, json=data)
        assert r.json()["errmsg"] == "updated"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list"
        list = requests.get(url=get_department_list_url, params=params)
        assert list.json()["department"][self.id - 1]["name"] == "测试研发中心"

    def test_delete_department(self):
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {
            "access_token": self.token,
            "id": self.id
        }
        r = requests.get(url=delete_url, params=params)
        assert r.json()["errmsg"] == "deleted"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url)
        assert len(list.json()["department"]) == self.id - 1
