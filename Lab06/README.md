# Lab06

## Environment

- Ubuntu 22.04.2 LTS
- gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
- valgrind-3.18.1

## Valgrind v.s. ASAN

| | Valgrind | ASAN |
|:-:|:-:|:-:|
| Heap out-of-bounds | :o: | :o: |
| Stack out-of-bounds | :o: | :o: |
| Global out-of-bounds | :x: | :o: |
| Use-after-free | :o: | :o: |
| Use-after-return | :o: | :o: |

### Heap out-of-bounds

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char * s = (char *)malloc(sizeof(char));
    s[1] = '\0';
    puts(s);
}
```

```
=================================================================
==1155==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000011 at pc 0x5598ef4a3216 bp 0x7ffcadb1c230 sp 0x7ffcadb1c220
WRITE of size 1 at 0x602000000011 thread T0
    #0 0x5598ef4a3215 in main src/hoob.c:6
    #1 0x7f464e5e0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f464e5e0e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x5598ef4a3104 in _start (/home/alardutp/labs/playground/Lab06/asan/hoob+0x1104)

0x602000000011 is located 0 bytes to the right of 1-byte region [0x602000000010,0x602000000011)
allocated by thread T0 here:
    #0 0x7f464e893867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x5598ef4a31da in main src/hoob.c:5
    #2 0x7f464e5e0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-buffer-overflow src/hoob.c:6 in main
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[01]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==1155==ABORTING
```

```
==1156== Memcheck, a memory error detector
==1156== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1156== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==1156== Command: ./valg/hoob
==1156==
==1156== Invalid write of size 1
==1156==    at 0x10917E: main (hoob.c:6)
==1156==  Address 0x4a8b041 is 0 bytes after a block of size 1 alloc'd
==1156==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1156==    by 0x10917A: main (hoob.c:5)
==1156==
==1156== Conditional jump or move depends on uninitialised value(s)
==1156==    at 0x484ED19: strlen (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1156==    by 0x48E0EE7: puts (ioputs.c:35)
==1156==    by 0x109186: main (hoob.c:7)
==1156==

==1156==
==1156== HEAP SUMMARY:
==1156==     in use at exit: 1 bytes in 1 blocks
==1156==   total heap usage: 2 allocs, 1 frees, 1,025 bytes allocated
==1156==
==1156== LEAK SUMMARY:
==1156==    definitely lost: 1 bytes in 1 blocks
==1156==    indirectly lost: 0 bytes in 0 blocks
==1156==      possibly lost: 0 bytes in 0 blocks
==1156==    still reachable: 0 bytes in 0 blocks
==1156==         suppressed: 0 bytes in 0 blocks
==1156== Rerun with --leak-check=full to see details of leaked memory
==1156==
==1156== Use --track-origins=yes to see where uninitialised values come from
==1156== For lists of detected and suppressed errors, rerun with: -s
==1156== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

Asan 能, valgrind 能

### Stack out-of-bounds

```c
#include <stdio.h>

int main() {
    char s[1];
    s[1] = '\0';
    puts(s);
}
```

```
=================================================================
==1318==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffc12cc5651 at pc 0x563c24b662d8 bp 0x7ffc12cc5620 sp 0x7ffc12cc5610
WRITE of size 1 at 0x7ffc12cc5651 thread T0
    #0 0x563c24b662d7 in main src/soob.c:5
    #1 0x7f4c11be6d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f4c11be6e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x563c24b66124 in _start (/home/alardutp/labs/playground/Lab06/asan/soob+0x1124)

Address 0x7ffc12cc5651 is located in stack of thread T0 at offset 33 in frame
    #0 0x563c24b661f8 in main src/soob.c:3

  This frame has 1 object(s):
    [32, 33) 's' (line 4) <== Memory access at offset 33 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow src/soob.c:5 in main
Shadow bytes around the buggy address:
  0x100002590a70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590a80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590a90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590aa0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590ab0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x100002590ac0: 00 00 00 00 00 00 f1 f1 f1 f1[01]f3 f3 f3 00 00
  0x100002590ad0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590ae0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590af0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590b00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100002590b10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==1318==ABORTING
```

```
==1320== Memcheck, a memory error detector
==1320== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1320== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==1320== Command: ./valg/soob
==1320==
==1320== Conditional jump or move depends on uninitialised value(s)
==1320==    at 0x484ED19: strlen (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1320==    by 0x48E0EE7: puts (ioputs.c:35)
==1320==    by 0x10918F: main (soob.c:6)
==1320==

==1320==
==1320== HEAP SUMMARY:
==1320==     in use at exit: 0 bytes in 0 blocks
==1320==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==1320==
==1320== All heap blocks were freed -- no leaks are possible
==1320==
==1320== Use --track-origins=yes to see where uninitialised values come from
==1320== For lists of detected and suppressed errors, rerun with: -s
==1320== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

Asan 能, valgrind 能

### Global out-of-bounds

```c
#include <stdio.h>

char s[1];

int main() {
    s[1] = '\0';
    puts(s);
}
```

```
=================================================================
==1334==ERROR: AddressSanitizer: global-buffer-overflow on address 0x5628c54350a1 at pc 0x5628c5432233 bp 0x7fffd0776360 sp 0x7fffd0776350
WRITE of size 1 at 0x5628c54350a1 thread T0
    #0 0x5628c5432232 in main src/goob.c:6
    #1 0x7f7414ad0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f7414ad0e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x5628c5432124 in _start (/home/alardutp/labs/playground/Lab06/asan/goob+0x1124)

0x5628c54350a1 is located 0 bytes to the right of global variable 's' defined in 'src/goob.c:3:6' (0x5628c54350a0) of size 1
  's' is ascii string ''
SUMMARY: AddressSanitizer: global-buffer-overflow src/goob.c:6 in main
Shadow bytes around the buggy address:
  0x0ac598a7e9c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7e9d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7e9e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7e9f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7ea00: 00 00 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9 f9 f9
=>0x0ac598a7ea10: 00 00 00 00[01]f9 f9 f9 f9 f9 f9 f9 00 00 00 00
  0x0ac598a7ea20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7ea30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7ea40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7ea50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac598a7ea60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==1334==ABORTING
```

```
==1335== Memcheck, a memory error detector
==1335== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1335== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==1335== Command: ./valg/goob
==1335==

==1335==
==1335== HEAP SUMMARY:
==1335==     in use at exit: 0 bytes in 0 blocks
==1335==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==1335==
==1335== All heap blocks were freed -- no leaks are possible
==1335==
==1335== For lists of detected and suppressed errors, rerun with: -s
==1335== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

Asan 能, valgrind 不能

### Use-after-free

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char * s = (char *)malloc(sizeof(char));
    *s = '\0';
    free(s);
    puts(s);
}
```

```
=================================================================
==1349==ERROR: AddressSanitizer: heap-use-after-free on address 0x602000000010 at pc 0x7f70fbc1fc12 bp 0x7fffeff5c770 sp 0x7fffeff5bf18
READ of size 2 at 0x602000000010 thread T0
    #0 0x7f70fbc1fc11 in __interceptor_puts ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1286
    #1 0x55de11a5a1f2 in main src/uaf.c:8
    #2 0x7f70fb9e0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #3 0x7f70fb9e0e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #4 0x55de11a5a104 in _start (/home/alardutp/labs/playground/Lab06/asan/uaf+0x1104)

0x602000000011 is located 0 bytes to the right of 1-byte region [0x602000000010,0x602000000011)
freed by thread T0 here:
    #0 0x7f70fbc93517 in __interceptor_free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:127
    #1 0x55de11a5a1ea in main src/uaf.c:7
    #2 0x7f70fb9e0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

previously allocated by thread T0 here:
    #0 0x7f70fbc93867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x55de11a5a1df in main src/uaf.c:5
    #2 0x7f70fb9e0d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-use-after-free ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1286 in __interceptor_puts
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==1349==ABORTING
```

```
==1350== Memcheck, a memory error detector
==1350== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1350== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==1350== Command: ./valg/uaf
==1350==
==1350== Invalid read of size 1
==1350==    at 0x484ED16: strlen (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1350==    by 0x48E0EE7: puts (ioputs.c:35)
==1350==    by 0x1091AA: main (uaf.c:8)
==1350==  Address 0x4a8b040 is 0 bytes inside a block of size 1 free'd
==1350==    at 0x484B27F: free (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1350==    by 0x1091A2: main (uaf.c:7)
==1350==  Block was alloc'd at
==1350==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1350==    by 0x109197: main (uaf.c:5)
==1350==

==1350==
==1350== HEAP SUMMARY:
==1350==     in use at exit: 0 bytes in 0 blocks
==1350==   total heap usage: 2 allocs, 2 frees, 1,025 bytes allocated
==1350==
==1350== All heap blocks were freed -- no leaks are possible
==1350==
==1350== For lists of detected and suppressed errors, rerun with: -s
==1350== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

Asan 能, valgrind 能

### Use-after-return

```c
#include <stdio.h>

char * uar() {
    char s[1];
    s[0] = '\0';
    return s;
}

int main() {
    puts(uar());
}
```

```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==1364==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fe44ec1297d bp 0x7ffdda456fd0 sp 0x7ffdda456768 T0)
==1364==The signal is caused by a READ memory access.
==1364==Hint: address points to the zero page.
    #0 0x7fe44ec1297d  (/lib/x86_64-linux-gnu/libc.so.6+0x19d97d)
    #1 0x7fe44ecddb1b in __interceptor_puts ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1286
    #2 0x55a48da03389 in main src/uar.c:10
    #3 0x7fe44ea9ed8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #4 0x7fe44ea9ee3f in __libc_start_main_impl ../csu/libc-start.c:392
    #5 0x55a48da03124 in _start (/home/alardutp/labs/playground/Lab06/asan/uar+0x1124)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0x19d97d)
==1364==ABORTING
```

```
==1367== Memcheck, a memory error detector
==1367== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1367== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==1367== Command: ./valg/uar
==1367==
==1367== Invalid read of size 1
==1367==    at 0x484ED16: strlen (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1367==    by 0x48E0EE7: puts (ioputs.c:35)
==1367==    by 0x109164: main (uar.c:10)
==1367==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1367==
==1367==
==1367== Process terminating with default action of signal 11 (SIGSEGV)
==1367==  Access not within mapped region at address 0x0
==1367==    at 0x484ED16: strlen (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==1367==    by 0x48E0EE7: puts (ioputs.c:35)
==1367==    by 0x109164: main (uar.c:10)
==1367==  If you believe this happened as a result of a stack
==1367==  overflow in your program's main thread (unlikely but
==1367==  possible), you can try to increase the size of the
==1367==  main thread stack using the --main-stacksize= flag.
==1367==  The main thread stack size used in this run was 8388608.
==1367==
==1367== HEAP SUMMARY:
==1367==     in use at exit: 0 bytes in 0 blocks
==1367==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==1367==
==1367== All heap blocks were freed -- no leaks are possible
==1367==
==1367== For lists of detected and suppressed errors, rerun with: -s
==1367== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault
```

Asan 能, valgrind 能

## Readzone bypass

```c
#include <stdio.h>

#define ARRSIZE 8
#define BYPASS ARRSIZE + 8

int main() {
    int a[ARRSIZE], b[ARRSIZE];
    a[BYPASS] = 87;
    printf("%d\n", b[0]);
}
```

```
87
```
