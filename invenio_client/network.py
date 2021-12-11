# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import httpx
from pydash import py_

from .store import TokenStore


class HTTPXClient:
    @classmethod
    def __proxy_request(cls, request_options=None):
        # proxing the request with the authentication headers
        service_access_token = TokenStore.get_token()

        return py_.merge(
            request_options or {},
            {"headers": {"Authorization": f"Bearer {service_access_token}"}},
        )

    @classmethod
    def request(cls, method, url, **kwargs):
        """Synchronous HTTP request.

        Request an URL using the specified HTTP `method`.

        Args:
            method (str): HTTP Method used to request (e.g. `GET`, `POST`, `PUT`, `DELETE`)

            url (str): URL that will be requested

            **kwargs (dict): Extra parameters to `httpx.request` method.

        Returns:
            Response: Request response.

        See:
            This method as based on httpx.Client. Please, check the documentation for more informations: https://www.python-httpx.org
        """
        with httpx.Client(verify=False) as client:
            return client.request(method, url, **cls.__proxy_request(kwargs))

    @classmethod
    def download(cls, url, output_file):
        """Download files."""
        _request_token = cls.__proxy_request()

        with httpx.Client(verify=False) as client:
            with client.stream("GET", url, **_request_token) as response:
                with open(output_file, "wb") as ofile:
                    for chunk in response.aiter_bytes():
                        ofile.write(chunk)
        return output_file


__all__ = "HTTPXClient"
