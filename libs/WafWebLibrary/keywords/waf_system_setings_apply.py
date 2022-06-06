#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import timeout


import time
from ..base import keyword, logger
from ..base import WafWebDriver

class WafSystemSettingsApplyKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'app_changes': { 'type': 'click', 'locator': 'xpath://*[@id="waf-apply-settings"]',},
        'confirm': { 'type': 'click', 'locator': 'css:.button-primary label',},
        'check_alert': {'type': 'alert', 'action': 'ACCEPT', 'sleep': 60, 'check': '成功' },
        'changes_item': { 'type': 'get', 'locator': 'css:td:nth-child(3)',},
    }

    def __init__(self):
        super().__init__()

    @keyword
    def click_apply_changes(self):
        self.operate_element(self.__elements['app_changes'])

    @keyword
    def confirm_apply(self):
        self.operate_element(self.__elements['confirm'])

    @keyword
    def check_apply_changes(self):
        self.operate_element(self.__elements['check_alert'])
        time.sleep(10) #等待站点可防护

    @keyword
    def check_changes_item(self, **kwargs):
        kwargs = kwargs.get('cfg')
        changes_item = kwargs.get('changes_item')
        el_text = self.operate_element(['changes_item']).text
        if changes_item not in el_text:
            raise Exception('应用更改内容: %s 与实际内容: %s 不符' % (el_text, changes_item))
