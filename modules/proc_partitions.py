
from sysinfo_lib import parseSpaceTable, tableToDict

def parser(stdout, stderr):
    output = {}
    if stdout:
        output = parseSpaceTable(stdout)
        output = tableToDict(output, 'name')

    outputa=[]
    for k,v in output.items():
        outputa.append(v)
    return {'output': outputa}

def register(main):
    main['proc_partitions'] = {
        'cmd': 'cat /proc/partitions',
        'description': 'Partition block allocation information',
        'parser': parser
    }
