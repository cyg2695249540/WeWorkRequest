# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/21 10:28
from time import sleep

from selenium.webdriver.common.by import By

from test_wework.page.base_page import BasePage


class ContactPage(BasePage):
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _adddepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def get_contact_list(self):
        self.wait_for_clickable(self._member_list)
        ele = self.finds(self._member_list)
        return [name.text for name in ele]

    def go_to_addmember_page(self):
        from test_wework.page.addmember_page import AddMemberPage
        while True:
            self.find_and_click(self._addmember_butto)
            try:
                self.find(self._cancel_member)
                break
            except:
                print("再次点击")
        return AddMemberPage(self.driver)

    def go_to_adddepartment_page(self):
        from test_wework.page.adddepartment_page import AddDepartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._adddepartment)
        return AddDepartmentPage()

    def get_department_list(self):
        # self.wait_for_clickable(self._jstree_anchor)
        sleep(1)
        ele = self.finds(self._jstree_anchor)
        return [name.text for name in ele]
