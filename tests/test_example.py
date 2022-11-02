from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reveerse_for_empte_string():
    assert reverse('') == ''
