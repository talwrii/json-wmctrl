import argparse
import itertools
import json
import re
import threading
from multiprocessing.pool import ThreadPool

from Xlib import X, display

PARSER = argparse.ArgumentParser(description='Locate top level X windows')
PARSER.add_argument('--class', dest='cls', help="Search for windows with the class. Regular expression.")
PARSER.add_argument("--next-unfocused", action='store_true', help="If there are multiple windows. Return the one with the lowest window id that is not focused.")
args = PARSER.parse_args()


def main():
    d = display.Display()
    root = d.screen().root

    query = root.query_tree()


    active_windows = root.get_full_property(
        d.intern_atom('_NET_ACTIVE_WINDOW', True), X.AnyPropertyType).value


    windows = root.get_full_property(
        d.intern_atom('_NET_CLIENT_LIST', True), X.AnyPropertyType).value

    data = []
    for window_id in sorted(windows):
        window = d.create_resource_object('window', window_id)

        title = window.get_full_property(
            d.intern_atom("WM_NAME", True), X.AnyPropertyType).value.decode('utf8')

        cls, cls2 = window.get_wm_class()

        if args.cls:
            if not re.search(args.cls, cls2):
                continue

        focus = window_id in active_windows

        data.append({
            "class_other": cls,
            "focus": focus,
            "class": cls2,
            "title": title or "",
            "id": window_id,
        })


    if args.next_unfocused:
        remaining = itertools.dropwhile(lambda d: not d["focus"], data)
        remaining = itertools.islice(remaining, 1, None)
        remaining = list(remaining)
        remaining = remaining or data
        print(json.dumps(remaining[0]))



    else:
        for d in data:
            print(json.dumps(d))
