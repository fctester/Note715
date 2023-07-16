import unittest
import requests
import time
from api_unittest.common.check_common import CheckCommon
from parameterized import parameterized  # 参数化的库
from api_unittest.common.read_yml import ReadYaml


class NotesvrSetNoteGroupLevel1(unittest.TestCase):
    checkCommon = CheckCommon()
    rY = ReadYaml()
    api_data = rY.api_yaml('note_groups/notesvrSetNotegroup')
    check_Required = api_data['check_Required']
    # # env_date = rY.env_yaml()
    # # host = env_date['host']
    host = 'http://note-api.wps.cn'
    path = '/v3/notesvr/set/notegroup'
    url = host + path
    userid = 993271150
    sid = 'V02SlGYQqEeHqyv-gvOnGjrcjx7bLTI00af3a71a003b341d6e'

    # userid = env_date['user_id']
    # sid = env_date['sid']

    def test01_major(self):
        """创建便签分组主流程，校验点：①协议规范(状态码、返回体keys)②接口返回③数据存储"""

        headers = {
            'Content-Type': 'application/json',
            'X-User-Key': f'{str(self.userid)}',
            'Cookie': f'wps_sid={self.sid}'
        }
        # 新建分组
        create_time = str(int(time.time() * 1000))
        group_id = create_time + 'testGroup'
        group_name = create_time + 'groupName'
        body = {
            'groupId': group_id,
            'groupName': group_name
        }
        res = requests.post(url=self.url, headers=headers, json=body)  # requests库支持请求方式直接写到方法属性中
        print(res.status_code)
        print(res.text)
        self.assertTrue(res.status_code == 200, msg='状态码错误')  # 校验状态码
        response = res.json()
        check_items = {'responseTime': 1, 'updateTime': 1}
        self.assertEqual(len(check_items), len(response.keys()))  # 校验返回body中对象数量
        self.checkCommon.check_response(check_items, response)  # 调用common中封装的校验返回体长度、值类型的方法

        # 查询便签分组
        get_group_path = '/v3/notesvr/get/notegroup'
        get_group_url = self.host + get_group_path
        get_group_body = {
            'excludeInvalid': 'Ture'
        }
        get_groups_res = requests.post(url=get_group_url, headers=headers, json=get_group_body)
        # print(get_groups_res.text)
        lst_group = []
        for i in get_groups_res.json()['noteGroups']:  # 循环取返回体中分组的id信息，写入到列表中
            lst_group_id = i['groupId']
            lst_group.append(lst_group_id)
            if lst_group_id == group_id:
                self.assertEqual(group_name, i['groupName'])
        self.assertIn(group_id, lst_group)

    @parameterized.expand(check_Required)
    def test02_input_check(self, dic):
        """必填项（Required）校验"""
        headers = {
            'Content-Type': 'application/json',
            'X-User-Key': f'{str(self.userid)}',
            'Cookie': f'wps_sid={self.sid}'
        }
        # 新建分组
        create_time = str(int(time.time() * 1000))
        group_id = create_time + 'testGroup'
        group_name = create_time + 'groupName'
        body = {
            'groupId': group_id,
            'groupName': group_name
        }
        body.pop(dic['key'])
        res = requests.post(url=self.url, headers=headers, json=body)
        self.assertEqual(dic['res_code'], res.status_code, msg='状态码错误')  # 校验状态码
        self.assertEqual('参数不合法！', res.json()['errorMsg'], msg='Msg错误')  # 校验errorMsg
