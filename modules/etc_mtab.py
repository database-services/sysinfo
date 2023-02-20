
import re

def parser(stdout, stderr):
    output = []
    if stdout:
        for line in stdout.splitlines():
            entry={}
            values = re.split(r'\s+', line)
            if len(values) > 5:
                entry = {
                    'partition': values[0],
                    'mountPoint': values[1],
                    'fileSystem': values[2],
                    'mountOptions': re.split(r',', values[3]),
                    'dump': values[4],
                    'fsckOrder': values[5]
                }
            if entry:
                output.append(entry)

    return {'output': output}

def register(main):
    main['etc_mtab'] = {
        'cmd': 'cat /etc/mtab',
        'description': 'Currently mounted filesystems',
        'parser': parser
    }
