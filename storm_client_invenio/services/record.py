# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from pydash import py_

from typeguard import typechecked
from typing import Dict, List, Union

from .base import BaseService
from ..models import Record

from ..object_factory import ObjectFactory

from ..models.record import RecordDraft, RecordBase, create_file_object


def _record_obj_to_dict(record_obj: Union[Dict, RecordBase]):
    """Transform RecordBase instance to a dict instance."""
    return record_obj.to_json() if isinstance(record_obj, RecordBase) else record_obj


@typechecked
class RecordService(BaseService):
    @property
    def is_draft_service(self):
        return self._as_draft

    def __init__(self, url: str, as_draft: bool = False) -> None:
        base_path = "records"
        super(RecordService, self).__init__(url, base_path)

        self._as_draft = as_draft

        # defining the record type
        self._record_type = "Record"
        self._complement_url = ""

        if as_draft:
            self._record_type = "RecordDraft"
            self._complement_url = "draft"

    def resolve(
        self, record_id: str, request_options: Dict = {}
    ) -> Union[RecordBase, None]:
        record_id_url = self._build_url([record_id, self._complement_url])
        operation_result = self._create_request("GET", record_id_url, **request_options)

        return ObjectFactory.resolve(self._record_type, operation_result.json())

    def create(self, data: RecordDraft, request_options: Dict = {}):
        json = _record_obj_to_dict(data)
        operation_result = self._create_request(
            "POST", self.url, json=json, **request_options
        )

        return ObjectFactory.resolve(self._record_type, operation_result.json())

    def save(self, data: RecordDraft, request_options: Dict = {}):
        json = _record_obj_to_dict(data)

        self_record_link = py_.get(json, "links.self", None)
        operation_result = self._create_request(
            "PUT", self_record_link, json=json, **request_options
        )

        # Editable records on storm are new drafts
        return ObjectFactory.resolve("RecordDraft", operation_result.json())

    def new_version(self, data: Record, request_options: Dict = {}) -> RecordDraft:
        json = _record_obj_to_dict(data)

        versions_link = py_.get(json, "links.versions", None)
        operation_result = self._create_request(
            "POST", versions_link, json=json, **request_options
        )

        # New records on storm are drafts
        return ObjectFactory.resolve("RecordDraft", operation_result.json())

    def publish(self, data: RecordDraft, request_options: Dict = {}) -> Record:
        # publishing the resource
        publish_record = data.links["publish"]

        response = self._create_request("POST", publish_record, **request_options)
        return ObjectFactory.resolve("Record", response.json())  # record is fixed here


@typechecked
class RecordFilesService(BaseService):
    def __init__(self, url: str, record_resource: RecordDraft) -> None:
        super(RecordFilesService, self).__init__(url)

        if py_.is_none(record_resource.id):
            raise TypeError(
                "The `record_resource` should be a defined InvenioRDM object."
            )

        self._record_resource = record_resource
        self._record_link_type = type(record_resource.links).__name__

    def _define_record_files(self, files: List, request_options: Dict = {}) -> Dict:
        # preparing the files
        files = py_.map(files, create_file_object)
        files_link = py_.get(self._record_resource, "links.files", None)

        operation_result = self._create_request(
            "POST", files_link, json=files, **request_options
        )
        return operation_result.json()

    def upload_files(
        self, files: Dict, commit: bool = False, request_options: Dict = {}
    ) -> RecordDraft:

        defined_files = self._define_record_files(list(files.keys()))

        for defined_file in py_.get(defined_files, "entries", []):
            defined_file_key = defined_file["key"]
            defined_file_content_link = py_.get(defined_file, "links.content")

            # uploading the file
            file_to_upload = files.get(defined_file_key)

            with open(file_to_upload, "rb") as data:
                response = self._create_request(
                    "PUT", defined_file_content_link, data=data, **request_options
                )

            if commit:
                response_json = response.json()

                commit_url = py_.get(response_json, "links.commit")
                self._create_request("POST", commit_url, json=files, **request_options)

        return self._record_resource.links.self


__all__ = ("RecordService", "RecordFilesService")
