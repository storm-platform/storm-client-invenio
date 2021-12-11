# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""InvenioRDM Client API services accessor."""

from .store import TokenStore
from .services.accessor import RecordAccessor


class InvenioRDM:
    def __init__(self, url, access_token, token_store=TokenStore):
        self._url = url

        # configuring the access token store
        token_store.save_token(access_token)

    @property
    def records(self):
        return RecordAccessor(self._url)


__all__ = "Storm"
