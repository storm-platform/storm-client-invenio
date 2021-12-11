# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from typing import Sequence
from collections import UserList

from .base import RecordBase
from .type import is_draft
from .link import RecordDraftLink, RecordLink


class RecordDraft(RecordBase):
    links_cls = RecordDraftLink


class Record(RecordBase):
    links_cls = RecordLink


#
# Record Collection
#
class RecordList(UserList):
    def __init__(self, data=None):
        if not isinstance(data, Sequence):
            raise ValueError("The `data` argument must be a valid sequence type.")

        data = py_.map(
            data, lambda obj: RecordDraft(obj) if is_draft(obj) else Record(obj)
        )
        super(RecordList, self).__init__(data)


__all__ = ("RecordDraft", "Record", "RecordList")
