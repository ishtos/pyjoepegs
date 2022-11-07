#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_items.py
@Time    :   2022/11/07 23:54:11
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.items import ItemsAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = ItemsAPI(api_key=api_key)

    def test_list_items(self) -> None:
        response = self.api.list_items()

        self.assertEqual(response["status_code"], 200)
