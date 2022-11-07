#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_search.py
@Time    :   2022/11/07 23:54:54
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.search import SearchAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = SearchAPI(api_key=api_key)

    def test_search(self) -> None:
        response = self.api.search()

        self.assertEqual(response["status_code"], 200)
