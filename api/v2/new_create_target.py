from api.v2.get_department_member import GetDepartmentMember
from base.BaseApi import BaseApi


class NewGreatTarget:
    def new_create_target(self):
        member_id = GetDepartmentMember()
        member_id.get_member_id
        path = '/new_create_target'
        data = {
            "target_members": [{
                "user_id": member_id.get_member_id(),
                "type": 1
            }, {
                "user_id": member_id.get_member_id(),
                "type": 2
            }, {
                "user_id": 508,
                "type": 3
            }],
            "name": "写一个接口自动化",
            "start_time": "2021-10-01",
            "template_id": 691, "end_time": "2021-11-31",

            "template_name": "2021年10月",
            "kr_infos": [{
                "name": "发布OKR接口自动化",
                "progress_type": 2,
                "key_result_members": [{
                    "user_id": member_id.get_member_id(),
                    "type": 1
                }, {
                    "user_id": 330,
                    "type": 2
                }]
            }, {
                "name": "封装",
                "key_result_members": [{
                    "user_id": 330,
                    "type": 1
                }, {
                    "user_id": 330,
                    "type": 2
                }]
            }],
            "tag": 1,
            "private_status": False,
            "token": "0aa4e9ccf58e8f577fabdd7a8f348bd50295d486",
            "is_wx_check": False
        }

        res = BaseApi().base_request_post(path, json=data)
        return res
