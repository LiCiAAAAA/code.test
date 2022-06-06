#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafRulesCustomMainKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'custom_rules': {'type': 'click', 'locator': 'link:自定义规则',},
        'create_rules': {'type': 'click', 'locator': 'css:#custom-list-create label',},
        'rule_content': {'type': 'input', 'locator': 'css:tbody:nth-child(2) > tr:nth-child(2) .input-text',},
        'html_decode': {'type': 'click', 'locator': 'id:decode-type-1-2',},
        'lowercase_decode': {'type': 'click', 'locator': 'id:decode-type-1-3',},
        'url_decode': {'type': 'click', 'locator': 'id:decode-type-1-4',},
        'custom_msg': {'type': 'input', 'locator': 'id:custom.content.message',},
        'severity': {'type': 'select', 'locator': 'id:custom.content.severity',},
        'alarm': {'type': 'select', 'locator': 'id:custom.content.alarm',},
        'action': {'type': 'select', 'locator': 'id:custom.content.action',},
        'rsp_code': {'type': 'select', 'locator': 'id:custom.content.response',},
        'apply_rule': {'type': 'click', 'locator': 'id:custom.apply.rule.%s',},
        'content_save': {'type': 'click', 'locator': 'css:#custom\\.save label',},
        'save_rules': {'type': 'click', 'locator': 'id:custom-list-save',},
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()

    @keyword
    def click_custom_rules(self):
        self.operate_element(self.__elements['custom_rules'])

    @keyword
    def create_rules(self, **kwargs):
        kwargs = kwargs.get('cfg')
        rule_content = kwargs.get('rule_content')
        custom_msg = kwargs.get('custom_msg')
        severity = kwargs.get('severity')
        alarm = kwargs.get('alarm')
        action = kwargs.get('action')
        rsp_code = kwargs.get('rsp_code')
        apply_rule = kwargs.get('apply_rule')
        el_dic = self.handle_locator(self.__elements['apply_rule'], apply_rule)
        self.operate_element(self.__elements['create_rules'])
        self.operate_element(self.__elements['rule_content'], rule_content)
        self.operate_element(self.__elements['custom_msg'], custom_msg)
        self.operate_element(self.__elements['severity'], severity)
        self.operate_element(self.__elements['alarm'], alarm)
        self.operate_element(self.__elements['action'], action)
        self.operate_element(self.__elements['rsp_code'], rsp_code)
        self.operate_element(el_dic)
        self.operate_element(self.__elements['content_save'])

    @keyword
    def save_custom_rules_list(self):
        self.operate_element(['save_rules'])