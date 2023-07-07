
import re
from sysinfo_lib import camelCase

def parser(stdout, stderr):
    output = []
    entry = {}
    slot = None
    if stdout:
        for line in stdout.splitlines():
            slotSearch = re.search(r'^Slot:\s+(.*)$', line, re.IGNORECASE)
            if slotSearch:
                if entry:
                    output.append(entry)
                entry={}
                slot = slotSearch.group(1).strip()
                entry['slot'] = slot

            keyValueSearch = re.search(r'^(\S[^:]+):\s+(.*)$', line)
            if slot and keyValueSearch:
                entry[camelCase(keyValueSearch.group(1))] = keyValueSearch.group(2).strip()

    return {'output': output}

def register(main):
    main['lspci'] = {
        'cmd': 'lspci -mm -vvv',
        'description': 'List all PCI devices',
        'parser': parser
    }
