#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `acqpack` package."""

import pytest

from acqpack import Motor, AsiController, Autosampler, FractionCollector, Manifold
from acqpack import utils as ut
from acqpack import gui

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
