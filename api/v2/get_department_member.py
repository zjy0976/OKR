from base.BaseApi import BaseApi


class GetDepartmentMember:

    def __init__(self, meember_id=None):
        self.member_id = meember_id

    def get_department_member(self):
        path = '/get_department_member?department_id=0&page=1&token=0aa4e9ccf58e8f577fabdd7a8f348bd50295d486&is_wx_check=false'

        res = BaseApi().base_request_get(path)
        return res

    def get_member_id(self):
        self.member_id = self.get_department_member().json()['data']['data'][1]['member_id']
        return self.member_id
