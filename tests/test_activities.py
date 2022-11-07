#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_activities.py
@Time    :   2022/11/07 23:53:52
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.activities import ActivitiesAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = ActivitiesAPI(api_key=api_key)

    def test_list_activity_by_collection(self) -> None:
        collection_address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.list_activity_by_collection(collection_address)

        self.assertEqual(response["status_code"], 200)

    def test_list_activity_by_item(self) -> None:
        collection_address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        token_id = "0"
        response = self.api.list_activity_by_item(collection_address, token_id)

        self.assertEqual(response["status_code"], 200)
