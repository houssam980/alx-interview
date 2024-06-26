#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = key in boxes[idx] and key != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
