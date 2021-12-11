# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from ..object_factory import ObjectFactory

from .record.link import RecordDraftLink, RecordLink
from .record.files import RecordFiles, RecordFileEntry
from .record.model import RecordDraft, Record, RecordList

CLASSES_FACTORY = {
    "RecordDraft": RecordDraft,
    "RecordFiles": RecordFiles,
    "Record": Record,
    "RecordFileEntry": RecordFileEntry,
    "RecordDraftLink": RecordDraftLink,
    "RecordLink": RecordLink,
    "RecordList": RecordList,
}

py_.map(CLASSES_FACTORY.keys(), lambda x: ObjectFactory.register(x, CLASSES_FACTORY[x]))

__all__ = "CLASSES_FACTORY"
