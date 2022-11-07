#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_sales.py
@Time    :   2022/11/07 23:54:44
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.sales import SalesAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = SalesAPI(api_key=api_key)

    def test_recent_taker_orders_grouped_by_txn_hash(self) -> None:
        response = self.api.recent_taker_orders_grouped_by_txn_hash()

        self.assertEqual(response["status_code"], 200)
