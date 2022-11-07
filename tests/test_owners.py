#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_owners.py
@Time    :   2022/11/07 23:54:32
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.owners import OwnersAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = OwnersAPI(api_key=api_key)

    @unittest.skip("TODO: 422 Unprocessable Entity")
    def test_list_owners(self) -> None:
        response = self.api.list_owners()

        self.assertEqual(response["status_code"], 200)

    def test_list_collection_owners(self) -> None:
        collection_id = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.list_collection_owners(collection_id)

        self.assertEqual(response["status_code"], 200)
