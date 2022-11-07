#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_maker_orders.py
@Time    :   2022/11/07 23:54:20
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.maker_orders import MakerOrdersAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = MakerOrdersAPI(api_key=api_key)

    def test_list_maker_orders(self) -> None:
        response = self.api.list_maker_orders()

        self.assertEqual(response["status_code"], 200)

    @unittest.skip("TODO: check order_id")
    def test_get_maker_order(self) -> None:
        order_id = ""
        response = self.api.get_maker_order(order_id)

        self.assertEqual(response["status_code"], 200)
