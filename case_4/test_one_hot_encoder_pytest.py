from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize('not_incoded, incoded',
                         [
                            (
                                ['Moscow', 'New York', 'Moscow', 'London'],
                                [
                                    ('Moscow', [0, 0, 1]),
                                    ('New York', [0, 1, 0]),
                                    ('Moscow', [0, 0, 1]),
                                    ('London', [1, 0, 0]),
                                ]
                            ),
                            (
                                ['Moscow', 'New York', 'Moscow'],
                                [
                                    ('Moscow', [0, 1]),
                                    ('New York', [1, 0]),
                                    ('Moscow', [0, 1])
                                ]
                            ),
                            (
                                ['0', '0', '7'],
                                [('0', [0, 1]), ('0', [0, 1]), ('7', [1, 0])]
                            )
                         ]
                         )
def test_equal(not_incoded, incoded):
    assert fit_transform(not_incoded) == incoded


def test_type():
    with pytest.raises(TypeError):
        fit_transform(5)
