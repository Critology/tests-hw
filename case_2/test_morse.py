from morse import decode
import pytest


@pytest.mark.parametrize('string, result',
                         [
                            ('... .- .-.. ..- - .', 'SALUTE'),
                            ('... --- ...', 'SOS'),
                            ('.---- ...-- ...-- --...', '1337')
                         ]
                         )
def test_decode(string, result):
    assert decode(string) == result


