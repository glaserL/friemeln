from friemeln.friemeln import get_friemeln


def test_true_is_true():
	assert True

def test_friemeln():
	result = get_friemeln()
	assert result == "FRIEMELN"
