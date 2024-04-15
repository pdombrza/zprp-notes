from encode import from_ascii_codes, to_ascii_codes
from hypothesis import given, example, settings
from hypothesis.strategies import text


@given(text())
@example("")
@settings(max_examples=500)
def test_decode_inverts_encode(test_str: str):
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str