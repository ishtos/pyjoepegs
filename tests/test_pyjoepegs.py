#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_pyjoepegs.py
@Time    :   2022/11/07 23:42:19
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.activities import ActivitiesAPI
from pyjoepegs.collections import CollectionsAPI
from pyjoepegs.items import ItemsAPI
from pyjoepegs.maker_orders import MakerOrdersAPI
from pyjoepegs.owners import OwnersAPI
from pyjoepegs.pyjoepegs import JoepegsAPI
from pyjoepegs.sales import SalesAPI
from pyjoepegs.search import SearchAPI
from pyjoepegs.users import UsersAPI


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = JoepegsAPI(api_key=api_key)

    def test_activities(self) -> None:
        self.assertIsInstance(self.api.activities(), ActivitiesAPI)

    def test_collections(self) -> None:
        self.assertIsInstance(self.api.collections(), CollectionsAPI)

    def test_items(self) -> None:
        self.assertIsInstance(self.api.items(), ItemsAPI)

    def test_maker_orders(self) -> None:
        self.assertIsInstance(self.api.maker_orders(), MakerOrdersAPI)

    def test_owners(self) -> None:
        self.assertIsInstance(self.api.owners(), OwnersAPI)

    def test_sales(self) -> None:
        self.assertIsInstance(self.api.sales(), SalesAPI)

    def test_search(self) -> None:
        self.assertIsInstance(self.api.search(), SearchAPI)

    def test_users(self) -> None:
        self.assertIsInstance(self.api.users(), UsersAPI)
