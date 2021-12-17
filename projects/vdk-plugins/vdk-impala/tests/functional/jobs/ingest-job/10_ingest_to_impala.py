# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0


def run(job_input):
    payload = {"some_data": "some_test_data", "more_data": "more_test_data"}

    for _ in range(5):
        job_input.send_object_for_ingestion(
            payload=payload, destination_table="test_table"
        )