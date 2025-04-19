# JSON wmctrl
This is a partial reimplementation of wmctrl, the linux tool to interact with windows, but supports JSON output for more subtle control.

At the moment, this only supports window listing because that is all I needed. The syntax is not compatible with the original wmctrl.

# Motivation
I use the wmctrl tool to raise windows like so `[[wmctrl]] -x -a "Firefox"`. However, this does not work well if you have multiple windows. I wanted to use wmctrl to get all firefox windows and toggle between them. But the output from wmctrl was difficult to parse.

# Usage
`json-wmctrl` will output all top level windows in JSON.

You can search by class name with `json-wmctrl --class "Firefox"` for example (this support regular expressions).

There is a flag `--next-unfocused` which will output just the next unfocused window.
This can be used together with `wmctrl -i -a` and `jq` to cycle focus through windows.

# Alternatives and prior work
This uses the Xlib python library, which you could use directly. See [this stackoverflow post on the topic](https://stackoverflow.com/questions/52545937/how-can-i-list-all-open-x11-windows-on-gnu-linux-from-a-python-script).

This [C++ command line tool by DarkMaguz](https://github.com/DarkMaguz/SimpleWMCtrl) implements this feature. But it is not easy to install like pip programs.

The command-line tool [jc](https://github.com/kellyjonbrazil/jc) is designed to convert the output of a number of command-line tools to `JSON`. It does not support `wmctrl` at the moment, and this tool contains additional functionality, but support could be easily added and may be added in the future.

# About me
I am @readwithai. I make tools for reading and agency sometimes in Obsidian and occassionally write about these things. I also have a side-line in small useful tools.

If any of that sounds useful, you can follow me on [X](https://x.com/readwithai). I often post about command-line hacks and tools here. You can also follow me on my blog (https://readwithai.substack.com).

Also you could read with [review of note taking with Obsidian](https://readwithai.substack.com/p/note-taking-with-obsidian-much-of).
