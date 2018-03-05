# -*- coding: utf-8 -*-

import json
import scrapy
from nga.items import NgaItem
from nga.utils import Util
import time

last24htime = 0

class NgaSpider(scrapy.Spider):
    name = "nga"
    allowed_domains = ["bbs.ngacn.cc"]
    postdate = None


    def start_requests(self):
        url = "http://bbs.ngacn.cc/thread.php?&lite=js"
        cookies = {
            'ngaPassportCid':"Z8is8l0tipk613c99ockr5a1iqvgm718a9410q0j",
            'ngaPassportUid':"14156059",
        }
        yield scrapy.FormRequest(url,cookies=cookies,callback=self.parse)


    def parse(self, response):
        for endpage in xrange(2000):
            url = 'http://bbs.ngacn.cc/thread.php?&lite=js' + '&page=%s' % endpage
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            endpage += 1


    def parse_dir_contents(self, response):
        item = NgaItem()
        util = Util()
        jdict = util.from_js(response.body)
        for i in xrange(35):
            if str(i) in jdict['data']['__T']:
                jdata = jdict['data']['__T'][str(i)]
                postdate = jdata['postdate']
                if int(postdate) > last24htime:
                    item['posttitle'] = jdata['subject']
                    item['postnum'] = jdata['replies']
                    item['posttime'] = jdata['postdate']
                    if 'parent' in jdata:
                        item['postarea'] = jdata['parent']['2']
                        yield item




