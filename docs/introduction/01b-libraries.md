# What is MicroPython?
MicroPython is an implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimized to run on microcontrollers. (*From [micropython.org](https://micropython.org/)*)

MicroPython was originally created by the Australian programmer and physicist Damien George. It is written in [C](https://en.wikipedia.org/wiki/C_(programming_language)).

MicroPython is now an OpenSource project and the source code is available in [GitHub](https://github.com/micropython/micropython).
## Micropython Libraries

When you start up your IDE, it may have a list of python modules built in.  You can list the current modules you have installed by running the `help('modules')` command.

```py
help('modules')
```

## MicroPython Builtin Functions
MicroPython is designed to run quickly in a small memory system.  So it has trimmed down many of the standard Python libraries to fit the needs of microcontrollers.  Most of these libraries start with the letter "u" so that you are aware they are designed to run on microcontrollers.

```txt
cmath – mathematical functions for complex numbers
gc – control the garbage collector
math – mathematical functions
uarray – arrays of numeric data
uasyncio — asynchronous I/O scheduler
ubinascii – binary/ASCII conversions
ucollections – collection and container types
uerrno – system error codes
uhashlib – hashing algorithms
uheapq – heap queue algorithm
uio – input/output streams
ujson – JSON encoding and decoding
uos – basic “operating system” services
ure – simple regular expressions
uselect – wait for events on a set of streams
usocket – socket module
ussl – SSL/TLS module
ustruct – pack and unpack primitive data types
usys – system specific functions
utime – time related functions
uzlib – zlib decompression
_thread – multithreading support
```

## MicroPython Specific Libraries

```text
btree – simple BTree database
framebuf — frame buffer manipulation
machine — functions related to the hardware
micropython – access and control MicroPython internals
network — network configuration
ubluetooth — low-level Bluetooth
ucryptolib – cryptographic ciphers
uctypes – access binary data in a structured way
```

## Adding a module

When you are using python and you attempt to use a module that python can't find you will get an error.  You must then use the python `pip` installer tool to add the new library.

## Getting MicroPython Libraries from PyPi


[Filter Only MicroPython Libraries](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython)

## Full List of modules

```text
ESP-test            audioop             filecmp             random
__future__          base64              fileinput           re
_abc                bcrypt              fnmatch             readline
_ast                bdb                 formatter           reedsolo
_asyncio            binascii            fractions           reprlib
_bisect             binhex              ftplib              resource
_blake2             bisect              functools           rlcompleter
_bootlocale         bitstring           gc                  runpy
_bz2                blink-builtin-led   genericpath         sched
_cffi_backend       brain_argparse      getopt              secrets
_codecs             brain_attrs         getpass             select
_codecs_cn          brain_builtin_inference gettext         selectors
_codecs_hk          brain_collections   glob                send2trash
_codecs_iso2022     brain_crypt         grp                 serial
_codecs_jp          brain_curses        gzip                setuptools
_codecs_kr          brain_dataclasses   hashlib             sh1106
_codecs_tw          brain_dateutil      heapq               sh1106-test
_collections        brain_fstrings      hmac                shelve
_collections_abc    brain_functools     html                shlex
_compat_pickle      brain_gi            http                shutil
_compression        brain_hashlib       i2c-display         signal
_contextvars        brain_http          i2c-scanner         site
_crypt              brain_io            i2c_lcd             six
_csv                brain_mechanize     i2clcd              smtpd
_ctypes             brain_multiprocessing imaplib           smtplib
_ctypes_test        brain_namedtuple_enum imghdr            sndhdr
_curses             brain_nose          imp                 socket
_curses_panel       brain_numpy_core_fromnumeric importlib  socketserver
_datetime           brain_numpy_core_function_base inspect  spi-debug
_dbm                brain_numpy_core_multiarray io          sqlite3
_decimal            brain_numpy_core_numeric ipaddress      sre_compile
_dummy_thread       brain_numpy_core_numerictypes isort     sre_constants
_elementtree        brain_numpy_core_umath itertools        sre_parse
_functools          brain_numpy_ndarray jedi                ssl
_hashlib            brain_numpy_random_mtrand json          stat
_heapq              brain_numpy_utils   keyword             statistics
_imp                brain_pkg_resources lazy_object_proxy   string
_io                 brain_pytest        led-strip           stringprep
_json               brain_qt            lib2to3             struct
_locale             brain_random        linecache           subprocess
_lsprof             brain_re            list-modules        sunau
_lzma               brain_six           locale              symbol
_markupbase         brain_ssl           logging             symtable
_md5                brain_subprocess    lzma                sys
_multibytecodec     brain_threading     macpath             sysconfig
_multiprocessing    brain_typing        mailbox             syslog
_opcode             brain_uuid          mailcap             tabnanny
_operator           builtins            marshal             tarfile
_osx_support        bz2                 math                telnetlib
_pickle             cProfile            mccabe              tempfile
_posixsubprocess    calendar            mimetypes           termios
_py_abc             certifi             mmap                test
_pydecimal          cffi                modulefinder        textwrap
_pyio               cgi                 multiprocessing     this
_queue              cgitb               mypy                thonny
_random             chunk               mypy_extensions     threading
_scproxy            clonevirtualenv     mypyc               time
_sha1               cmath               nacl                timeit
_sha256             cmd                 netrc               tkinter
_sha3               code                nis                 token
_sha512             codecs              nntplib             tokenize
_signal             codeop              ntpath              toml
_sitebuiltins       collections         nturl2path          trace
_socket             colorsys            numbers             traceback
_sqlite3            compileall          opcode              tracemalloc
_sre                concurrent          operator            tty
_ssl                configparser        optparse            turtle
_stat               contextlib          os                  turtledemo
_string             contextvars         paramiko            typed_ast
_strptime           copy                parser              types
_struct             copyreg             parso               typing
_symtable           crypt               pathlib             typing_extensions
_sysconfigdata_m_darwin_darwin cryptography        pdb      unicodedata
_testbuffer         csv                 pickle              unittest
_testcapi           ctypes              pickletools         urllib
_testimportmultiple curses              pip                 uu
_testmultiphase     dataclasses         pipenv              uuid
_thread             datetime            pipes               venv
_threading_local    dbm                 pkg_resources       virtualenv
_tkinter            decimal             pkgutil             virtualenv_support
_tracemalloc        difflib             platform            warnings
_uuid               dir-example         plistlib            wave
_warnings           dis                 poplib              weakref
_weakref            distutils           posix               webbrowser
_weakrefset         doctest             posixpath           websockets
_xxtestfuzz         docutils            pprint              wheel
abc                 dummy_threading     profile             wrapt
aifc                easy_install        pstats              wsgiref
antigravity         ecdsa               pty                 xdrlib
argparse            email               ptyprocess          xml
array               encodings           pwd                 xmlrpc
array-test          ensurepip           py_compile          xxlimited
ast                 enum                pyclbr              xxsubtype
astroid             errno               pycparser           zipapp
asttokens           espefuse            pydoc               zipfile
asynchat            espressif           pydoc_data          zipimport
asyncio             espsecure           pyexpat             zlib
asyncore            esptool             pylint              
at                  faulthandler        queue               
atexit              fcntl               quopri              
```

