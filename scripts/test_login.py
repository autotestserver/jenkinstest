import allure

def test_one():
    assert 1

@allure.step(title="测试登录流程")
def test_login():
    allure.attach('登录', '输入用户名')
    print('abc') #输入用户名

    allure.attach('登录', '输入密码')
    print('abc')

    allure.attach('登录', '点击登录')
    print('abc')
    assert 1


