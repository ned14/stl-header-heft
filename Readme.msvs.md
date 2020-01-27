[Explanation of this project](Readme.md)

<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-2019.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-history.png"/>
</center>

## Low token count C++ 20 VS2019 headers

Each of these is in the bottom quartile of token parse times for all STL headers:

- ranges
- version
- climits
- concepts
- compare
- cfloat
- cstddef
- initializer_list
- cassert
- cerrno
- csignal
- cstdarg
- cstdbool
- ciso646
- csetjmp
- cstdalign
- cstdint
- cuchar
- clocale
- cfenv
- cinttypes
- cwctype
- cctype
- ctime


## Lowest token count C++ 20 VS2019 containers

Each of these is less than two thirds the token parse time of the worst STL container header:

- deque
- list
- map
- stack
- set
- vector

## Highest token count C++ 20 VS2019 headers

You may wish to avoid using these headers if compile times are very important
to you:

- array
- bitset
- ccomplex
- codecvt
- complex
- ctgmath
- execution
- filesystem
- future
- iomanip
- regex
- thread
- vector

## Highest token count C++ 20 VS2019 containers

You may wish to avoid using these containers if compile times are very important
to you:

- array

All these are SURPRISING!

## Surprising high token count C++ 20 VS2019 headers

I found these headers have much higher token count than you'd expect.

- atomic
    - Cause: Performs significant preprocessor metaprogramming instead of using
    a pre-expanded edition.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/atomic.csv
- array
    - Cause: Drags in a lot of other headers, including `<algorithm>`, `<iterator>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on. I can't see why when
    libstdc++ doesn't do this.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/array.csv
- complex
    - Cause: Drags in a lot of other headers, including `<sstream>`, `<string>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/complex.csv
