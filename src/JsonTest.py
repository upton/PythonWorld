#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dd = dict(age=18, x=123, name='upton', b=5, c='xyz',)

s = json.dumps(dd)  

print s
print json.dumps(dd, separators=(',', ':'))  # 去掉，：后面的空格
print json.dumps(dd, indent=2, sort_keys=True)  # 格式美化输出

d = json.loads(s)

print d['name']

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
stu = Student('Bob', 20, 88)

print json.dumps(stu, default=lambda obj: obj.__dict__)

js = r'''{"quotes":[{"symbol":"SH601299","exchange":"SH","code":"601299","name":"中国北车","current":"14.09","percentage":"3.37","change":"0.460","open":"14.25","high":"14.99","low":"13.81","close":"0.0","last_close":"13.63","high52week":"14.99","low52week":"4.17","volume":"6.35752048E8","volumeAverage":"124725423","marketCapital":"1.7274030446927E11","eps":"0.35","pe_ttm":"30.322","pe_lyr":"40.8756","beta":"0.0","totalShares":"12259780303","time":"Wed Jan 21 15:03:04 +0800 2015","afterHours":"0.0","afterHoursPct":"0.0","afterHoursChg":"0.0","afterHoursTime":"Thu Oct 20 09:59:01 CST 2011","updateAt":"1421823823318","dividend":"0.2","yield":"0.0","turnover_rate":"6.28","instOwn":"0.0","rise_stop":"14.99","fall_stop":"12.27","currency_unit":"CNY","amount":"9.198379483E9","net_assets":"3.8665","hasexist":"false","type":"11","flag":"1","rest_day":"","kzz_stock_symbol":"","kzz_stock_name":"","kzz_stock_current":"0.0","kzz_convert_price":"0.0","kzz_covert_value":"0.0","kzz_cpr":"0.0","kzz_putback_price":"0.0","kzz_convert_time":"","kzz_redempt_price":"0.0","kzz_straight_price":"0.0","kzz_stock_percent":"","pb":"3.64","benefit_before_tax":"0.0","benefit_after_tax":"0.0","convert_bond_ratio":"","totalissuescale":"","outstandingamt":"","maturitydate":"","remain_year":"","convertrate":"","interestrtmemo":"","release_date":"","circulation":"0.0","par_value":"0.0","due_time":"0.0","value_date":"","due_date":"","publisher":"","redeem_type":"","issue_type":"1","bond_type":"","warrant":"","sale_rrg":"","rate":"","after_hour_vol":"0","float_shares":"10126084096","float_market_capital":"1.4267652491264E11","disnext_pay_date":"","convert_rate":"","psr":"1.6225"}]}'''

data = json.loads(js)

print data.get('quots')
