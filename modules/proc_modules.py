
import re

def parser(stdout, stderr):
    output = []
    if stdout:
        for line in stdout.splitlines():
            entry = {}
            lineSplit = re.split(r'[\s\t]+', line)
            if lineSplit and len(lineSplit) > 5:
                entry = {
                    'moduleName': lineSplit[0],
                    'moduleMemorySize': lineSplit[1],
                    'numInstancesLoaded': lineSplit[2],
                    'depends': lineSplit[3].strip(',').split(','),
                    'state': lineSplit[4],
                    'kernelMemoryOffset': lineSplit[5]
                }
            if entry:
                output.append(entry)

    return {'output': output}

def register(main):
    main['proc_modules'] = {
        'cmd': 'cat /proc/modules',
        'description': 'List of all modules loaded into the kernel',
        'parser': parser
    }
