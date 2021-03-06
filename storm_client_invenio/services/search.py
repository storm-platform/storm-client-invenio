# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import posixpath

from pydash import py_

from .base import BaseService
from ..models import RecordList
from ..object_factory import ObjectFactory

from typing import Dict
from typeguard import typechecked

from cachetools import cached, LRUCache


@typechecked
class RecordSearchService(BaseService):
    def __init__(self, url: str, user_records: bool = False) -> None:
        self._base_path = "records"
        if user_records:
            self._base_path = posixpath.join("user", self._base_path)

        super(RecordSearchService, self).__init__(url, self._base_path)

    @cached(cache=LRUCache(maxsize=128))
    def query(self, request_options: Dict = {}, **kwargs) -> RecordList:
        operation_result = self._create_request(
            "GET", self.url, params=kwargs, **request_options
        )

        return ObjectFactory.resolve(
            "RecordList", py_.get(operation_result.json(), "hits.hits", {})
        )


__all__ = "RecordSearchService"
