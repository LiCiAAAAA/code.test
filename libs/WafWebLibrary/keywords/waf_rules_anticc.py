#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import timeout
from ..base import keyword, logger
from ..base import WafWebDriver


class WafRulesAnticcKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'strategy': {'type': 'click', 'locator': 'link:策略' },
        'anticc': {'type': 'click', 'locator': 'LINK:行为分析' },
        'anticc_config': {'type': 'click', 'locator': 'css:span:nth-child(3) label'},
        'runtype': {'type': 'select', 'locator': 'id:anticc-runtype'},
        'anticc_config_save': {'type': 'click', 'locator': 'css:.button-primary label'},
        'check_anticc_save': {'type': 'alert', 'action': 'ACCEPT', 'check': '成功' },
        'create_anticc': {'type': 'click', 'locator': 'link:新建规则' },
        'ip_check': {'type': 'select', 'locator': 'id:ip-check'},
        'ip_method': {'type': 'select', 'locator': 'id:ip-method'},
        'add_measure': {'type': 'click', 'locator': 'link:添加测量指标'},
        'opthins_speed': {'type': 'select', 'locator': 'css:#check-options-container select'},
        'detect_cycle': {'type': 'input', 'locator': 'css:#check-options-container p:nth-child(1) > span:nth-child(2) > .input-text'},
        'access_threshold': {'type': 'input', 'locator': 'css:#check-options-container p:nth-child(1) > span:nth-child(4) > .input-text'},
        'block': {'type': 'click', 'locator': 'css:#check-options-container span:nth-child(2) > label:nth-child(2)'},
        'anticc_name': {'type': 'input', 'locator': 'id:title'},
        'save_anticc': {'type': 'click', 'locator': 'css:.button-primary label'},
        'anticc_enable': {'type': 'click', 'locator': 'css:.button-primary label'},
        'del_anticc': {'type': 'click', 'locator': 'xpath://td[3]/span[2]/a/span/span/label'},
        'handle_alert': {'type': 'alert', 'action': 'ACCEPT'},
        'check_anticc_rule': {'type': 'alert', 'action': 'ACCEPT', 'check': '成功' },
        'cc_slow': {'type': 'click', 'locator': 'css:span:nth-child(2) label'},
        'cc_slow_status': {'type': 'select', 'locator': 'id:anticc-slow'},
        'timeout': {'type': 'input', 'locator': 'id:http-request-timeout'},
        'cc_slow_save': {'type': 'click', 'locator': 'css:.button-primary label'},
    }

    def __init__(self):
        super().__init__()

    @keyword
    def click_strategy(self):
        self.operate_element(self.__elements['strategy'])
    
    @keyword
    def click_anticc(self):
        self.operate_element(self.__elements['anticc'])

    @keyword
    def anticc_config(self):
        self.operate_element(self.__elements['anticc_config'])

    @keyword
    def enable_anticc(self, *args):
        self.operate_element(self.__elements['runtype'], *args)
        self.operate_element(self.__elements['anticc_config_save'])

    @keyword
    def check_anticc_save(self):
        self.operate_element(self.__elements['check_anticc_save'])
    
    @keyword
    def create_new_anticc(self):
        self.operate_element(self.__elements['create_anticc'])

    @keyword
    def anticc_rule(self, **kwargs):
        kwargs = kwargs.get('anticc_cfg')
        check_obj = kwargs.get('ip_check')
        method_obj = kwargs.get('ip_method')
        detect_cycle = kwargs.get('detect_cycle')
        access_threshold = kwargs.get('access_threshold')
        title = kwargs.get('title')
        self.operate_element(self.__elements['ip_check'], check_obj)
        self.operate_element(self.__elements['ip_method'], method_obj)
        self.operate_element(self.__elements['add_measure'])
        self.operate_element(self.__elements['detect_cycle'], detect_cycle)
        self.operate_element(self.__elements['access_threshold'], access_threshold)
        self.operate_element(self.__elements['block'])
        self.operate_element(self.__elements['anticc_name'], title)
        self.operate_element(self.__elements['save_anticc'])

    @keyword
    def modify_cc_check_obj(self, **kwargs):
        obj = kwargs.get('cfg')

    @keyword
    def check_anticc_rule_save(self):
        self.operate_element(self.__elements['handle_alert'])
        self.operate_element(self.__elements['check_anticc_rule'])

    @keyword
    def apply_rule(self):
        self.operate_element(self.__elements['anticc_enable'])
        self.operate_element(self.__elements['check_anticc_rule'])

    @keyword
    def del_anticc_rule(self):
        self.operate_element(self.__elements['del_anticc'])
        self.operate_element(self.__elements['handle_alert'])

    @keyword
    def enable_cc_slow(self, **kwargs):
        kwargs = kwargs.get('cfg')
        timeout = kwargs.get('timeout')
        cc_slow_status = kwargs.get('cc_slow_status')
        self.operate_element(['cc_slow'])
        self.operate_element(['cc_slow_status'], cc_slow_status)
        self.operate_element(['timeout'], timeout)
        self.operate_element(['cc_slow_save'])
