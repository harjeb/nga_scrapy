# -*- coding: utf-8 -*-

import json

class Util():
    def from_js(self,js_str):  #将nga返回js格式数据转换成json格式
        jsbegin = r'window.script_muti_get_var_store='
        js_str = js_str.strip()
        js_str = js_str.decode("gbk").encode("utf-8")
        if not js_str.startswith(jsbegin):
            raise ValueError('Invalid js')
        return json.loads(js_str[len(jsbegin):],encoding="utf-8")