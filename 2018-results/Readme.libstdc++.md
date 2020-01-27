[Explanation of this project](Readme.md)

<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-7.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/libstdc++-history.png"/>
</center>

## Low token count C++ 17 libstdc++ headers

Each of these is in the bottom quartile of token parse times for all STL headers:

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

Each of these is less than half the token parse time of the worst STL container header:

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

- array
    - Cause: includes `<string>` via `<stdexcept>`!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/array.csv
- complex
    - Cause: includes `<string>` via `<sstream>`!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/complex.csv
- iterator
    - Cause: includes `<ostream>` and `<bits/c++config.h>` many times!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/iterator.csv
- memory
    - Cause: includes `<tuple>`, `<array>`, `<stdexcept>` and `<string>`!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/memory.csv
- optional
    - Cause: includes `<string>` via `<stdexcept>`!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/optional.csv
- string
    - Cause: includes `<bits/c++config.h>` many times!
    - https://github.com/ned14/stl-header-heft/blob/master/stdc%2B%2B-7/string.csv
