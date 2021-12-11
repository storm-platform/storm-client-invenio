# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import json
from json import JSONEncoder

from pydash import py_

from .link import BaseLink
from .type import is_draft, is_record

from ..base import BaseModel


class RecordBase(BaseModel):
    links_cls = BaseLink
    serializer_cls = JSONEncoder

    def __init__(self, data=None):
        super(RecordBase, self).__init__(data or {})

    @property
    def id(self):
        return py_.get(self.data, "id", None)

    @property
    def links(self):
        return self.links_cls(py_.get(self.data, "links", None))

    @property
    def is_draft(self):
        return is_draft(self.data)

    @property
    def is_record(self):
        return is_record(self.data)

    def to_json(self):
        return json.loads(json.dumps(self.data, cls=self.serializer_cls))


__all__ = "RecordBase"
