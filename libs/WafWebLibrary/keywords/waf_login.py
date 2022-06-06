#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver


class WafLoginKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        'pwd': { 'type': 'input', 'locator': 'id:user_pass', 'hide': True, },
        'login': {'type': 'click', 'locator': 'id:user_login', },
        'loginerr': {'type': 'alert', 'action': 'ACCEPT', 'check': '无法登录' },
        'pwdexpired': {'type': 'alert', 'action': 'DISMISS', 'check': '天后过期' },
        'userpanel':  {'type': 'click', 'locator': 'id:user-panel', },
        'loginout': {'type': 'click', 'locator': 'link:注销', },
    }
    def __init__(self):
        super().__init__()
    
    @keyword
    def waf_login(self, user, pwd, **kwargs):
        self.operate_element(self.__elements['user'], user, **kwargs)
        self.operate_element(self.__elements['pwd'], pwd, **kwargs)
        self.operate_element(self.__elements['login'], **kwargs)

    @keyword
    def login_error(self, **kwargs):
        self.operate_element(self.__elements['loginerr'], **kwargs)
