#!/usr/bin/python

from __future__ import absolute_import, print_function
import sys, os, subprocess, shutil
if __name__ == '__main__' and __package__ is None:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pcpp'))
from pcpp.cmd import CmdPreprocessor

stl_headers = [
    "cstdlib",
    "csignal",
    "csetjmp",
    "cstdarg",
    "typeinfo",
    "typeindex",
    "type_traits",
    "bitset",
    "functional",
    "utility",
    "ctime",
    "chrono",
    "cstddef",
    "initializer_list",
    "tuple",
    "any",
    "optional",
    "variant",
    "new",
    "memory",
    "scoped_allocator",
    "memory_resource",
    "climits",
    "cfloat",
    "cstdint",
    "cinttypes",
    "limits",
    "exception",
    "stdexcept",
    "cassert",
    "system_error",
    "cerrno",
    "cctype",
    "cwctype",
    "cstring",
    "cwchar",
    "cuchar",
    "string",
    "string_view",
    "charconv",
    "array",
    "vector",
    "deque",
    "list",
    "forward_list",
    "set",
    "map",
    "unordered_set",
    "unordered_map",
    "stack",
    "queue",
    "algorithm",
    "execution",
    "iterator",
    "cmath",
    "complex",
    "valarray",
    "random",
    "numeric",
    "ratio",
    "cfenv",
    "iosfwd",
    "ios",
    "istream",
    "ostream",
    "iostream",
    "fstream",
    "sstream",
    "strstream",
    "iomanip",
    "streambuf",
    "cstdio",
    "locale",
    "clocale",
    "codecvt",
    "regex",
    "atomic",
    "thread",
    "mutex",
    "shared_mutex",
    "future",
    "condition_variable",
    "filesystem"
]
stl_headers.sort()

if len(sys.argv) < 2:
    print("Usage:", os.path.basename(sys.argv[0]), "<stdc++-N|c++|msvc>", file = sys.stderr)
    sys.exit(1)
stl = sys.argv[1]
if stl.startswith('stdc++'):
    ver = int(stl[7])
    flags = [
        '-D', '__x86_64__',
        '-D', '__WCHAR_MAX__=0x7fffffff',
        '-D', '__WCHAR_MIN__=(-__WCHAR_MAX__ - 1)',
        '-I', '/usr/include/c++/%d' % ver,
        '-I', '/usr/include/x86_64-linux-gnu/c++/%d' % ver,
        '-I', '/usr/lib/gcc/x86_64-linux-gnu/%d/include' % ver,
        '-I', '/usr/include/x86_64-linux-gnu',
        '-I', '/usr/include',
        '-I', '/usr/local/include'
    ]
    header_path = '/usr/include/c++/%d/%%s' % ver
    if ver == 7:
        stl_headers.remove("charconv")
        stl_headers.remove("execution")
        stl_headers.remove("strstream")
        stl_headers = [ 'experimental/filesystem' if x == 'filesystem' else x for x in stl_headers ]
        stl_headers = [ 'experimental/memory_resource' if x == 'memory_resource' else x for x in stl_headers ]
    elif ver == 6:
        stl_headers.remove("charconv")
        stl_headers.remove("execution")
        stl_headers.remove("strstream")
        stl_headers.remove("variant")
        stl_headers = [ 'experimental/any' if x == 'any' else x for x in stl_headers ]
        stl_headers = [ 'experimental/filesystem' if x == 'filesystem' else x for x in stl_headers ]
        stl_headers = [ 'experimental/memory_resource' if x == 'memory_resource' else x for x in stl_headers ]
        stl_headers = [ 'experimental/optional' if x == 'optional' else x for x in stl_headers ]
        stl_headers = [ 'experimental/string_view' if x == 'string_view' else x for x in stl_headers ]
    elif ver == 5:
        stl_headers.remove("charconv")
        stl_headers.remove("cuchar")
        stl_headers.remove("execution")
        stl_headers.remove("filesystem")
        stl_headers.remove("memory_resource")
        stl_headers.remove("strstream")
        stl_headers.remove("variant")
        stl_headers = [ 'experimental/any' if x == 'any' else x for x in stl_headers ]
        stl_headers = [ 'experimental/optional' if x == 'optional' else x for x in stl_headers ]
        stl_headers = [ 'experimental/string_view' if x == 'string_view' else x for x in stl_headers ]
    else:
        print("Unsupported libstdc++ version %d" % ver, file = sys.stderr)
        sys.exit(1)
else:
    print("STL", stl, "is currently unsupported", file = sys.stderr)
    sys.exit(1)

try:
    shutil.rmtree(stl)
except: pass
os.mkdir(stl)
os.mkdir(os.path.join(stl, "experimental"))
stl_headers_times = []
for header in stl_headers:
    cmdline = [
        'noexec',
        '-o', os.path.join(stl, header + '.all.hpp'),
        header_path % header,
        '--filetimes=' + os.path.join(stl, header) + '.csv',
        '-D', '__cplusplus=20180000'
    ] + flags
    p = CmdPreprocessor(cmdline)
    stl_headers_times.append((p.include_times[0].elapsed, header))
    print("%s took %f secs" % (header, p.include_times[0].elapsed))
stl_headers_times.sort()
with open(os.path.join(stl, 'all') + '.csv', 'wt') as oh:
    print('"Seconds","Header"', file = oh)
    for t,p in stl_headers_times:
        print('%f,"%s"' % (t, p), file = oh)
