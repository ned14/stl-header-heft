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
- array
- complex
- forward_list
- string
- vector
