#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigWebappListKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'config': { 'type': 'click', 'locator': 'link:配置'},
        'site': { 'type': 'click', 'locator': 'link:保护站点'},
        'add_site': { 'type': 'click', 'locator': 'link:添加保护站点'},
        'site_name': { 'type': 'input', 'locator': 'id:webapp.name',},
        'site_ip': { 'type': 'input', 'locator': 'id:webapp.ip',},
        'site_port': { 'type': 'input', 'locator': 'id:webapp.port',},
        'linkage_protect': { 'type': 'click', 'locator': 'id:webapp-linkage-%s'},
        'save_site': { 'type': 'click', 'locator': 'css:.button-primary label'},
        # 'clear_site': { 'type': 'get', 'locator': 'link:清空保护站点'},
        'clear_site': { 'type': 'get', 'locator': 'link:清空'},
        'handle_alert': {'type': 'alert', 'action': 'ACCEPT'},
        'modify': { 'type': 'click', 'locator': 'link:修改'},
        'open_https': { 'type': 'select', 'locator': 'id:webapp.https'},
        'set_run_status': { 'type': 'select', 'locator': 'css:.coml-right > select'},
        'frontend_port': { 'type': 'input', 'locator': 'id:webapp.frontend.port'},
        'frontend_interface': { 'type': 'select', 'locator': 'id:webapp.linkage.frontend.interface'},
        'backend_interface': { 'type': 'select', 'locator': 'id:webapp.linkage.backend.interface'},
        'frontend_ip': { 'type': 'input', 'locator': 'id:webapp.linkage.frontend.ip'},
        'backend_ip': { 'type': 'input', 'locator': 'id:webapp.linkage.backend.ip'},
        'frontend_netmask': { 'type': 'input', 'locator': 'id:webapp.linkage.frontend.netmask'},
        'backend_netmask': { 'type': 'input', 'locator': 'id:webapp.linkage.backend.netmask'},
        'frontend_gateway': { 'type': 'input', 'locator': 'id:webapp.linkage.frontend.gateway'},
    }
    
    TRANSPARENT = 'transparent'
    REVERSE = 'reverse'
    BYPASS= 'bypass'
    
    def __init__(self):
        super().__init__()

    @keyword
    def click_config(self):
        self.operate_element(self.__elements['config'])

    @keyword
    def click_site(self):
        self.operate_element(self.__elements['site'])

    @keyword
    def click_add_site(self):
        self.operate_element(self.__elements['add_site'])

    @keyword
    def add_site_config(self, **kwargs):
        kwargs = kwargs.get('site_config')
        site_name = kwargs.get('site_name')
        site_ip = kwargs.get('site_ip')
        site_port = kwargs.get('site_port')
        el_dic = self.handle_locator(self.__elements['linkage_protect'], kwargs.get('linkage_protect'))
        self.operate_element(self.__elements['site_name'], site_name)
        self.operate_element(self.__elements['site_ip'], site_ip)
        self.operate_element(self.__elements['site_port'], site_port)
        self.operate_element(el_dic)
        self.operate_element(self.__elements['save_site'])

    @keyword
    def modify_site(self, **kwargs):
        kwargs = kwargs.get('https_site_config')
        site_port = kwargs.get('site_port')
        https_status = kwargs.get('https_status')
        self.operate_element(self.__elements['modify'])
        self.operate_element(self.__elements['site_port'], site_port)
        self.operate_element(self.__elements['open_https'], https_status)
        self.operate_element(self.__elements['save_site'])

    @keyword
    def clear_site(self):
        el = self.operate_element(self.__elements['clear_site'])
        if el:
            el.click()
            self.operate_element(self.__elements['handle_alert'])

    @keyword
    def set_run_status(self, **kwargs):
        kwargs = kwargs.get('cfg')
        deploy = kwargs.get('deploy')
        run_status = kwargs.get('run_status')
        self.operate_element(self.__elements['set_run_status'], run_status)
        self.handle_alert()
        if deploy == self.REVERSE:
            self.handle_alert()
        self.handle_alert()

    @keyword
    def add_reverse_site(self, **kwargs):
        kwargs = kwargs.get('cfg')
        site_name = kwargs.get('site_name')
        site_ip = kwargs.get('site_ip')
        site_port = kwargs.get('site_port')
        frontend_port = kwargs.get('frontend_port')
        frontend_interface = kwargs.get('frontend_interface')
        backend_interface = kwargs.get('backend_interface')
        if not backend_interface:
            backend_interface = frontend_interface
        frontend_ip = kwargs.get('frontend_ip')
        backend_ip = kwargs.get('backend_ip')
        if not backend_ip:
            backend_ip = frontend_ip
        netmask = kwargs.get('netmask')
        gateway = kwargs.get('frontend_gateway')
        self.operate_element(self.__elements['site_name'], site_name)
        self.operate_element(self.__elements['site_ip'], site_ip)
        self.operate_element(self.__elements['site_port'], site_port)
        self.operate_element(self.__elements['frontend_port'], frontend_port)
        self.operate_element(self.__elements['frontend_interface'], frontend_interface)
        self.operate_element(self.__elements['backend_interface'], backend_interface)
        self.operate_element(self.__elements['frontend_ip'], frontend_ip)
        self.operate_element(self.__elements['backend_ip'], backend_ip)
        self.operate_element(self.__elements['frontend_netmask'], netmask)
        self.operate_element(self.__elements['backend_netmask'], netmask)
        self.operate_element(self.__elements['frontend_gateway'], gateway)
        self.operate_element(self.__elements['save_site'])
