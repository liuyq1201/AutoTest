import json
import re

a = {
    "userInfo": {
        "registered_enterprise": {
            "is_registered": False,
            "mobile": 15174536401,
            "enterpriseName": "新企业测试",
            "managerFullName": "管理员",
            "managerEmail": "liuyaqing@fxiaoke.com",
            "licence": {
                "productVersion": "enterprise_edition",
                "startTime": 1607746332000,
                "expiredTime": 4077404340000
            },
            "addQuota": {
                "quota": 100,
                "gmtBegin": "2020-10-13 00:00:00",
                "gmtEnd": "2099-10-13 00:00:00",
                "url": "http://172.31.100.247:12832/open/manage/test/addquota/"
            },
            "password": "",
            "prefabricate": False
        },
        "enterpriseAccount": {
            "ei": "85735",
            "ea": "85735",
            "account": "15636707586",
            "password": "1234qwer"
        },
        "environment": "firstshare",
        "type": "default"
    },
    "enterpriseResource": [
    ],
    "systemResource": [
        {
            "customObjectPacks": {
                "param": {
                    "name": "一级部门",
                    "data_own_department": [
                        "999998"
                    ],
                    "parent_id": [
                        "999999"
                    ]
                },
                "config": {
                    "execute_count": 1
                }
            }
        },
        {
            "departmentPacks": {
                "param": {
                    "name": "一级部门",
                    "data_own_department": [
                        "999998"
                    ],
                    "parent_id": [
                        "999999"
                    ]
                },
                "config": {
                    "execute_count": 1
                }
            }
        }
    ],
    "customResource": []
}

# print(len(a['systemResource']))
# for i in range(len(a['systemResource'])):
#     for j in a['systemResource'][i]:
#         print(j)


# a = 'LoginId=LOGIN_ID_20cd1c8a-6e4e-440f-9196-db580ec3d409; Domain=.ceshi112.com; Path=/; Secure; HttpOnly; SameSite=None'
#
# print(a.split(";")[0])
'''
 url = URL[request.data['environment']]
        if request.data['registered_enterprise']['is_registered']:
            mobile = request.data['registered_enterprise']["mobile"]
            enterpriseName = request.data['registered_enterprise']['enterpriseName']
            managerFullName = request.data['registered_enterprise']['managerFullName']
            email = request.data['registered_enterprise']['managerEmail']
            res = self.enterprise.create_enterprise(mobile, enterpriseName, managerFullName, email)
            ei = res["enterpriseId"]
            logger.info(ei)
            res1 = self.enterprise.create_license(ei,
                                                  request.data['registered_enterprise']['licence']['productVersion'])
            res2 = self.enterprise.addquota(ei, request.data['registered_enterprise']['addQuota']['quota'])

        else:
            ei = request.data['tenantId']['ei']
            account = request.data['tenantId']['account']
            res_login = self.enterprise.login(ei, account)
            cookie = res_login[0]
            token = res_login[1]

            param = self.datautil.departmentObject(request.data)
            self.sysObject.createDepartmentObject(url, cookie, token, param, param['execute_count'])
            # self.sysObject.createWebLayoutAndCreateDescribe(url, cookie, token,)
'''

# par = {'userInfo': {'registered_enterprise': {'mobile': 15174536401, 'enterpriseName': '新企业测试', 'managerFullName': '管理员', 'managerEmail': 'liuyaqing@fxiaoke.com', 'password': '1234qwer', 'prefabricate': False, 'licence': {'productVersion': 'enterprise_edition', 'startTime': 1607746332000, 'expiredTime': 4077404340000}, 'addQuota': {'quota': 200, 'gmtBegin': '2020-10-13 00:00:00', 'gmtEnd': '2099-10-13 00:00:00', 'url': 'http://172.31.100.247:12832/open/manage/test/addquota/'}}, 'enterpriseAccount': {'ei': '85811', 'ea': '', 'account': '', 'password': '1234qwer'}, 'environment': 'firstshare',
#                     'type': 'record_8ubb7__c'}, 'enterpriseResource': {'crm': {}, 'resource': [{'code': 'custom_button', 'mastercode': 'custom_button_limit', 'num': '5'}], 'app': [], 'emp': []}, 'customResource': [], 'systemResource': []}
#
# str = json.dumps(par).replace("{", '[').replace("}", ']')
# print(str)
# !/usr/bin/python3
# -*- coding:utf-8 -*-
#
# import random
# import string
#
#
# def create_string_number(n):
#     """生成一串指定位数的字符+数组混合的字符串"""
#     m = random.randint(1, n-3)
#     a = "".join([str(random.randint(0, 9)) for _ in range(m)])
#     print(a)
#     b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
#     return ''.join(random.sample(list(a + b), n))
#
# print(create_string_number(5))
# c='[\\"object_data\\":[\\"object_describe_api_name\\":\\"AccountObj\\",\\"record_type\\":\\"default__c\\",\\"created_by\\":[\\"1000\\"],\\"owner\\":[\\"1000\\"],\\"data_own_department\\":[\\"1000\\"],\\"data_own_department__r\\":\\"1级\\",\\"biz_reg_name\\":false,\\"biz_status\\":\\"allocated\\",\\"is_remind_recycling\\":false,\\"account_status\\":\\"3\\",\\"From\\":2,\\"IsDuplicateSearch\\":true,\\"object_describe_id\\":\\"6359ecf92694b000017cba96\\",\\"name\\":\\"工具创44建数1据\\",\\"account_level\\":\\"\\",\\"parent_account_id\\":null,\\"account_source\\":\\"\\",\\"industry_level1\\":\\"\\",\\"industry_level2\\":\\"\\",\\"tel\\":\\"\\",\\"email\\":\\"\\",\\"fax\\":\\"\\",\\"url\\":\\"\\",\\"remark\\":\\"\\",\\"out_owner\\":[],\\"field_YXMPn__c\\":\\"\\",\\"location\\":\\"\\",\\"country\\":\\"\\",\\"province\\":\\"\\",\\"city\\":\\"\\",\\"district\\":\\"\\",\\"address\\":\\"\\",\\"industry_ext\\":\\"[]\\",\\"requestId\\":\\"db3c06a135d6489886f0bc99e492cfb8\\"]]'
# d = c.replace("[", '{').replace("]", '}').replace("\\", "").replace('false', 'False').replace('true','True')
# print(d)
# print(json.loads(d))

# s = json.dumps(c).replace("[", '{').replace("]", '}').replace("\\", "")
# print(json.loads(s))
# print("参数是{}".format(json.loads(s)))
# a={'userInfo': {'registered_enterprise': {'mobile': 15174536401, 'enterpriseName': '新企业测试', 'managerFullName': '管理员', 'managerEmail': 'liuyaqing@fxiaoke.com', 'password': '1234qwer', 'prefabricate': False, 'licence': {'productVersion': 'enterprise_edition', 'startTime': 1607746332000, 'expiredTime': 4077404340000}, 'addQuota': {'quota': 200, 'gmtBegin': '2020-10-13 00:00:00', 'gmtEnd': '2099-10-13 00:00:00', 'url': 'http://172.31.100.247:12832/open/manage/test/addquota/'}}, 'enterpriseAccount': {'ei': '85811', 'ea': '', 'account': 'a1', 'password': '1234qwer'}, 'environment': 'firstshare', 'type': 'record_y969X__c'}, 'enterpriseResource': {'crm': [{'option1': '100', 'option2': '100'}], 'resource': [{'code': 'custom_object', 'mastercode': 'custom_objects_limit', 'num': '5'}], 'app': [], 'emp': [{'$ref': '$.enterpriseResource.crm[0]'}]}, 'customResource': [], 'systemResource': [{'batch_delete_data': {'param': 'AccountObj', 'config': 'a'}}, {'customObject': {'param': 'object_g4454h__c', 'config': 'b'}}]}
#
# a=str(1234)
# print(type(a))
#
# b=json.dumps(a).replace("{", '[').replace("}", ']')
#
# print(b)
#
# s='wechat_standardpro_upgrade_strengthen_edition'
# if '_upgrade_' in s:
#
#     print(s.index('_upgrade_'))
#     print(s[s.index('_upgrade_')+9:])
#
#   def get_del_version(self, ei, n):
#         ''' n表示要求的数的阶乘 '''
#         if n == 1:
#             return n
#         n = get_del_version(self, ei, n)
#         return n

# a='ssss'
# print(str(a)+'_app')
# search_query_info = {"limit": 20, "offset": 0, "filters": [{"field_name": "display_name", "field_values": ["fs-bpm-after-action"], "operator": "EQ", "filterGroup": "1"}, {"field_name": "display_name", "field_values": ["fs-bpm-after-action"], "operator": "EQ"}], "orders": [{"fieldName": "create_time", "isAsc": False}]}
# print(json.dumps(search_query_info))
import time
# a= 'sid=Fe26.2**745647f990dc5cd950fb035b3aaa569e190dcba0d6ae90b4ff515aa6df515154*uYL40PX7t9xRVb7hH_-Czg*p26WADCL0yHnBt2-BFZwZ8ylIY-jGOrU_0_NX2dcoEYeHR-S-GA_zgQIDYgUoboF1XeUgvEf8199FPex52_vfPZX-M8g9cVd7Lg7vly_Bi3DJSMOTAMqBUUZsytRJ2zLRJnxZMvYAHDqhPNs6Wy9GkcntXFWiKRiwFV2EZ-Hjh35fUdOYT_vLdnolZ4S_9GNOHjisggDTkcloIo4S3L9IjkwJT2aUl87VuKklNWxJO8rlFl_8cFxDPHDGM1ZJUz0**547c018af34047b2b1193c764977f16cdf6d2eec3e459850ccb6d1cf72d5da66*8zBTy_TitQVGGF2GflejqbxopFPK2ZIvEMMPOPMYcn4; HttpOnly; Path=/kibana01'
# print(a.split(";")[0])
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# fifteen_minutes_ago = (datetime.datetime.now() - datetime.timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")


timeStamp1 = int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")) * 1000)
# print(current_time)
print(timeStamp1)

s = list('20230624')
s.insert(4, '-')
s.insert(7, '-')
print("".join(s))
# timeStamp = int(time.mktime(time.strptime('2023-05-27', "%Y-%m-%d"))*1000)
# print(timeStamp)
# time_array = time.strptime(, "%Y-%m-%d %H:%M:%S")
# time_stamp = int(round(time.mktime(time_array)) * 1000)
# print(fifteen_minutes_ago)
# print(current_time)

# from flask import Flask, jsonify, request, Response
# app = Flask(__name__)
# import flask
# # 指定接口访问的路径（set_response是API名称），支持什么请求方式get，post
# @app.route('/set_response', methods=['post'])
# def set_response():
#
#     params = flask.request.json
#     print(params)
#     return {'code': 200, 'message': 'file  exist'}
# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port = 19996
#     app.run(ip, port, debug=True)


# s='5ms jdbc-support.prepareUpdateBatch(DELETE FROM sch_88135.dt_auth_out_simple WHERE tenant_id=? AND object_describe_api_name=? AND auth_target=? AND auth_code=? AND scene=?) db-paas-bi-copier:10.112.52.251:5432/sch_bi_112 Batch entry 0 DELETE FROM sch_88135.dt_auth_out_simple WHERE tenant_id="88135" AND object_describe_api_name=NULL AND auth_target="88135.-10000" AND auth_code=NULL AND scene=NULL was aborted: ERROR: operator does not exist: smallint = character varyingHint: No operator matches the given name and argument types. You might need to add explicit type casts.Position: 138  Call getNextException to see other errors in the batch.'
# print(str(s)[1:40])
a = {
    "testEnvSafe": {
        "sent": ["刘亚庆"],
        "unsent": ["阿萨德撒", "刘亚庆", "撒大", "阿萨德撒"],
        "targetSessionId": "34cbf428e722477a993be307423c3b4b",
        "content": "您是本周群维护管理员，辛苦你跟进处理相关问题"}
}

# print(a['testEnvSafe'])
#
# s = [1, 2, 3, 5, 54, 9]
#
# a = len(s) * 0.15 + 2
# print(a)
# s = "{\"type\":\"select_one\",\"define_type\":\"custom\",\"api_name\":\"field_T2n1R__c\",\"label\":\"单选\",\"help_text\":\"\",\"is_required\":false,\"is_unique\":false,\"is_active\":true,\"is_index\":true,\"status\":\"new\",\"default_value\":\"\",\"options\":[{\"label\":\"示例选项\",\"value\":\"option1\"},{\"label\":\"其他\",\"value\":\"other\",\"not_usable\":true}]}"
# print(json.dumps(json.dumps(json.loads(s))))
#
# print("作废" not in 'PaaS-流程引擎-作废')
#
# a = '流程接口自动化--历史线上bug相关'
# print(a.split('--')[0])

a = ['@liu', '@hhh']
print(a[0].startswith('@'))
b = [x for x in a if x.startswith('@')]
print(b[0][1:])

s = '90.222%'
s1 = '89.12%'
print(float(s.replace('%', '')) > float(s1.replace('%', '')))
l = "测试哈哈哈"
l1 = "测试"
print(l.find(l1)==0)
