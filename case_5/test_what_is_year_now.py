from unittest.mock import patch
from whats_year_now import what_is_year_now


@patch
def test_what_is_year_now():
    with patch("whats_year_now.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.__enter__.loads.__enter__.decode.return_value = '["myjsondata"]'
        assert what_is_year_now() == "2012-03-05"


"2012-03-05"