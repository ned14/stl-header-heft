#!/usr/bin/python

from __future__ import absolute_import, print_function
import sys, os, subprocess, shutil, glob, multiprocessing, traceback
if __name__ == '__main__' and __package__ is None:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pcpp'))
from pcpp.pcmd import CmdPreprocessor

# multiprocessing capable
def process_header(stl, header_path, flags, header):
    try:
        cmdline = [
            'noexec',
            '-o', os.path.join(stl, header + '.all.hpp'),
            header_path % header,
            '--filetimes=' + os.path.join(stl, header) + '.csv',
            '-D', '__cplusplus=20300000',
            '-D', '__cpp_lib_concepts=1'
        ] + flags
        p = CmdPreprocessor(cmdline)
        print("%s took %f secs" % (header, p.include_times[0].elapsed))
        return (p.include_times[0].elapsed, header)
    except:
        print('%s: %s' % (header, traceback.format_exc()))
        return (-1, header)

stl_headers = [
    "algorithm",
    "any",
    "array",
    "atomic",
    "bitset",
    "cassert",
    "ccomplex",
    "cctype",
    "cerrno",
    "cfenv",
    "cfloat",
    "charconv",
    "chrono",
    "cinttypes",
    "ciso646",
    "climits",
    "clocale",
    "cmath",
    "codecvt",
    "compare",
    "complex",
    "concepts",
    "condition_variable",
    "coroutine",
    "csetjmp",
    "csignal",
    "cstdalign",
    "cstdarg",
    "cstdbool",
    "cstddef",
    "cstdint",
    "cstdio",
    "cstdlib",
    "cstring",
    "ctgmath",
    "ctime",
    "cuchar",
    "cwchar",
    "cwctype",
    "deque",
    "exception",
    "execution",
    "filesystem",
    "forward_list",
    "fstream",
    "functional",
    "future",
    "initializer_list",
    "iomanip",
    "ios",
    "iosfwd",
    "iostream",
    "istream",
    "iterator",
    "limits",
    "list",
    "locale",
    "map",
    "memory",
    "memory_resource",
    "mutex",
    "new",
    "numeric",
    "numbers",
    "optional",
    "ostream",
    "profile",
    "queue",
    "random",
    "ranges",
    "ratio",
    "regex",
    "scoped_allocator",
    "set",
    "shared_mutex",
    "span",
    "sstream",
    "stack",
    "stdexcept",
    "stop_token",
    "streambuf",
    "string",
    "string_view",
    "strstream",
    "system_error",
    "thread",
    "tuple",
    "type_traits",
    "typeindex",
    "typeinfo",
    "unordered_map",
    "unordered_set",
    "utility",
    "valarray",
    "variant",
    "vector",
    "version"
]
stl_headers.sort()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", os.path.basename(sys.argv[0]), "<stdc++-N|c++|msvs-N> [<concurrency>]", file = sys.stderr)
        sys.exit(1)
    stl = sys.argv[1]
    concurrency = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    if stl.startswith('stdc++'):
        ver = int(stl[7:])
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
        if ver < 10:
            stl_headers.remove("coroutine")
            stl_headers.remove("numbers")
            stl_headers.remove("profile")
            stl_headers.remove("span")
            stl_headers.remove("stop_token")
        if ver < 8:
            stl_headers.remove("charconv")
            stl_headers.remove("execution")
            stl_headers.remove("strstream")
            stl_headers = [ 'experimental/filesystem' if x == 'filesystem' else x for x in stl_headers ]
            stl_headers = [ 'experimental/memory_resource' if x == 'memory_resource' else x for x in stl_headers ]
        if ver < 7:
            stl_headers.remove("variant")
            stl_headers = [ 'experimental/any' if x == 'any' else x for x in stl_headers ]
            stl_headers = [ 'experimental/optional' if x == 'optional' else x for x in stl_headers ]
            stl_headers = [ 'experimental/string_view' if x == 'string_view' else x for x in stl_headers ]
        if ver < 6:
            stl_headers.remove("cuchar")
            stl_headers.remove("filesystem")
            stl_headers.remove("memory_resource")
        else:
            print("Unsupported libstdc++ version %d" % ver, file = sys.stderr)
            sys.exit(1)
    elif stl.startswith('msvs'):
        ver = int(stl[5:])
        if ver >= 15:
            crtpath = glob.glob('C:/Program Files (x86)/Windows Kits/10/Include/*')[0]
            #vcpath = glob.glob('C:/Program Files (x86)/Microsoft Visual Studio/%d/Enterprise/VC/Tools/MSVC/*' % ver)[0]
            vcpath = glob.glob('C:/Program Files (x86)/Microsoft Visual Studio/%d/Community/VC/Tools/MSVC/*' % ver)[0]
            flags = [
                '-D', '_WIN32',
                '-D', '_M_X64=1',
                '-D', '_HAS_CXX17=1',
                '-D', '_HAS_CXX20=1',
                '-I', crtpath + '/ucrt',
                '-I', vcpath + '/include',
            ]
            header_path = vcpath + '/include/%s'
            if ver <= 2019:
                stl_headers.remove("coroutine")
                stl_headers.remove("profile")
                stl_headers.remove("stop_token")
            if ver <= 2017:
                stl_headers.remove("charconv")
                stl_headers.remove("compare")
                stl_headers.remove("concepts")
                stl_headers.remove("ranges")
                stl_headers.remove("version")
        else:
            flags = [
                '-D', '_WIN32',
                '-D', '_M_X64=1',
                '-I', 'C:/Program Files (x86)/Microsoft Visual Studio %d.0/VC/include' % ver,
            ]
            header_path = 'C:/Program Files (x86)/Microsoft Visual Studio %d.0/VC/include/%%s' % ver
            if ver <= 12:
                stl_headers.remove("any")
                stl_headers.remove("charconv")
                stl_headers.remove("compare")
                stl_headers.remove("concepts")
                stl_headers.remove("coroutine")
                stl_headers.remove("cuchar")
                stl_headers.remove("execution")
                stl_headers.remove("memory_resource")
                stl_headers.remove("optional")
                stl_headers.remove("profile")
                stl_headers.remove("ranges")
                stl_headers.remove("shared_mutex")
                stl_headers.remove("stop_token")
                stl_headers.remove("string_view")
                stl_headers.remove("variant")
                stl_headers.remove("version")
            if ver <= 11:
                if ver == 11:
                    print("WARNING: VS2012 uses MSVC-specific preprocessor metaprogramming which pcpp will fail to parse")
                stl_headers.remove("cfenv")
                stl_headers.remove("cinttypes")
                stl_headers.remove("filesystem")
                stl_headers.remove("initializer_list")
                stl_headers.remove("strstream")
            if ver <= 9:
                # This is a C++ 03 compiler with TR1
                stl_headers.remove("atomic")
                stl_headers.remove("chrono")
                stl_headers.remove("codecvt")
                stl_headers.remove("condition_variable")
                stl_headers.remove("forward_list")
                stl_headers.remove("future")
                stl_headers.remove("mutex")
                stl_headers.remove("random")
                stl_headers.remove("ratio")
                stl_headers.remove("regex")
                stl_headers.remove("scoped_allocator")
                stl_headers.remove("system_error")
                stl_headers.remove("thread")
                stl_headers.remove("tuple")
                stl_headers.remove("typeindex")

                # Missing conformance
                stl_headers.remove("cstdint")
    else:
        print("STL", stl, "is currently unsupported", file = sys.stderr)
        sys.exit(1)

    try:
        shutil.rmtree(stl)
    except: pass
    os.mkdir(stl)
    os.mkdir(os.path.join(stl, "experimental"))
    stl_headers_times = []
    if concurrency > 1:
        with multiprocessing.Pool(concurrency) as p:
            results = []
            for header in stl_headers:
                results.append(p.apply_async(process_header, (stl, header_path, flags, header)))
            stl_headers_times = [x.get() for x in results]
    else:
        for header in stl_headers:
            stl_headers_times.append(process_header(stl, header_path, flags, header))
    stl_headers_times.sort()
    with open(os.path.join(stl, 'all') + '.csv', 'wt') as oh:
        print('"Seconds","Header"', file = oh)
        for t,p in stl_headers_times:
            print('%f,"%s"' % (t, p), file = oh)
