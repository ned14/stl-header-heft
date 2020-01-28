[Explanation of this project](Readme.md)

<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-9.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-history.png"/>
</center>

## Low token count C++ 20 libstdc++-9 headers

Each of these is in the bottom quartile of token parse times for all STL headers:

- atomic
- cassert
- cctype
- cerrno
- cfenv
- cfloat
- charconv
- chrono
- cinttypes
- ciso646
- climits
- clocale
- csetjmp
- csignal
- cstdalign
- cstdarg
- cstdbool
- cstddef
- cstdint
- cstdio
- cstdlib
- cstring
- ctime
- cuchar
- cwchar
- cwctype
- exception
- initializer_list
- iosfwd
- limits
- new
- ratio
- type_traits
- typeindex
- typeinfo
- utility
- version

## Lowest token count C++ 20 libstdc++-9 containers

Each of these is less than half the token parse time of the worst STL container header:

- deque
- forward_list
- list
- vector

## Highest token count C++ 20 libstdc++-9 headers

You may wish to avoid using these headers if compile times are very important
to you:

- algorithm
- filesystem
- functional
- iomanip
- memory, memory_resource
- regex
- random
- thread, future, shared_mutex, condition_variable, mutex, execution (any of the threading support)

Note that the iostream headers are actually fine, they all lie around the median.

## Highest token count C++ 20 libstdc++-9 containers

You may wish to avoid using these containers if compile times are very important
to you:

- unordered_map and unordered_set
- map and set
- valarray
