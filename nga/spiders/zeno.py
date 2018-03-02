# -*- coding: utf-8 -*-

import json
import scrapy
from nga.items import NgaItem
from nga.utils import Util
import datetime

class NgaSpider(scrapy.Spider):
    name = "nga"
    allowed_domains = ["bbs.ngacn.cc"]


    def start_requests(self):
        url = "http://bbs.ngacn.cc/thread.php?&lite=js&page=10"
        cookies = {
            'ngaPassportCid':"Z8is8l0tipk613c99ockr5a1iqvgm718a9410q0j",
            'ngaPassportUid':"14156059",
        }
        yield scrapy.FormRequest(url,cookies=cookies,callback=self.parse)


    def parse(self, response):
        item = NgaItem()
        util = Util()
        jdict = util.from_js(response.body)
        for i in xrange(35):
            jdata = jdict['data']['__T'][str(i)]
            item['posttitle'] = jdata['subject']
            item['postnum'] = jdata['replies']
            if len(jdata['parent']['2'])>0:
                item['postarea'] = jdata['parent']['2']
            yield item



