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
    - Always?
    - Or depending on STL?
- What C++ STL headers are high token count to include?
    - Always?
    - Or depending on STL?

# libstdc++ 5, 6, 7 (2015-2017)
<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-7.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-history.png"/>
</center>

[Detailed observation notes](Readme.libstdc++.md)

# VS2008, VS2012, VS2013, VS2017 (2008-2018)
<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-2017.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-history.png"/>
</center>

[Detailed observation notes](Readme.msvs.md)
