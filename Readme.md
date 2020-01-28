# STL Header Heft

(C) 2018 - 2020 Niall Douglas http://www.nedproductions.biz/

Herein lie some STL header token parsing benchmarks as according to my pure
Python C99 preprocessor [pcpp](https://github.com/ned14/pcpp). Although
written in Python, it scales linearly with tokens and has comparable
performance dynamics to a preprocessor/tokeniser written in C or C++
(i.e. it will be mostly some fixed linear multiple slower).

C tokens per file actually has little correlation with header file size which
was a surprise to me. Most C++ compilers will generate an internal DAG
(often called an AST) from the tokens parsed from all the includes and
source files. The generation of this in-memory representation is *usually*
mostly linear to token count. Only when templates get instantiated and
inline functions compiled does the compile time begin to vary significantly
from the parse time, particularly if a lot of SFINAE or complex constexpr is being
repeatedly executed by the compiler.

These benchmarks say nothing about how complex a header is to compile,
only how complex it is to parse. Nevertheless, for million file builds,
milliseconds of difference can add up quickly. Therefore it would be
really useful to know:

- What C++ STL headers are low token count to include?
    - Always?
    - Or depending on STL?
- What C++ STL headers are high token count to include?
    - Always?
    - Or depending on STL?

# libstdc++ 7, 8, 9 (2017-2020)
<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-9.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-history.png"/>
</center>

[Detailed observation notes](Readme.libstdc++.md)

# VS2017, VS2019 (2018-2020)
<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-2019.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-history.png"/>
</center>

[Detailed observation notes](Readme.msvs.md)

## Low token count C++ 20 headers on both libstdc++ 9 and VS2019

Each of these is in the bottom quartile of token parse times for all STL headers
in their respective STLs. You are therefore more likely to be safe if you include
only these:

- cassert
- cctype
- cerrno
- cfenv
- cfloat
- cinttypes
- ciso646
- climits
- clocale
- compare
- csetjmp
- csignal
- cstdalign
- cstdarg
- cstdbool
- cstddef
- cstdint
- cstring
- ctime
- cuchar
- cwctype
- initializer_list
- version

Some of the C headers like `<cmath>`, `<cstdio>` and `<cstdlib>` can be quite heavy in some STLs!

## Highest token count C++ 20 headers on either libstdc++ 9 and VS2019

You may wish to avoid using these headers, especially in global interface
files, if compile times across GCC and MSVC are very important to you:

- algorithm
- array
- bitset
- ccomplex
- codecvt
- complex
- condition_variable
- ctgmath
- deque
- execution
- filesystem
- forward_list
- fstream
- functional
- future
- iomanip
- ios
- iostream
- istream
- iterator
- list
- locale
- map
- memory
- memory_resource
- mutex
- ostream
- queue
- random
- ranges
- regex
- scoped_allocator
- set
- shared_mutex
- sstream
- stack
- stdexcept
- streambuf
- string
- string_view
- strstream
- system_error
- thread
- unordered_map
- unordered_set
- valarray
- variant
- vector
