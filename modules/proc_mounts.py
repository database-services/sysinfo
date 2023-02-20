
import re

def parser(stdout, stderr):
    output = []
    if stdout:
        for line in stdout.splitlines():
            entry = {}
            lineSplit = re.split(r'[\s\t]+', line)
            if lineSplit and len(lineSplit) > 4:
                accessValues = {}
                for access in re.split(r',', lineSplit[3]):
                    accessSplit = re.split(r'=', access + '=')
                    accessValues[accessSplit[0]] = accessSplit[1]

                entry = {
                    'device': lineSplit[0],
                    'mountPoint': lineSplit[1],
                    'type': lineSplit[2],
                    'access': accessValues
                }
            if entry:
                output.append(entry)
    
    return {'output': output}

def register(main):
    main['proc_mounts'] = {
        'cmd': 'cat /proc/mounts',
        'description': 'List mounted filesystems (info provides from kernel)',
        'parser': parser
    }
