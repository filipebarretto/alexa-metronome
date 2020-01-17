# -*- coding: utf-8 -*-

import six
import boto3
import json


def get_slots(slots):
    items = []
    resolved_slot = None
    for _, slot in six.iteritems(slots):
        print(slot)
        if slot.value is not None:
            resolved_slot = slot.value
            items.append(slot.value.lower())
    return items
