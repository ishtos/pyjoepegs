#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_users.py
@Time    :   2022/11/07 23:55:04
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.users import UsersAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = UsersAPI(api_key=api_key)

    # @unittest.skip("TODO: 422 Unprocessable Entity")
    def test_get_user_by_name(self) -> None:
        name = "ishtos"
        response = self.api.get_user_by_name(name)

        self.assertIsInstance(response, dict)

    def test_get_user(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user(address)

        self.assertIsInstance(response, dict)

    def test_get_user_collections(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user_collections(address)

        self.assertIsInstance(response, list)

    def test_get_user_items(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user_items(address)

        self.assertIsInstance(response, list)

    def test_get_user_items_on_auction(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user_items_on_auction(address)

        self.assertIsInstance(response, list)

    def test_get_user_bids_received(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user_bids_received(address)

        self.assertIsInstance(response, list)

    def test_get_user_activity(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_user_activity(address)

        self.assertIsInstance(response, list)
