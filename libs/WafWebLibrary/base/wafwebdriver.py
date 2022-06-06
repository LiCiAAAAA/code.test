#!/usr/bin/env python
# -*- coding:utf-8 -*-

import copy
from re import L
from requests import HTTPError

from robot.api.deco import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from .utils import *
from SSHLibrary import SSHLibrary
from RequestsLibrary import RequestsLibrary
from SeleniumLibrary import SeleniumLibrary


class WafWebDriver(SeleniumLibrary):
    """
    1. 封装SeleniumLibrary
        1. 原生关键字可以正常使用

    2. 封装RequestsLibrary
        1. 可以对当前窗口的WAF直接执行rpc操作
        2. 当前提供 `waf_get`, 返回为响应输出
        3. 后续如果需要 PUT等其他方法，可以扩展
        4. 如果需要在RF中使用RequestsLibrary原生关键字，需要在RF中手动导入

    3. 封装SSHLibrary
        1. 可以对当前窗口的WAF直接执行ssh操作
        2. 当前提供 `waf_ssh_login`, `waf_ssh_exec`, `waf_ssh_write` 两个命令, 返回为命令输出
        1. `waf_ssh_login` - 登陆shell
        2. `waf_ssh_exec`  - 当前shell执行
        3. 如果需要在RF中使用SSHLibrary原生关键字，需要在RF中手动导入

    """
    __instance = False
    __session = {}   # 'scheme://host:port' : 'alias',

    def __init__(self):
        if self.__instance:
            return
        self.__instance = True
        super().__init__()
        self.os_type = None
        self.ssh = SSHLibrary()
        self.req = RequestsLibrary()
        self.builtin = BuiltIn()

    @keyword
    def get(self, **kwargs):
        kwargs = kwargs.get('req_params')
        url = kwargs.get('url')
        params = kwargs.get('params')
        expected_status = kwargs.get('expected_status')
        msg = kwargs.get('msg')
        verify = kwargs.get('verify')
        if not verify:
            verify = False
        try:
            self.rsp = self.req.session_less_get(
                url, params=params, expected_status=expected_status, msg=msg, verify=verify)
        except HTTPError as ht:
            if ht.response.status_code == 403:
                return
            raise(ht)
        # logger.error(self.rsp)

    @keyword
    def post(self, **kwargs):
        url = kwargs.get('url')
        params = kwargs.get('params')
        expected_status = kwargs.get('expected_status')
        msg = kwargs.get('msg')
        cookies = kwargs.get('cookies')
        verify = kwargs.get('verify')
        if not verify:
            verify = False
        try:
            self.rsp = self.req.session_less_post(
                url, params=params, expected_status=expected_status, msg=msg, verify=verify, cookies=cookies)
            return self.rsp
        except HTTPError as ht:
            if ht.response.status_code == 403:
                return
            raise(ht)
        

    @keyword
    def waf_ssh_exec(self, text, alias=None,sleep=None):
        """
            alias 登陆后默认alias
            sleep 等待返回值的时间
        """
        self._waf_switch_ssh_connection(alias)
        self.ssh.write(text)
        time_wait(sleep)
        return self.ssh.read()

    @keyword
    def ssh_exec(self, text, alias,sleep=None):
        """
            alias 登陆后默认alias
            sleep 等待返回值的时间
        """
        self.ssh.switch_connection(alias)
        self.ssh.write(text)
        time_wait(sleep)
        return self.ssh.read()

    @keyword
    def c_get_cookies(self):
        cookies = {}
        t_co = self.get_cookies()
        t_list = t_co.split(';')
        for item in t_list:
            item_list = item.split('=')
            cookies[item_list[0]] = item_list[-1]
        return cookies

    @keyword
    def c_get_cookie(self, name):
        cookie = {}
        cookie_obj = self.get_cookie(name)
        cookie[name] = cookie_obj.value
        return cookie

    @keyword
    def ssh_login(self,host, username, password, alias=None, port=22, **kwargs):
        if not alias:
            alias = 's_0'
        self.ssh.open_connection(host=host, alias=alias, port=port)
        self.ssh.login(username=username,password=password, **kwargs)
        return alias

    @keyword
    def waf_ssh_login(self, username=None, password=None, url=None,**kwargs):
        url_dict = self._get_url_dict(url)[-1]
        rst, alias = self._get_session_alias(url_dict)
        # if rst:
        #     return alias

        self.ssh.open_connection(host=url_dict['host'], alias=alias, port=url_dict['port'])
        self.ssh.login(username=username,password=password, **kwargs)
        return alias

    def _waf_switch_ssh_connection(self, alias):
        if not alias:
            # 获取当前窗口 alias
            url_dict = self._get_url_dict()[-1]
            alias = self._get_session_alias(url_dict)[-1]
        return self.ssh.switch_connection(alias)

    # @keyword
    # def get_req(self):
    #     self.req.get_request

    @keyword
    def _req_on_session(self, alias, url, method=None, params=None, **kwargs):
        session = self.req._cache.switch(alias)
        if 'get' in method:
            response = self.req._common_request("get", session, url,params=params, **kwargs)
        elif 'post' in method:
            # proxies = {
            #     "https": 'http://10.20.88.49:8081',}
            # response = self.req._common_request("post", session, url, params=params, proxies=proxies, **kwargs)
            response = self.req._common_request("post", session, url, params=params, **kwargs)
        # time.sleep(1000)
        return response

    @keyword
    def waf_get(self, WAF_URL=None, **kwargs):
        """
        Just like `Get On Session`
        V460的Cookie存活机制:每隔5分钟去访问一次任意非静态页面
        """

        alias = self._create_waf_web_session(url=WAF_URL)
        return self._req_on_session(alias, method='get', **kwargs)

    def waf_post(self, WAF_URL=None, **kwargs):
        """
        Just like `Post On Session`
        V460的Cookie存活机制:每隔5分钟去访问一次任意非静态页面
        """
        
        if kwargs.get('t_headers'):
            t_header = kwargs.pop('t_headers')
            alias = self._create_waf_web_session(url=WAF_URL, **t_header)
        else:
            alias = self._create_waf_web_session(url=WAF_URL)
        return self._req_on_session(alias, method='post', **kwargs)

    def _create_waf_web_session(self, url=None, **kwargs):
        url_dict = self._get_url_dict(url)[0]
        rst, alias = self._get_session_alias(url_dict)
        # if rst:
        #     return alias
        
        waf_header = {}
        waf_cookie = self.get_cookie('WAFFSSID')
        waf_header['Host'] = url_dict['host']
        waf_header['Cookie'] = str(waf_cookie.name) + '=' + str(waf_cookie.value)
        waf_header['User-Agent'] = str(self.execute_javascript("return navigator.userAgent;"))
        if kwargs:
            for sub_key in kwargs:
                waf_header[sub_key] = kwargs.get(sub_key)
        
        self.req.create_session(alias, url_dict['url'], headers=waf_header, disable_warnings=1)
        return alias

    def _get_session_alias(self, url_dict):
        alias = self.__session.get(url_dict['url'])
        if alias:
            return True, alias
        alias = 's_' + str(len(self.__session))
        self.__session[url_dict['url']] = alias
        return False, alias

    def _get_url_dict(self, url=None):
        """
        1. url likes: scheme://host[:post][/path]
        2. return dict: {'scheme': xx, 'host': xx, 'post': xx, 'url': xx}
        3. URL 为空，则返回当前的 web_dict, ssh_dict
        4. URL 不为空, 则返回url的 url_dict
        """
        if not url:
            web_dict = url_parse(self.get_location())
            ssh_url = str('ssh://' + web_dict['host'] + ':22')
            ssh_dict = url_parse(ssh_url)
            return web_dict, ssh_dict
        else:
            url_dict = url_parse(url)
            return url_dict

    @keyword
    def open_new_browser(self, browser='chrome', options=None, **kwargs):
        if browser == 'chrome':
            options = get_chrome_options()
        
        return self.open_browser(browser=browser, options=options, **kwargs)

    @keyword
    def open_url(self, *args):
        return self.go_to(*args)

    @keyword
    def operate_element(self, element, *args, **kwargs):
        el_type = element.get('type')
        if el_type == 'input':
            self._handle_input(element, *args, **kwargs)
        elif el_type == 'click':
            self._handle_click(element, **kwargs)
        elif el_type == 'alert':
            self._handle_alert(element, *args, **kwargs)
        elif el_type == 'select':
            self._handle_select(element, *args, **kwargs)
        elif el_type == 'get':
            el = self._handle_get(element, *args, **kwargs)
            return el
        else:
            pass

    def _handle_get(self, element, *args, **kwargs):
        el_locator = element.get('locator')
        try:
            el = self.find_element(el_locator)
        except Exception:
            return False
        return el

    def _handle_select(self, element, *args, **kwargs):
        el_locator = element.get('locator')
        
        self.wait_until_element_is_visible(el_locator)
        self.select_from_list_by_label(el_locator, *args)

    def _handle_input(self, element, *args, **kwargs):
        el_locator = element.get('locator')
        
        # self.wait_until_element_is_visible(el_locator)
        self.input_text(el_locator, *args, **kwargs)

    def _handle_click(self, element, **kwargs):
        el_locator = element.get('locator')
        el_sleep = element.get('sleep')
        
        self.wait_until_element_is_visible(el_locator)
        self.click_element(el_locator, **kwargs)
        
        time_wait(el_sleep)

    def _handle_alert(self, element, **kwargs):      
        el_action = element.get('action')
        el_check = element.get('check')
        el_sleep = element.get('sleep')
        
        msg = self.handle_alert(el_action, timeout=el_sleep, **kwargs)
        
        check_msg(el_check, msg)
        # time_wait(el_sleep)

    def handle_locator(self, locator, value):
        cp_locator = copy.deepcopy(locator)
        # el_dic = cp_locator.get(key)
        cp_locator['locator'] = cp_locator['locator'] % value
        # cp_locator[key] = el_dic
        return cp_locator

def main():
    WafWebDriver()
    time_wait(3)
  
  
if __name__ == "__main__":
    main()
