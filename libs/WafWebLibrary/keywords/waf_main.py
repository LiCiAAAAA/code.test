#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafMainKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'main': { 'type': 'click', 'locator': 'css:span', },
        'about': { 'type': 'click', 'locator': 'css:span.nav-collapse-hide',},
        'about-exit': {'type': 'click', 'locator': 'css:button.ui-state-default.ui-corner-all', },
        'apply': { 'type': 'click', 'locator': 'id:waf-apply-settings', },
        'runtype': { 'type': 'click', 'locator': 'link:运行模式', },
        'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
        'normal': { 'type': 'click', 'locator': 'link:正常防护', 'sleep': 2, },
        'normal-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成','sleep': 6, },
        'apply-ok': {'type': 'alert', 'action': 'ACCEPT', 'check': '应用更改', },
        'userpanel':  {'type': 'click', 'locator': 'id:user-panel', },
        'loginout': {'type': 'click', 'locator': 'link:注销', },
        'account': {'type': 'click', 'locator': 'link:账户', },
        'pwdexpired': {'type': 'alert', 'action': 'DISMISS', 'check': '天后过期' },
    }

    def __init__(self):
        super().__init__()

    @keyword
    def into_main(self, **kwargs):
        self.operate_element(self.__elements['main'], **kwargs)

    @keyword
    def into_about(self, **kwargs):
        self.operate_element(self.__elements['about'], **kwargs)
    
    @keyword
    def exit_about(self, **kwargs):
        self.operate_element(self.__elements['about-exit'], **kwargs)

    @keyword
    def apply_settings(self, **kwargs):
        self.operate_element(self.__elements['apply'], **kwargs)

    @keyword
    def switch_proxy(self, **kwargs):
        self.operate_element(self.__elements['runtype'], **kwargs)
        self.operate_element(self.__elements['proxy'], **kwargs)
        self.operate_element(self.__elements['proxy-alert'], **kwargs)
        self.operate_element(self.__elements['apply-ok'], **kwargs)

    @keyword
    def switch_normal(self, **kwargs):
        self.operate_element(self.__elements['runtype'], **kwargs)
        self.operate_element(self.__elements['normal'], **kwargs)
        self.operate_element(self.__elements['normal-alert'], **kwargs)
        self.operate_element(self.__elements['apply-ok'], **kwargs)
    
    @keyword
    def into_account(self, **kwargs):
        self.operate_element(self.__elements['userpanel'], **kwargs)
        self.operate_element(self.__elements['account'], **kwargs)

    @keyword
    def login_out(self, **kwargs):
        self.operate_element(self.__elements['userpanel'], **kwargs)
        self.operate_element(self.__elements['loginout'], **kwargs)

    @keyword
    def pwd_expired(self, **kwargs):
        self.operate_element(self.__elements['pwdexpired'], **kwargs)
