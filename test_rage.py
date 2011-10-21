def test_error():
    assert False

def pytest_generate_tests(metafunc):
    for i in range(10):
        metafunc.addcall()