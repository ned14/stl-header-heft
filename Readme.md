# STL Header Heft

(C) 2018 Niall Douglas http://www.nedproductions.biz/

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
- What C++ STL headers are high token count to include?

## Low token count C++ 17 libstdc++ headers

Each of these is at most less than half the token parse time of any other
libstdc++ header:

- any
- atomic
- cassert
- cctype
- cerrno
- cfenv
- cfloat
- chrono
- cinttypes
- climits
- clocale
- cmath
- csetjmp
- csignal
- cstdarg
- cstddef
- cstdint
- cstdio
- cstdlib
- cstring
- ctime
- cwchar
- cwctype
- exception
- initializer_list
- iosfwd
- limits
- new
- numeric
- ratio
- type_traits
- typeindex
- typeinfo
- utility

## Lowest token count C++ 17 libstdc++ containers

Each of these is at most less than half the token parse time of any other
libstdc++ container:

- deque
- forward_list
- list
- set
- stack
- vector

## Highest token count C++ 17 libstdc++ headers

You may wish to avoid using these headers if compile times are very important
to you:

- regex
- random
- thread, future, shared_mutex, condition_variable, mutex (any of the threading support)
- memory, memory_resource
- iomanip
- functional

Note that the iostream headers are actually fine, they all lie around the median.

## Highest token count C++ 17 libstdc++ containers

You may wish to avoid using these containers if compile times are very important
to you:

- unordered_map and unordered_set
- map and set
- array (SURPRISING!)
- string (SURPRISING!)
- valarray

## Surprising high token count C++ 17 libstdc++ headers

I found these headers have much higher token count than you'd expect.
As in, at least double of or considerably more than `<vector>`!

- array
- complex
- iterator
- memory
- optional
- string
