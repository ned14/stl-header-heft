[Explanation of this project](Readme.md)

<center>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-2019.png"/>
<img src="https://raw.githubusercontent.com/ned14/stl-header-heft/master/graphs/msvs-history.png"/>
</center>

## Low token count C++ 20 VS2019 headers

Each of these is in the bottom quartile of token parse times for all STL headers:

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

Note that `cstdlib` and `cstdio` are not in this list. They have become rather fatter, relatively speaking, in VS2019.

## Lowest token count C++ 20 VS2019 containers

All apart from `<array>` now have a low token count in VS2019.

## Highest token count C++ 20 VS2019 headers

You may wish to avoid using these headers if compile times are very important
to you:

- array
- ccomplex
- codecvt
- complex
- ctgmath
- execution
- filesystem
- fstream
- functional
- future
- iomanip
- ios
- iostream
- istream
- iterator
- locale
- ostream
- random
- ranges
- regex
- sstream
- strstream

## Highest token count C++ 20 VS2019 containers

You may wish to avoid using these containers if compile times are very important
to you:

- array

This is expected to be fixed in VS2020.

## Surprising high token count C++ 20 VS2019 headers

I found these headers have much higher token count than you'd expect.

- atomic
    - Cause: Drags in a lot of other headers. I can't see why when
    libstdc++ doesn't do this.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/atomic.csv
- array
    - Cause: Drags in a lot of other headers, including `<algorithm>`, `<iterator>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on. I can't see why when
    libstdc++ doesn't do this.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/array.csv
- complex
    - Cause: Drags in a lot of other headers, including `<sstream>`, `<string>`,
    `<istream>`, `<ostream>`, `<stdexcept>` and so on. libstdc++ is just as bad.
    - https://github.com/ned14/stl-header-heft/blob/master/msvs-2019/complex.csv
