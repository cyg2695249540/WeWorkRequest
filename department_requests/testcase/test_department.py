# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/10/21 14:43
import json

import allure
import pytest
import yaml

from department_requests.api.department import Department


@allure.feature("创建部门模块")
class TestDepartment():
    def setup_class(self):
        self.department = Department()
        config_infor = yaml.safe_load(open("config.yaml"))
        # 通过传入不同的secret获取不同的token权限，给不同的测试用例使用
        self.department.get_token(config_infor["token"]["department_secret"])


    @allure.feature("创建部门")
    @pytest.mark.parametrize("id,departmentname", [(4, "技术部")], ids={"创建部门"})
    def test_create_department(self, id, departmentname):
        r = self.department.create_department(id,departmentname)
        assert r["errmsg"] == "created"
        list = self.department.get_department_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={id})].name")[0]
        assert departmentname == name

    @allure.feature("更新部门")
    @pytest.mark.parametrize("id,departmentname", [(4, "测试研发中心")], ids={"更新部门"})
    def test_update_department(self,id,departmentname):
        r = self.department.update_department(id,departmentname)
        assert r["errmsg"] == "updated"
        list = self.department.get_department_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={id})].name")[0]
        assert departmentname == name

    @allure.feature("删除部门")
    @pytest.mark.parametrize("id", [(4)], ids={"删除部门"})
    def test_delete_department(self,id):
        self.department.delete_department(id)
        list = self.department.get_department_list()
        department_id = self.department.base_jsonpath(list, "$..id")
        assert id not in department_id

    @allure.feature("字段格式验证")
    def test_get_department_list(self):
        r = self.department.get_department_list()
        get_list_schema = json.load(open("./json_schema/get_list_schema.json", encoding="utf-8"))
        self.department.base_jsonschema(r, get_list_schema)
