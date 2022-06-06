#!/usr/bin/env python
# -*- coding:utf-8 -*-

from copy import deepcopy
from time import sleep
from ..base import keyword, logger
from ..base import WafWebDriver

class WafLogsAlarmsKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'log': {'type': 'click', 'locator': 'link:日志',},
        'alarms_log': {'type': 'click', 'locator': 'link:应用防护日志',},
        'alarms_log_item': {'type': 'click', 'locator': 'css:tr:nth-child(1) .fa'},
        'hostname': {'type': 'get', 'locator': 'css:#alarm-detail #detail-hostname',},
        'event': {'type': 'get', 'locator': 'css:#alarm-detail #detail-event',},
        'match': {'type': 'get', 'locator': 'css:#alarm-detail #detail-match',},
        'method': {'type': 'get', 'locator': 'css:#alarm-detail #detail-method',},
        'rule_num': {'type': 'get', 'locator': 'link:%s',},
        'rule_desc': {'type': 'get', 'locator': 'css:#alarm-detail #detail-rule-desc',},
        'detail_tag': {'type': 'get', 'locator': 'css:#alarm-detail #detail-tag',},
        'src_ip': {'type': 'get', 'locator': 'css:#detail-source > span',},
        'dst_ip': {'type': 'get', 'locator': 'css:#alarm-detail #detail-dest',},
        'url': {'type': 'get', 'locator': 'css:#alarm-detail #detail-url',},
        'detail_agent': {'type': 'get', 'locator': 'css:#alarm-detail #detail-agent',},
        'ip_location': {'type': 'get', 'locator': 'css:#alarm-detail #detail-iplocation',},
        'detail_content': {'type': 'click', 'locator': "xpath://button[contains(.,'详细')]",},
        'select_el': {'type': 'select', 'locator': 'css:#extra-info td:nth-child(2) > select',},
        'log_content': {'type': 'get', 'locator': 'css:#extra-info p',},
        'close_log': {'type': 'click', 'locator': "xpath://button[contains(.,'关闭')]",},
        
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_log(self):
        self.operate_element(self.__elements['log'])

    @keyword
    def click_alarms_log(self):
        self.operate_element(self.__elements['alarms_log'])

    @keyword
    def check_alarms_log(self, **kwargs):
        kwargs = kwargs.get('cfg')
        select_el = kwargs.get('select_el')
        if select_el:
            select_el = kwargs.pop('select_el')
            log_content = kwargs.pop('log_content')
        self.operate_element(self.__elements['alarms_log_item'])
        for d_key in kwargs:
            if d_key == 'rule_num':
                elements = deepcopy(self.__elements[d_key])
                elements['locator'] = elements['locator'] % kwargs[d_key]
                el_txt = self.operate_element(elements[d_key]).text
            else:
                el_txt = self.operate_element(self.__elements[d_key]).text
            if not kwargs[d_key] in el_txt:
                raise Exception('日志内容: %s 与 实际内容: %s 不符' % (el_txt, kwargs[d_key]))
        if select_el:
            self.operate_element(self.__elements['detail_content'])
            el_txt = self.operate_element(self.__elements[d_key]).text
            if not log_content in el_txt:
                raise Exception('日志内容: %s 与 实际内容: %s 不符' % (el_txt, log_content))
            self.operate_element(self.__elements['close_log'])
        self.operate_element(self.__elements['close_log'])