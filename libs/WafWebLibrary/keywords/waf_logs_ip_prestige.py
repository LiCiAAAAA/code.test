#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafLogsIpPrestigeKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    # @keyword
    # def haha(self, **kwargs):
        # self.operate_element(self.__elements['main'], **kwargs)
    
    