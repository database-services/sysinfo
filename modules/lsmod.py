
import re

def parser(stdout, stderr):
    output = []
    entry = {}
    if stdout:
        for line in stdout.splitlines():
            entry = {}
            lineMatch = re.search(r'^(^\S+)\s*(\d+)\s*(\d+)\s*(.*)$', line)
            if lineMatch:
                entry = {
                    'module': lineMatch.group(1),
                    'size': lineMatch.group(2),
                    'usedNumber': lineMatch.group(3),
                    'usedBy': lineMatch.group(4)
                }
    
            if entry:
                output.append(entry)

    return {'output': output}

def register(main):
    main['lsmod'] = {
        'cmd': 'lsmod',
        'description': 'Show the status of modules in the Linux Kernel',
        'parser': parser
    }
