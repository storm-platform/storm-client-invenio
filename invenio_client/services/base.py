# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import posixpath

from ..network import HTTPXClient


class BaseService:
    def __init__(
        self,
        service_url: str,
        base_path: str = None,
        **kwargs,
    ) -> None:
        self._base_path = base_path
        self._service_url = service_url

    @property
    def url(self):
        if not self._base_path:
            raise NotImplemented(
                "This method is implemented to use `service_url` and `base_path`."
            )

        return posixpath.join(self._service_url, self._base_path)

    def _build_url(self, urls):
        return posixpath.join(*[self.url, *urls]).strip("/")

    def _create_request(self, method, url, **kwargs):
        response = HTTPXClient.request(
            method,
            url,
            **kwargs,
        )

        response.raise_for_status()
        return response


__all__ = "BaseService"
