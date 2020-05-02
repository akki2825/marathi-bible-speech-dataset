# -*- coding: utf-8 -*-
"""
Script to align text and corresponding voice sample using forced alignment.

Usage:
    aligner.py --audio-file=<a> --text-file=<t> --syncmap-file=<s>

Options:
    --audio-file=<a>        Audio file path
    --text-file=<t>         Text file path
    --syncmap-file=<s>      Syncmap file path
"""
from docopt import docopt
from aeneas.executetask import ExecuteTask
from aeneas.task import Task


if __name__ == "__main__":
    args = docopt(__doc__)

    audio_file = args["--audio-file"]

    text_file = args["--text-file"]

    syncmap_file = args["--syncmap-file"]

    config_string = u"task_language=kan|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)

    task.audio_file_path_absolute = audio_file
    task.text_file_path_absolute = text_file
    task.sync_map_file_path_absolute = syncmap_file

    # process Task
    ExecuteTask(task).execute()
    task.output_sync_map_file()
