import pytest


@pytest.fixture
def data_websites():
    data = [
        'www.google.com.ua',
        'www.ukr.net',
        'www.ithillel.ua'
    ]
    return data


# @pytest.fixture
# def data_websites():
#     data = [
#         'fake && ls bubu',
#         'tfp.ukr.net',
#         'wdn.ithillel.ua'
#     ]
#     return data
