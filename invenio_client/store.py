# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


class TokenStore:
    """Single source of truth for access token storage and retrieval."""

    __access_token = None

    @classmethod
    def save_token(cls, token):
        cls.__access_token = token

    @classmethod
    def get_token(cls):
        if not cls.__access_token:
            raise RuntimeError("Access token is not defined yet. Please, define it.")
        return cls.__access_token


__all__ = "TokenStore"
