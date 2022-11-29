#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_collections.py
@Time    :   2022/11/07 23:53:57
@Author  :   ishtos
@License :   (C)Copyright 2022 ishtos
"""

import os
import unittest

import dotenv

from pyjoepegs.collections import CollectionsAPI


class TestActivitiesAPI(unittest.TestCase):
    def setUp(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        dotenv.load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("API_KEY")

        self.api = CollectionsAPI(api_key=api_key)

    def test_list_collections(self) -> None:
        response = self.api.list_collections()

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_get_trending_collections(self) -> None:
        response = self.api.get_trending_collections()

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    @unittest.skip("TODO: check slug")
    def test_get_collection_by_slug(self) -> None:
        slug = ""
        response = self.api.get_collection_by_slug(slug)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_get_collection(self) -> None:
        address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_collection(address)

        self.assertIsInstance(response, dict)

    def test_get_item(self) -> None:
        collection_address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        token_id = "0"
        response = self.api.get_item(collection_address, token_id)

        self.assertIsInstance(response, dict)

    @unittest.skip("TODO: check trait_type")
    def test_get_collection_attribute_values(self) -> None:
        collection_address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        trait_type = ""
        response = self.api.get_collection_attribute_values(collection_address, trait_type)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_get_collection_attributes(self) -> None:
        collection_address = "0xb842344669579ecf4cee12f740520376c4cbc6d1"
        response = self.api.get_collection_attributes(collection_address)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
