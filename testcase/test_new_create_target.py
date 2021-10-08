import pytest

from api.v2.new_create_target import NewGreatTarget


def test_new_create_target():
    newCreateTarget = NewGreatTarget()
    res = newCreateTarget.new_create_target()
    print(res.text)


if __name__ == '__main__':
    pytest.test_new_create_target()
