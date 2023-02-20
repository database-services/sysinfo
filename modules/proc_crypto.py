
import re
from sysinfo_lib import camelCase

def parser(stdout, stderr):
    output = []
    if stdout:
        for block in re.split(r'\r\r|\n\n|\r\n\r\n', stdout):
            entry = {}
            for line in block.splitlines():
                values = re.search(r'([^\t]+)\s*:\s*(.*)$', line)
                if values:
                    entry[camelCase(values.group(1).strip())] = values.group(2).strip()

            if 'name' in entry:
                output.append(entry)

    return {'output': output}

def register(main):
    main['proc_crypto'] = {
        'cmd': 'cat /proc/crypto',
        'description': 'Installed cryptographic ciphers used by the Linux kernel',
        'parser': parser
    }
