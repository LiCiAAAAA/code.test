#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigNetworkKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'net_config': { 'type': 'click', 'locator': 'link:网络配置'},
        'del_protect': {'type': 'click', 'locator': 'css:.button-danger label'},
        'create_interface': {'type': 'click', 'locator': 'link:创建接口'},
        'select_inteface_type': {'type': 'select', 'locator': 'xpath://*[@id="dialog-interface-add"]/table/tbody/tr[2]/td[2]/select'},
        'brif': {'type': 'click', 'locator': 'id:brif-%s'},
        'net_save': {'type': 'click', 'locator': 'xpath://button'},
        'check_del_protect': {'type': 'alert', 'action': 'ACCEPT', 'check': '删除'},
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()

    @keyword
    def click_net_config(self):
        self.operate_element(self.__elements['net_config'])

    @keyword
    def del_protect(self):
        self.operate_element(self.__elements['del_protect'])

    @keyword
    def click_create_interface(self):
        self.operate_element(self.__elements['create_interface'])

    @keyword
    def select_inteface_type(self, interface_type):
        self.operate_element(self.__elements['select_inteface_type'], interface_type)

    @keyword
    def create_protect(self, **kwargs):
        brif1 = kwargs.get('brif1')
        brif2 = kwargs.get('brif2')
        brif1 = self.handle_locator(self.__elements['brif'], brif1)
        brif2 = self.handle_locator(self.__elements['brif'], brif2)
        self.operate_element(brif1)
        self.operate_element(brif2)
        self.operate_element(self.__elements['net_save'])

    @keyword
    def check_del_protect(self):
        self.operate_element(self.__elements['check_del_protect'])