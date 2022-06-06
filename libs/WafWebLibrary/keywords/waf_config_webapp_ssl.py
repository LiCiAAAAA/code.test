#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigWebappSslKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'ssl_cer': {'type': 'click', 'locator': 'link:证书管理'},
        'add_cer': {'type': 'click', 'locator': 'css:label:nth-child(1)'},
        'upload_cer': {'type': 'input', 'locator': 'id:upload-file-select'},
        'upload': {'type': 'click', 'locator': 'css:#file-upload label'},
        'save': {'type': 'click', 'locator': 'css:.button-primary label'},
        'check_alert': {'type': 'alert', 'action': 'ACCEPT', 'sleep': 60, 'check': '成功' },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_cer_manager(self, **kwargs):
        self.operate_element(self.__elements['ssl_cer'], **kwargs)

    @keyword
    def add_cer(self, **kwargs):
        kwargs =  kwargs.get('file_path') 
        cer_path = kwargs.get('cer_path')
        key_path = kwargs.get('key_path')
        pem_path = kwargs.get('pem_path')
        self.operate_element(self.__elements['add_cer'])
        self.operate_element(self.__elements['upload_cer'], cer_path)
        self.operate_element(self.__elements['upload'])
        self.operate_element(self.__elements['upload_cer'], key_path)
        self.operate_element(self.__elements['upload'])
        if pem_path:
            self.operate_element(self.__elements['upload_cer'], pem_path)
            self.operate_element(self.__elements['upload'])
        self.operate_element(self.__elements['save'])

    @keyword
    def check_ssl_save(self, **kwargs):
        self.operate_element(self.__elements['check_alert'])
