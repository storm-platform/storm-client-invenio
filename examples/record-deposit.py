# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from storm_client_invenio import InvenioRDM
from storm_client_invenio.models.record import Record, RecordDraft

#
# 1. Create a InvenioRDM Client instance.
#
service = InvenioRDM(
    "https://invenio-instance/api",
    "",
)

#
# 2. Create a Record Draft
#

#
# 2.1 Create draft object
#
record_draft = RecordDraft(
    dict(
        metadata=dict(
            title="Example draft",
            description="Example draft description",
            contributors=[
                dict(
                    person_or_org=dict(
                        family_name="Some",
                        given_name="Person",
                        name="Some, Person",
                        type="personal",
                    ),
                    role=dict(id="other", title=dict(en="Other")),
                )
            ],
            creators=[
                dict(
                    person_or_org=dict(
                        family_name="Some",
                        given_name="Person",
                        name="Some, Person",
                        type="personal",
                    )
                )
            ],
            publisher="InvenioRDM Client",
            resource_type=dict(id="software", title=dict(en="Software")),
            rights=[
                dict(
                    id="cc-by-4.0",
                )
            ],
            dates=dict(
                date="2020-05-05", type=dict(id="issued", title=dict(en="Issued"))
            ),
            publication_date="2021-12-08",
        )
    )
)

#
# 2.1 Create draft record in the REST API
#
created_draft = service.records.draft().create(record_draft)
print(created_draft)

#
# 2.2 Draft files
#
updated_draft = service.records.files(created_draft).upload_files(
    {
        "alice.txt": "data/alice.txt",
        "creative-commons.png": "data/creative-commons.png",
    },
    commit=True,
)

#
# 3. Publish the record draft
#
record = service.records.draft().publish(updated_draft)
print(record)


#
# 4. Search Draft and Records
#
print(service.records.search().query(q="is_published: true"))

# Search only for user specific records
user_records = service.records.search(user_records=True).query()
for record in user_records:
    if type(record) == Record:
        print("Record")
        print(type(record))
        print(record.links.draft)

    elif type(record) == RecordDraft:
        print("Record Draft")
        print(type(record))
        print(record.links.draft)
