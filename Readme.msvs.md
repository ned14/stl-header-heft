[Explanation of this project](Readme.md)

## Low token count C++ 17 VS2017 headers

Each of these is in the bottom quartile of token parse times for all STL headers:

- cassert
- cctype
- cerrno
- cfenv
- cfloat
- cinttypes
- climits
- clocale
- csetjmp
- csignal
- cstdarg
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
- new
- ratio
- typeindex
- typeinfo

## Lowest token count C++ 17 VS2017 containers

Each of these is less than half the token parse time of the worst STL container header:

- deque
- list
- map

## Highest token count C++ 17 VS2017 headers

You may wish to avoid using these headers if compile times are very important
to you:

- array
- bitset
- codecvt
- execution
- filesystem
- fstream
- future
- regex
- thread
- vector

Note that the iostream headers apart from `fstream` are fine, they all lie around the median.

## Highest token count C++ 17 VS2017 containers

You may wish to avoid using these containers if compile times are very important
to you:

- array
- forward_list
- string
- vector

All these are SURPRISING!

## Surprising high token count C++ 17 VS2017 headers

I found these headers have much higher token count than you'd expect.

- atomic
    - Cause: Performs significant preprocessor metaprogramming instead of using
    a pre-expanded edition.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/atomic.csv
- array
    - Cause: Drags in a lot of other headers, including `<algorithm>`, `<iterator>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on. I can't see why when
    libstdc++ doesn't do this.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/array.csv
- complex
    - Cause: Drags in a lot of other headers, including `<sstream>`, `<string>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/complex.csv
- forward_list
    - Cause: Includes quite a few internal headers which do limited preprocessor
    metaprogramming, none of each of which would be a problem alone, but added
    together it starts looking big.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/forward_list.csv
- string
    - Cause: Includes `<istream>`, `<ostream>`, `<stdexcept>` and so on.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/string.csv
- vector
    - Cause: Includes quite a few internal headers which do limited preprocessor
    metaprogramming, none of each of which would be a problem alone, but added
    together it starts looking big. libstdc++ implements this as one of the very
    lightest of headers, so I think this implementation could do with some spring
    cleaning.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2017/vector.csv
