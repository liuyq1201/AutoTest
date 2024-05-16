import json
import requests
import re
from deepdiff import DeepDiff
j2 = {
    "workflow": {
        "cancelable": True,
        "remindLatency": 0,
        "modifier": "1004",
        "description": "",
        "type": "approvalflow",
        "transitions": [
            {
                "toId": "1616381799812",
                "serialNumber": 0,
                "id": "1508311088516248",
                "fromId": "start"
            },
            {
                "toId": "1616381799813",
                "serialNumber": 0,
                "id": "1616381799814",
                "fromId": "1616381799812"
            },
            {
                "toId": "end",
                "condition": {
                    "left": {
                        "expression": "action"
                    },
                    "right": {
                        "type": {
                            "name": "text"
                        },
                        "value": "reject"
                    },
                    "type": "equals"
                },
                "serialNumber": 0,
                "id": "1616381799815",
                "fromId": "1616381799813"
            },
            {
                "toId": "end",
                "condition": {
                    "left": {
                        "expression": "action"
                    },
                    "right": {
                        "type": {
                            "name": "text"
                        },
                        "value": "agree"
                    },
                    "type": "equals"
                },
                "serialNumber": 0,
                "id": "1616381799816",
                "fromId": "1616381799813"
            }
        ],
        "remind": False,
        "sourceWorkflowId": "apprX98QYPVEBQ__crmappr",
        "modifyTime": 1678038765850,
        "enable": True,
        "appId": "CRM",
        "linkAppEnable": False,
        "id": "6404d6edc2f597120bf7de36",
        "creator": "1004",
        "variables": [
            {
                "id": "action",
                "type": {
                    "name": "text"
                }
            }
        ],
        "isAutoAgree": 0,
        "remindWhenInstanceComplete": True,
        "entityId": "object_L0b8l__c",
        "history": False,
        "priority": 0,
        "triggerTypes": [
            "1"
        ],
        "applicantConfig": [
            "submitter"
        ],
        "createTime": 1617010771412,
        "activities": [
            {
                "execution": {
                    "pass": []
                },
                "id": "start",
                "type": "startEvent"
            },
            {
                "execution": {
                    "pass": []
                },
                "id": "end",
                "type": "endEvent"
            },
            {
                "execution": {
                    "pass": []
                },
                "taskType": "single",
                "enableMoveToCurrentActivityWhenReject": True,
                "linkAppEnable": False,
                "name": "单人审批A1",
                "candidateEditable": False,
                "id": "1616381799812",
                "assignee": {
                    "applicant": [
                        "applicant"
                    ]
                },
                "type": "userTask"
            },
            {
                "execution": {
                    "pass": []
                },
                "gatewayType": 0,
                "id": "1616381799813",
                "type": "exclusiveGateway"
            }
        ],
        "name": "勿动-驳回重新发起-定义改变1678038762700",
        "tenantId": "590118",
        "remindWhenTaskComplete": True,
        "allowRetrieve": True
    },
    "workflowRule": {
        "conditionsDisable": 0,
        "conditionPattern": "(0)",
        "workflowSrcId": "apprX98QYPVEBQ__crmappr",
        "entityId": "object_L0b8l__c",
        "ruleId": "6404d6edc2f597120bf7de37",
        "triggerTypes": [
            "1"
        ],
        "conditions": [
            {
                "rowNo": 0,
                "leftSide": {
                    "fieldName": "field_mC153__c",
                    "fieldSrc": "object_L0b8l__c",
                    "fieldType": "string"
                },
                "rightSide": {
                    "metadata": {
                        "containSubDept": False
                    },
                    "value": "驳回测试-定义改变"
                },
                "executeResult": False,
                "operator": "equals"
            }
        ]
    },
    "execution": {},
    "triggerNames": [
        "新建"
    ]
}


def login_fs():
    url = 'https://www.fxiaoke.com/FHH/EM0HUL/Authorize/EnterpriseAccountLogin'
    data = {
        "enterpriseAccount": "fktest143",
        "userAccount": "lyq",
        "rsaPassword": "UU7wkgHPW8+z/P66UvFcV3cgKRuTlCrKlWl79aAK5caTOf6dWJpiSuhhesceXtzbnQ2BYVb+2VxbyP+6QfFsa7K+m7UfJ+G/+7Olf1i0tGjwNomJ+znZra10+D5rQRi8WVwZQKTQw4deskhtKOCDrKQYaTMHENelrWlWDu73tIA=",
        "persistenceHint": True,
        "publickKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB",
        "deviceId": "08064f5a881fc36fa17b7f7fe8ae4983"
    }

    headers = {
        "content-type": "application/json",
        "accept-language": "zh-CN,zh-TW;0.9,en;0.8",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "content-length": "61",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }

    r = requests.request("POST", url, json=data, headers=headers)
    if (r.status_code == 200):
        set_cookie = r.headers["Set-Cookie"]
        print(set_cookie)
        fs_token = get_cookie(set_cookie, "fs_token")
        FSAuthX = get_cookie(set_cookie, "FSAuthX")
        FSAuthXC = get_cookie(set_cookie, "FSAuthXC")
        cookie = "FSAuthX=" + FSAuthX + ";FSAuthXC=" + FSAuthXC;
        return fs_token, cookie,


def get_cookie(content, key):
    pattern = re.compile(r'(' + key + '=)' + '([^;]{1,});')
    return pattern.search(content).group(2)  # group 是获取正则表达式中第几个分组，（）为一个分组，分组0默认值是match中的内容


def approval_definition(fs_token, cookie, ):
    '''
    创建对象
    '''

    desc_data = {"workflowId": "64021360c2f597120bf7c697"}
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept-Language": "application/json",
        "cookie": cookie
    }
    url = 'https://www.fxiaoke.com/FHH/EM1AAPPROVAL/Definition/Detail?' + fs_token
    res = requests.request("POST", url, json=desc_data, headers=headers)
    print("查询定义成功" + res.text)

    return json.loads(res.text)


def json_key_value_exist(json1, json2):
    """判断第一个 JSON 数据中的所有 key 和对应的值是否都出现在第二个 JSON 数据中"""

    return DeepDiff(json1, json2)


if __name__ == '__main__':
    j = {
  "Result": {
    "FailureCode": 0,
    "StatusCode": 0,
    "UserInfo": {
      "EmployeeID": 1004,
      "EnterpriseAccount": "fktest143"
    }
  },
  "Value": {
    "workflow": {
      "cancelable": False,
      "remindLatency": 0,
      "modifier": "1004",
      "description": "",
      "type": "approvalflow",
      "transitions": [
        {
          "toId": "1656944845812",
          "serialNumber": 0,
          "id": "1508311088516248",
          "fromId": "start"
        },
        {
          "toId": "1656944845813",
          "serialNumber": 0,
          "id": "1656944845814",
          "fromId": "1656944845812"
        },
        {
          "toId": "end",
          "condition": {
            "left": {
              "expression": "action"
            },
            "right": {
              "type": {
                "name": "text"
              },
              "value": "reject"
            },
            "type": "equals"
          },
          "serialNumber": 0,
          "id": "1656944845815",
          "fromId": "1656944845813"
        },
        {
          "toId": "1677569450283",
          "condition": {
            "left": {
              "expression": "action"
            },
            "right": {
              "type": {
                "name": "text"
              },
              "value": "agree"
            },
            "type": "equals"
          },
          "serialNumber": 0,
          "id": "1656944845816",
          "fromId": "1656944845813"
        },
        {
          "toId": "1677569450284",
          "serialNumber": 0,
          "id": "1677569450285",
          "fromId": "1677569450283"
        },
        {
          "toId": "end",
          "condition": {
            "left": {
              "expression": "action"
            },
            "right": {
              "type": {
                "name": "text"
              },
              "value": "reject"
            },
            "type": "equals"
          },
          "serialNumber": 0,
          "id": "1677569450286",
          "fromId": "1677569450284"
        },
        {
          "toId": "end",
          "condition": {
            "left": {
              "expression": "action"
            },
            "right": {
              "type": {
                "name": "text"
              },
              "value": "agree"
            },
            "type": "equals"
          },
          "serialNumber": 0,
          "id": "1677569450287",
          "fromId": "1677569450284"
        },
        {
          "toId": "1656944845812",
          "condition": {
            "left": {
              "expression": "action"
            },
            "right": {
              "type": {
                "name": "text"
              },
              "value": "go_back"
            },
            "type": "equals"
          },
          "serialNumber": 0,
          "id": "1677857608997",
          "fromId": "1677569450284"
        }
      ],
      "remind": False,
      "sourceWorkflowId": "apprQ2C7GNW4KX__crmappr",
      "modifyTime": 1677857632638,
      "enable": True,
      "appId": "CRM",
      "linkAppEnable": False,
      "id": "64021360c2f597120bf7c697",
      "creator": "1004",
      "variables": [
        {
          "id": "action",
          "type": {
            "name": "text"
          }
        }
      ],
      "isAutoAgree": 0,
      "dataLockType": 0,
      "remindWhenInstanceComplete": False,
      "entityId": "object_1nUAW__c",
      "history": False,
      "priority": 2,
      "triggerTypes": [
        "1",
        "2"
      ],
      "applicantConfig": [
        "owner"
      ],
      "submitterCancelable": False,
      "createTime": 1677554663128,
      "activities": [
        {
          "execution": {
            "pass": [],
            "reject": []
          },
          "id": "start",
          "type": "startEvent"
        },
        {
          "execution": {
            "pass": [],
            "reject": []
          },
          "id": "end",
          "type": "endEvent"
        },
        {
          "execution": {
            "pass": []
          },
          "extension": {
            "layoutType": "objectFlowLayout",
            "layoutApiName": "layout_4o2qg__c",
            "layoutName": "哈哈哈哈哈阿斯顿"
          },
          "taskType": "one_pass",
          "enableMoveToCurrentActivityWhenReject": True,
          "linkAppEnable": False,
          "name": "单人审批1",
          "id": "1656944845812",
          "assignee": {
            "applicant": [
              "applicant"
            ]
          },
          "assigneeType": "assignee",
          "type": "userTask"
        },
        {
          "execution": {
            "pass": [],
            "reject": []
          },
          "gatewayType": 0,
          "id": "1656944845813",
          "type": "exclusiveGateway"
        },
        {
          "execution": {
            "pass": []
          },
          "extension": {
            "defaultButtons": []
          },
          "taskType": "single",
          "enableMoveToCurrentActivityWhenReject": True,
          "linkAppEnable": False,
          "name": "单人审批2",
          "candidateEditable": False,
          "id": "1677569450283",
          "assignee": {
            "applicant": [
              "applicant"
            ]
          },
          "assigneeType": "assignee",
          "type": "userTask"
        },
        {
          "execution": {
            "pass": []
          },
          "gatewayType": 0,
          "id": "1677569450284",
          "type": "exclusiveGateway"
        }
      ],
      "name": "非勿动-主从审批测试副本副本",
      "tenantId": "590118",
      "remindWhenTaskComplete": False,
      "allowRetrieve": True
    },
    "workflowRule": {
      "conditionsDisable": 1,
      "conditionPattern": "",
      "workflowSrcId": "apprQ2C7GNW4KX__crmappr",
      "entityId": "object_1nUAW__c",
      "ruleId": "64021360c2f597120bf7c698",
      "triggerTypes": [
        "1",
        "2"
      ]
    },
    "execution": {
      "pass": [
        {
          "taskType": "send_qixin",
          "recipients": {
            "applicant": [
              "applicant"
            ]
          },
          "title": "审批已通过",
          "content": "啊啊啊啊啊啊手动"
        }
      ]
    },
    "triggerNames": [
      "新建",
      "编辑"
    ]
  }
}

    cookie = login_fs()
    res = approval_definition(cookie[0], cookie[1])
    e = json_key_value_exist(j, res)
    print(e)
