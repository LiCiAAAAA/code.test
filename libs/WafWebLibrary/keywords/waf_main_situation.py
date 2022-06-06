#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from ..base import keyword, logger
from ..base import WafWebDriver

class WafMainSituationKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'status': {'type': 'click', 'locator': 'link:状态',},
        'sys_situation': {'type': 'click', 'locator': 'link:系统概况',},
        'cpu_percent': {'type': 'get', 'locator': 'id:rt.cpu.pencent',},
        'mem_percent': {'type': 'get', 'locator': 'id:rt.mem.pencent',},
        'hds_percent': {'type': 'get', 'locator': 'id:rt.hds.pencent',},
        'hdu_percent': {'type': 'get', 'locator': 'id:rt.hdu.pencent',},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()

    @keyword
    def click_status(self):
        self.operate_element(self.__elements['status'])

    @keyword
    def click_sys_situation(self):
        self.operate_element(self.__elements['sys_situation'])

    @keyword
    def obtain_situation(self):
        sys_situation = {}
        sys_situation['cpu_percent'] = self.operate_element(self.__elements['cpu_percent']).text[:-1]
        sys_situation['mem_percent'] = self.operate_element(self.__elements['mem_percent']).text[:-1]
        sys_situation['hds_percent'] = self.operate_element(self.__elements['hds_percent']).text[:-1]
        sys_situation['hdu_percent'] = self.operate_element(self.__elements['hdu_percent']).text[:-1]
        return sys_situation