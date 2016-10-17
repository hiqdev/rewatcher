import Rewatcher

def test_colored():
    str = 'test string'
    assert str == Rewatcher.colored(str, 'yellow', False)
    assert '\033[93m' + str + '\033[0m' == Rewatcher.colored(str, 'yellow', True)
