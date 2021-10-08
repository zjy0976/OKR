from api.v2.get_department_member import GetDepartmentMember


def test_get_department_member():
    getDeparmentMeber = GetDepartmentMember()
    res = getDeparmentMeber.get_department_member()
    print(res.text)

