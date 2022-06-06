#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigMonitorKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'cfg_monitor': {'type': 'click', 'locator': 'link:监控管理',},
        'snmp_v2': {'type': 'click', 'locator': 'id:snmp.enabled.v2',},
        'snmp_v3': {'type': 'click', 'locator': 'id:snmp.enabled.v3',},
        'snmp_name': {'type': 'input', 'locator': 'id:snmp-device-name',},
        'snmp_community': {'type': 'input', 'locator': 'id:snmp-community',},
        'encrypt_type': {'type': 'select', 'locator': 'id:snmp.encrypt_type',},
        'encrypt_pwd': {'type': 'input', 'locator': 'id:snmp-encrypt-password',},
        'username': {'type': 'input', 'locator': 'id:snmp-auth-username',},
        'auth_pwd': {'type': 'input', 'locator': 'id:snmp-auth-password',},
        'auth_type': {'type': 'select', 'locator': 'id:snmp.auth_type',},
        'snmp_save': {'type': 'click', 'locator': 'id:global.snmp.save',},
        'snmp_status': {'type': 'get', 'locator': 'id:global.snmp.status',},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_cfg_monitor(self):
        self.operate_element(self.__elements['cfg_monitor'])

    @keyword
    def enable_snmp(self, snmp_v):
        self.operate_element(self.__elements[snmp_v], snmp_v)
        self.operate_element(self.__elements['snmp_save'])

    @keyword
    def config_snmp(self, **kwargs):
        kwargs = kwargs.get('cfg')
        snmp_name = kwargs.get('snmp_name')
        snmp_community = kwargs.get('snmp_community')
        timeout = kwargs.get('timeout', 60)
        encrypt_type = kwargs.get('encrypt_type')
        encrypt_pwd = kwargs.get('encrypt_pwd')
        # logger.error(encrypt_pwd)
        username = kwargs.get('username')
        auth_pwd = kwargs.get('auth_pwd')
        auth_type = kwargs.get('auth_type')
        start_time = time.time()
        end_time = start_time + timeout
        self.operate_element(self.__elements['snmp_name'], snmp_name)
        if snmp_community:
            self.operate_element(self.__elements['snmp_community'], snmp_community)
        if encrypt_type:
             self.operate_element(self.__elements['encrypt_type'], encrypt_type)
             self.operate_element(self.__elements['encrypt_pwd'], encrypt_pwd)
             self.operate_element(self.__elements['username'], username)
             self.operate_element(self.__elements['auth_pwd'], auth_pwd)
             self.operate_element(self.__elements['auth_type'], auth_type)
        self.operate_element(self.__elements['snmp_save'])
        while start_time < end_time:
            start_time = time.time()
            el = self.operate_element(self.__elements['snmp_status'])
            if not el:
                continue
            msg = el.text
            if not '成功' in msg:
                time.sleep(0.3)
                continue
            return
        raise Exception('预期结果%s, 实际结果%s' % ('成功', msg))

    @keyword
    def check_snmp_cmd_result(self, **kwargs):
        dev_ip = self._get_url_dict()[-1]['host']
        oid = kwargs.get('oid')
        kwargs = kwargs.get('cfg')
        user = kwargs.get('user')
        pwd = kwargs.get('pwd')
        client_ip = kwargs.get('client_ip')
        cmd = kwargs.get('cmd') % (dev_ip, oid)
        alias = self.ssh_login(client_ip, user, pwd)
        results = self.ssh_exec(cmd, alias)
        return results