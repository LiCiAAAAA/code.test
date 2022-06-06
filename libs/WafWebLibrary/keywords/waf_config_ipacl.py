#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigIpaclKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'ipacl': {'type': 'click', 'locator': 'link:网络层IP白名单',},
        'create_ipacl': {'type': 'click', 'locator': 'link:新建白名单',},
        'white_ip': {'type': 'input', 'locator': 'id:ipacl-content',},
        'save': {'type': 'click', 'locator': 'link:保存',},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_ipacl(self):
        self.operate_element(self.__elements['ipacl'])

    @keyword
    def create_ipacl(self, **kwargs):
        kwargs = kwargs.get('cfg')
        white_ip = kwargs.get('white_ip')
        self.operate_element(self.__elements['create_ipacl'])
        self.operate_element(self.__elements['white_ip'], white_ip)
        self.operate_element(self.__elements['save'])