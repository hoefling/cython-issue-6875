from eggs import eggs

def test_eggs():
    with eggs() as result:
        assert result == 42
