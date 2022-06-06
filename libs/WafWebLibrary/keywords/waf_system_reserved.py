#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base.utils import *
from ..base import WafWebDriver

class WafSystemreReservedKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'dev_key': {'type': 'input', 'locator': 'dev-key',},
        'commit': {'type': 'click', 'locator': 'css:label:nth-child(1)',},
        'ssh_on': {'type': 'click', 'locator': 'css:#settings\\.submit\\.button\\.ssh\\.on label',},
        'ssh_off': {'type': 'click', 'locator': 'css:#settings\\.submit\\.button\\.ssh\\.off label',},
        'check_on': {'type': 'alert', 'action': 'ACCEPT', 'sleep': 6, 'check': '开启' },
        'check_off': {'type': 'alert', 'action': 'ACCEPT', 'sleep': 6, 'check': '关闭' },
        'tw_recycle_enable': {'type': 'select', 'locator': 'css:td > select',},
        'tw_save': {'type': 'click', 'locator': 'css:#settings\\.save\\.sysctl\\.button label',},
    }

    def __init__(self):
        super().__init__()

    @keyword
    def system_reserved(self, dev_key):
        self.operate_element(self.__elements['dev_key'], dev_key)
        self.operate_element(self.__elements['commit'])

    @keyword
    def ssh_on(self):
        self.operate_element(self.__elements['ssh_on'])
        self.operate_element(self.__elements['check_on'])

    @keyword
    def ssh_off(self):
        self.operate_element(self.__elements['ssh_off'])
        self.operate_element(self.__elements['check_off'])

    @keyword
    def tw_recycle_on(self, **kwargs):
        kwargs = kwargs.get('cfg')
        tw_recycle =kwargs.get('tw_recycle') 
        self.operate_element(self.__elements['tw_recycle_enable'], tw_recycle)
        self.operate_element(self.__elements['tw_save'])

    @keyword
    def check_success(self, timeout=60):
        self.handle_alert('ACCEPT', timeout)

    @keyword
    def custom_request(self, **kwargs):
        other_dic = {}
        cfg = kwargs.get('cfg1')
        request_parames = kwargs.get('cfg2')
        c_header = request_parames.get('header')
        other_dic['headers'] = c_header
        body = request_parames.get('body')
        other_dic['data'] = body
        cookie = request_parames.get('cookie')
        method = request_parames.get('method')
        verify = request_parames.get('verify')
        if verify:
            other_dic['verify'] = verify
        other_dic['verify'] = False
        if cookie:
            cookie_name = request_parames.get('cookie_name')
            cookies = self.c_get_cookie(cookie_name)
            other_dic['cookies'] = cookies
        url = cfg.get('protocol') + cfg.get('master') + kwargs.get('cfg3')
        rsp = custom_req(method, url, **other_dic)
        return rsp

    @keyword
    def waf_req(self, **kwargs):
        other_dic = {}
        request_parames = kwargs.get('cfg2')
        c_header = request_parames.get('header')
        if c_header:
            other_dic['t_headers'] = c_header
        body = request_parames.get('body')
        # other_dic['data'] = body
        method = request_parames.get('method')
        verify = request_parames.get('verify')
        if verify:
            other_dic['verify'] = verify
        other_dic['verify'] = False
        url = request_parames.get('protocol') + kwargs.get('ip') + request_parames.get('path')
        if 'get' in method:
            rsp = self.waf_get(url=url)
        elif 'post' in method:
            rsp = self.waf_post(url=url, data=body,**other_dic)
        return rsp

    @keyword
    def new_custom_request(self,**kwargs):
        other_dic = {}
        request_parames = kwargs.get('cfg2')
        c_header = request_parames.get('header')
        other_dic['headers'] = c_header
        body = request_parames.get('body')
        other_dic['data'] = body
        cookie = request_parames.get('cookie')
        method = request_parames.get('method')
        verify = request_parames.get('verify')
        if verify:
            other_dic['verify'] = verify
        other_dic['verify'] = False
        if cookie:
            cookie_name = request_parames.get('cookie_name')
            # logger.error(self.waf_get(url=url).text)
            cookies = self.c_get_cookie(cookie_name)
            other_dic['cookies'] = cookies
        url = request_parames.get('protocol') + kwargs.get('ip') + request_parames.get('path')
        rsp = custom_req(method, url, **other_dic)
        return rsp