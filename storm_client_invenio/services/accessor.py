# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from .search import RecordSearchService
from .record import RecordService, RecordFilesService


class BaseServiceAccessor:
    def __init__(self, url):
        self._url = url


class RecordAccessor(BaseServiceAccessor):
    def __init__(self, url, **kwargs):
        super(RecordAccessor, self).__init__(url)

    def draft(self):
        return RecordService(self._url, as_draft=True)

    def record(self):
        return RecordService(self._url, as_draft=False)

    def files(self, node_resource):
        return RecordFilesService(self._url, node_resource)

    def search(self, user_records=False):
        return RecordSearchService(self._url, user_records)


__all__ = ("BaseServiceAccessor", "RecordAccessor")
