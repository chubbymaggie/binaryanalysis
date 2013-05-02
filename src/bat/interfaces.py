#!/usr/bin/python

## Binary Analysis Tool

'''This file contains information about several APIs and standards
such as POSIX'''

## data extracted from various POSIX standards
## http://pubs.opengroup.org/onlinepubs/9699919799/idx/functions.html
posixfunctions = ["FD_CLR",
         "FD_ISSET",
         "FD_SET",
         "FD_ZERO",
         "_Exit",
         "_exit",
         "_longjmp",
         "_setjmp",
         "_tolower",
         "_toupper",
         "a64l",
         "abort",
         "abs",
         "accept",
         "access",
         "acosf",
         "acoshf",
         "acosh",
         "acoshl",
         "acos",
         "acosl",
         "aio_cancel",
         "aio_error",
         "aio_fsync",
         "aio_read",
         "aio_return",
         "aio_suspend",
         "aio_write",
         "alarm",
         "alphasort",
         "asctime",
         "asctime_r",
         "asinf",
         "asinhf",
         "asinh",
         "asinhl",
         "asin",
         "asinl",
         "assert",
         "atan2f",
         "atan2",
         "atan2l",
         "atanf",
         "atanhf",
         "atanh",
         "atanhl",
         "atan",
         "atanl",
         "atexit",
         "atof",
         "atoi",
         "atol",
         "atoll",
         "basename",
         "bind",
         "bsearch",
         "btowc",
         "cabsf",
         "cabs",
         "cabsl",
         "cacosf",
         "cacoshf",
         "cacosh",
         "cacoshl",
         "cacos",
         "cacosl",
         "calloc",
         "cargf",
         "carg",
         "cargl",
         "casinf",
         "casinhf",
         "casinh",
         "casinhl",
         "casin",
         "casinl",
         "catanf",
         "catanhf",
         "catanh",
         "catanhl",
         "catan",
         "catanl",
         "catclose",
         "catgets",
         "catopen",
         "cbrtf",
         "cbrt",
         "cbrtl",
         "ccosf",
         "ccoshf",
         "ccosh",
         "ccoshl",
         "ccos",
         "ccosl",
         "ceilf",
         "ceil",
         "ceill",
         "cexpf",
         "cexp",
         "cexpl",
         "cfgetispeed",
         "cfgetospeed",
         "cfsetispeed",
         "cfsetospeed",
         "chdir",
         "chmod",
         "chown",
         "cimagf",
         "cimag",
         "cimagl",
         "clearerr",
         "clock_getcpuclockid",
         "clock_getres",
         "clock_gettime",
         "clock",
         "clock_nanosleep",
         "clock_settime",
         "clogf",
         "clog",
         "clogl",
         "closedir",
         "close",
         "closelog",
         "confstr",
         "conjf",
         "conj",
         "conjl",
         "connect",
         "copysignf",
         "copysign",
         "copysignl",
         "cosf",
         "coshf",
         "cosh",
         "coshl",
         "cos",
         "cosl",
         "cpowf",
         "cpow",
         "cpowl",
         "cprojf",
         "cproj",
         "cprojl",
         "crealf",
         "creal",
         "creall",
         "creat",
         "crypt",
         "csinf",
         "csinhf",
         "csinh",
         "csinhl",
         "csin",
         "csinl",
         "csqrtf",
         "csqrt",
         "csqrtl",
         "ctanf",
         "ctanhf",
         "ctanh",
         "ctanhl",
         "ctan",
         "ctanl",
         "ctermid",
         "ctime",
         "ctime_r",
         "dbm_clearerr",
         "dbm_close",
         "dbm_delete",
         "dbm_error",
         "dbm_fetch",
         "dbm_firstkey",
         "dbm_nextkey",
         "dbm_open",
         "dbm_store",
         "difftime",
         "dirfd",
         "dirname",
         "div",
         "dlclose",
         "dlerror",
         "dlopen",
         "dlsym",
         "dprintf",
         "drand48",
         "dup2",
         "dup",
         "duplocale",
         "encrypt",
         "endgrent",
         "endhostent",
         "endnetent",
         "endprotoent",
         "endpwent",
         "endservent",
         "endutxent",
         "erand48",
         "erfcf",
         "erfc",
         "erfcl",
         "erff",
         "erf",
         "erfl",
         "execle",
         "execl",
         "execlp",
         "execve",
         "execv",
         "execvp",
         "exit",
         "exp2f",
         "exp2",
         "exp2l",
         "expf",
         "exp",
         "expl",
         "expm1f",
         "expm1",
         "expm1l",
         "fabsf",
         "fabs",
         "fabsl",
         "faccessat",
         "fattach",
         "fchdir",
         "fchmodat",
         "fchmod",
         "fchownat",
         "fchown",
         "fclose",
         "fcntl",
         "fdatasync",
         "fdetach",
         "fdimf",
         "fdim",
         "fdiml",
         "fdopendir",
         "fdopen",
         "feclearexcept",
         "fegetenv",
         "fegetexceptflag",
         "fegetround",
         "feholdexcept",
         "feof",
         "feraiseexcept",
         "ferror",
         "fesetenv",
         "fesetexceptflag",
         "fesetround",
         "fetestexcept",
         "feupdateenv",
         "fexecve",
         "fflush",
         "ffs",
         "fgetc",
         "fgetpos",
         "fgets",
         "fgetwc",
         "fgetws",
         "fileno",
         "flockfile",
         "floorf",
         "floor",
         "floorl",
         "fmaf",
         "fma",
         "fmal",
         "fmaxf",
         "fmax",
         "fmaxl",
         "fmemopen",
         "fminf",
         "fmin",
         "fminl",
         "fmodf",
         "fmod",
         "fmodl",
         "fmtmsg",
         "fnmatch",
         "fopen",
         "fork",
         "fpathconf",
         "fpclassify",
         "fprintf",
         "fputc",
         "fputs",
         "fputwc",
         "fputws",
         "fread",
         "freeaddrinfo",
         "free",
         "freelocale",
         "freopen",
         "frexpf",
         "frexp",
         "frexpl",
         "fscanf",
         "fseek",
         "fseeko",
         "fsetpos",
         "fstatat",
         "fstat",
         "fstatvfs",
         "fsync",
         "ftell",
         "ftello",
         "ftok",
         "ftruncate",
         "ftrylockfile",
         "ftw",
         "funlockfile",
         "futimens",
         "fwide",
         "fwprintf",
         "fwrite",
         "fwscanf",
         "gai_strerror",
         "getaddrinfo",
         "getchar",
         "getchar_unlocked",
         "getc",
         "getc_unlocked",
         "getcwd",
         "getdate",
         "getdelim",
         "getegid",
         "getenv",
         "geteuid",
         "getgid",
         "getgrent",
         "getgrgid",
         "getgrgid_r",
         "getgrnam",
         "getgrnam_r",
         "getgroups",
         "gethostent",
         "gethostid",
         "gethostname",
         "getitimer",
         "getline",
         "getlogin",
         "getlogin_r",
         "getmsg",
         "getnameinfo",
         "getnetbyaddr",
         "getnetbyname",
         "getnetent",
         "getopt",
         "getpeername",
         "getpgid",
         "getpgrp",
         "getpid",
         "getpmsg",
         "getppid",
         "getpriority",
         "getprotobyname",
         "getprotobynumber",
         "getprotoent",
         "getpwent",
         "getpwnam",
         "getpwnam_r",
         "getpwuid",
         "getpwuid_r",
         "getrlimit",
         "getrusage",
         "getservbyname",
         "getservbyport",
         "getservent",
         "gets",
         "getsid",
         "getsockname",
         "getsockopt",
         "getsubopt",
         "gettimeofday",
         "getuid",
         "getutxent",
         "getutxid",
         "getutxline",
         "getwchar",
         "getwc",
         "globfree",
         "glob",
         "gmtime",
         "gmtime_r",
         "grantpt",
         "hcreate",
         "hdestroy",
         "hsearch",
         "htonl",
         "htons",
         "hypotf",
         "hypot",
         "hypotl",
         "iconv_close",
         "iconv",
         "iconv_open",
         "if_freenameindex",
         "if_indextoname",
         "if_nameindex",
         "if_nametoindex",
         "ilogbf",
         "ilogb",
         "ilogbl",
         "imaxabs",
         "imaxdiv",
         "inet_addr",
         "inet_ntoa",
         "inet_ntop",
         "inet_pton",
         "initstate",
         "insque",
         "ioctl",
         "isalnum",
         "isalnum_l",
         "isalpha",
         "isalpha_l",
         "isascii",
         "isastream",
         "isatty",
         "isblank",
         "isblank_l",
         "iscntrl",
         "iscntrl_l",
         "isdigit",
         "isdigit_l",
         "isfinite",
         "isgraph",
         "isgraph_l",
         "isgreaterequal",
         "isgreater",
         "isinf",
         "islessequal",
         "islessgreater",
         "isless",
         "islower",
         "islower_l",
         "isnan",
         "isnormal",
         "isprint",
         "isprint_l",
         "ispunct",
         "ispunct_l",
         "isspace",
         "isspace_l",
         "isunordered",
         "isupper",
         "isupper_l",
         "iswalnum",
         "iswalnum_l",
         "iswalpha",
         "iswalpha_l",
         "iswblank",
         "iswblank_l",
         "iswcntrl",
         "iswcntrl_l",
         "iswctype",
         "iswctype_l",
         "iswdigit",
         "iswdigit_l",
         "iswgraph",
         "iswgraph_l",
         "iswlower",
         "iswlower_l",
         "iswprint",
         "iswprint_l",
         "iswpunct",
         "iswpunct_l",
         "iswspace",
         "iswspace_l",
         "iswupper",
         "iswupper_l",
         "iswxdigit",
         "iswxdigit_l",
         "isxdigit",
         "isxdigit_l",
         "j0",
         "j1",
         "jn",
         "jrand48",
         "kill",
         "killpg",
         "l64a",
         "labs",
         "lchown",
         "lcong48",
         "ldexpf",
         "ldexp",
         "ldexpl",
         "ldiv",
         "lfind",
         "lgammaf",
         "lgamma",
         "lgammal",
         "linkat",
         "link",
         "lio_listio",
         "listen",
         "llabs",
         "lldiv",
         "llrintf",
         "llrint",
         "llrintl",
         "llroundf",
         "llround",
         "llroundl",
         "localeconv",
         "localtime",
         "localtime_r",
         "lockf",
         "log10f",
         "log10",
         "log10l",
         "log1pf",
         "log1p",
         "log1pl",
         "log2f",
         "log2",
         "log2l",
         "logbf",
         "logb",
         "logbl",
         "logf",
         "log",
         "logl",
         "longjmp",
         "lrand48",
         "lrintf",
         "lrint",
         "lrintl",
         "lroundf",
         "lround",
         "lroundl",
         "lsearch",
         "lseek",
         "lstat",
         "malloc",
         "mblen",
         "mbrlen",
         "mbrtowc",
         "mbsinit",
         "mbsnrtowcs",
         "mbsrtowcs",
         "mbstowcs",
         "mbtowc",
         "memccpy",
         "memchr",
         "memcmp",
         "memcpy",
         "memmove",
         "memset",
         "mkdirat",
         "mkdir",
         "mkdtemp",
         "mkfifoat",
         "mkfifo",
         "mknodat",
         "mknod",
         "mkstemp",
         "mktime",
         "mlockall",
         "mlock",
         "mmap",
         "modff",
         "modf",
         "modfl",
         "mprotect",
         "mq_close",
         "mq_getattr",
         "mq_notify",
         "mq_open",
         "mq_receive",
         "mq_send",
         "mq_setattr",
         "mq_timedreceive",
         "mq_timedsend",
         "mq_unlink",
         "mrand48",
         "msgctl",
         "msgget",
         "msgrcv",
         "msgsnd",
         "msync",
         "munlockall",
         "munlock",
         "munmap",
         "nanf",
         "nan",
         "nanl",
         "nanosleep",
         "nearbyintf",
         "nearbyint",
         "nearbyintl",
         "newlocale",
         "nextafterf",
         "nextafter",
         "nextafterl",
         "nexttowardf",
         "nexttoward",
         "nexttowardl",
         "nftw",
         "nice",
         "nl_langinfo",
         "nl_langinfo_l",
         "nrand48",
         "ntohl",
         "ntohs",
         "openat",
         "opendir",
         "open",
         "openlog",
         "open_memstream",
         "open_wmemstream",
         "pathconf",
         "pause",
         "pclose",
         "perror",
         "pipe",
         "poll",
         "popen",
         "posix_fadvise",
         "posix_fallocate",
         "posix_madvise",
         "posix_memalign",
         "posix_mem_offset",
         "posix_openpt",
         "posix_spawnattr_destroy",
         "posix_spawnattr_getflags",
         "posix_spawnattr_getpgroup",
         "posix_spawnattr_getschedparam",
         "posix_spawnattr_getschedpolicy",
         "posix_spawnattr_getsigdefault",
         "posix_spawnattr_getsigmask",
         "posix_spawnattr_init",
         "posix_spawnattr_setflags",
         "posix_spawnattr_setpgroup",
         "posix_spawnattr_setschedparam",
         "posix_spawnattr_setschedpolicy",
         "posix_spawnattr_setsigdefault",
         "posix_spawnattr_setsigmask",
         "posix_spawn_file_actions_addclose",
         "posix_spawn_file_actions_adddup2",
         "posix_spawn_file_actions_addopen",
         "posix_spawn_file_actions_destroy",
         "posix_spawn_file_actions_init",
         "posix_spawn",
         "posix_spawnp",
         "posix_trace_attr_destroy",
         "posix_trace_attr_getclockres",
         "posix_trace_attr_getcreatetime",
         "posix_trace_attr_getgenversion",
         "posix_trace_attr_getinherited",
         "posix_trace_attr_getlogfullpolicy",
         "posix_trace_attr_getlogsize",
         "posix_trace_attr_getmaxdatasize",
         "posix_trace_attr_getmaxsystemeventsize",
         "posix_trace_attr_getmaxusereventsize",
         "posix_trace_attr_getname",
         "posix_trace_attr_getstreamfullpolicy",
         "posix_trace_attr_getstreamsize",
         "posix_trace_attr_init",
         "posix_trace_attr_setinherited",
         "posix_trace_attr_setlogfullpolicy",
         "posix_trace_attr_setlogsize",
         "posix_trace_attr_setmaxdatasize",
         "posix_trace_attr_setname",
         "posix_trace_attr_setstreamfullpolicy",
         "posix_trace_attr_setstreamsize",
         "posix_trace_clear",
         "posix_trace_close",
         "posix_trace_create",
         "posix_trace_create_withlog",
         "posix_trace_event",
         "posix_trace_eventid_equal",
         "posix_trace_eventid_get_name",
         "posix_trace_eventid_open",
         "posix_trace_eventset_add",
         "posix_trace_eventset_del",
         "posix_trace_eventset_empty",
         "posix_trace_eventset_fill",
         "posix_trace_eventset_ismember",
         "posix_trace_eventtypelist_getnext_id",
         "posix_trace_eventtypelist_rewind",
         "posix_trace_flush",
         "posix_trace_get_attr",
         "posix_trace_get_filter",
         "posix_trace_getnext_event",
         "posix_trace_get_status",
         "posix_trace_open",
         "posix_trace_rewind",
         "posix_trace_set_filter",
         "posix_trace_shutdown",
         "posix_trace_start",
         "posix_trace_stop",
         "posix_trace_timedgetnext_event",
         "posix_trace_trid_eventid_open",
         "posix_trace_trygetnext_event",
         "posix_typed_mem_get_info",
         "posix_typed_mem_open",
         "powf",
         "pow",
         "powl",
         "pread",
         "printf",
         "pselect",
         "psiginfo",
         "psignal",
         "pthread_atfork",
         "pthread_attr_destroy",
         "pthread_attr_getdetachstate",
         "pthread_attr_getguardsize",
         "pthread_attr_getinheritsched",
         "pthread_attr_getschedparam",
         "pthread_attr_getschedpolicy",
         "pthread_attr_getscope",
         "pthread_attr_getstack",
         "pthread_attr_getstacksize",
         "pthread_attr_init",
         "pthread_attr_setdetachstate",
         "pthread_attr_setguardsize",
         "pthread_attr_setinheritsched",
         "pthread_attr_setschedparam",
         "pthread_attr_setschedpolicy",
         "pthread_attr_setscope",
         "pthread_attr_setstack",
         "pthread_attr_setstacksize",
         "pthread_barrierattr_destroy",
         "pthread_barrierattr_getpshared",
         "pthread_barrierattr_init",
         "pthread_barrierattr_setpshared",
         "pthread_barrier_destroy",
         "pthread_barrier_init",
         "pthread_barrier_wait",
         "pthread_cancel",
         "pthread_cleanup_pop",
         "pthread_cleanup_push",
         "pthread_condattr_destroy",
         "pthread_condattr_getclock",
         "pthread_condattr_getpshared",
         "pthread_condattr_init",
         "pthread_condattr_setclock",
         "pthread_condattr_setpshared",
         "pthread_cond_broadcast",
         "pthread_cond_destroy",
         "pthread_cond_init",
         "pthread_cond_signal",
         "pthread_cond_timedwait",
         "pthread_cond_wait",
         "pthread_create",
         "pthread_detach",
         "pthread_equal",
         "pthread_exit",
         "pthread_getconcurrency",
         "pthread_getcpuclockid",
         "pthread_getschedparam",
         "pthread_getspecific",
         "pthread_join",
         "pthread_key_create",
         "pthread_key_delete",
         "pthread_kill",
         "pthread_mutexattr_destroy",
         "pthread_mutexattr_getprioceiling",
         "pthread_mutexattr_getprotocol",
         "pthread_mutexattr_getpshared",
         "pthread_mutexattr_getrobust",
         "pthread_mutexattr_gettype",
         "pthread_mutexattr_init",
         "pthread_mutexattr_setprioceiling",
         "pthread_mutexattr_setprotocol",
         "pthread_mutexattr_setpshared",
         "pthread_mutexattr_setrobust",
         "pthread_mutexattr_settype",
         "pthread_mutex_consistent",
         "pthread_mutex_destroy",
         "pthread_mutex_getprioceiling",
         "pthread_mutex_init",
         "pthread_mutex_lock",
         "pthread_mutex_setprioceiling",
         "pthread_mutex_timedlock",
         "pthread_mutex_trylock",
         "pthread_mutex_unlock",
         "pthread_once",
         "pthread_rwlockattr_destroy",
         "pthread_rwlockattr_getpshared",
         "pthread_rwlockattr_init",
         "pthread_rwlockattr_setpshared",
         "pthread_rwlock_destroy",
         "pthread_rwlock_init",
         "pthread_rwlock_rdlock",
         "pthread_rwlock_timedrdlock",
         "pthread_rwlock_timedwrlock",
         "pthread_rwlock_tryrdlock",
         "pthread_rwlock_trywrlock",
         "pthread_rwlock_unlock",
         "pthread_rwlock_wrlock",
         "pthread_self",
         "pthread_setcancelstate",
         "pthread_setcanceltype",
         "pthread_setconcurrency",
         "pthread_setschedparam",
         "pthread_setschedprio",
         "pthread_setspecific",
         "pthread_sigmask",
         "pthread_spin_destroy",
         "pthread_spin_init",
         "pthread_spin_lock",
         "pthread_spin_trylock",
         "pthread_spin_unlock",
         "pthread_testcancel",
         "ptsname",
         "putchar",
         "putchar_unlocked",
         "putc",
         "putc_unlocked",
         "putenv",
         "putmsg",
         "putpmsg",
         "puts",
         "pututxline",
         "putwchar",
         "putwc",
         "pwrite",
         "qsort",
         "raise",
         "rand",
         "random",
         "rand_r",
         "readdir",
         "readdir_r",
         "read",
         "readlinkat",
         "readlink",
         "readv",
         "realloc",
         "realpath",
         "recvfrom",
         "recv",
         "recvmsg",
         "regcomp",
         "regerror",
         "regexec",
         "regfree",
         "remainderf",
         "remainder",
         "remainderl",
         "remove",
         "remque",
         "remquof",
         "remquo",
         "remquol",
         "renameat",
         "rename",
         "rewinddir",
         "rewind",
         "rintf",
         "rint",
         "rintl",
         "rmdir",
         "roundf",
         "round",
         "roundl",
         "scalblnf",
         "scalbln",
         "scalblnl",
         "scalbnf",
         "scalbn",
         "scalbnl",
         "scandir",
         "scanf",
         "sched_getparam",
         "sched_get_priority_max",
         "sched_get_priority_min",
         "sched_getscheduler",
         "sched_rr_get_interval",
         "sched_setparam",
         "sched_setscheduler",
         "sched_yield",
         "seed48",
         "seekdir",
         "select",
         "sem_close",
         "semctl",
         "sem_destroy",
         "semget",
         "sem_getvalue",
         "sem_init",
         "sem_open",
         "semop",
         "sem_post",
         "sem_timedwait",
         "sem_trywait",
         "sem_unlink",
         "sem_wait",
         "send",
         "sendmsg",
         "sendto",
         "setbuf",
         "setegid",
         "setenv",
         "seteuid",
         "setgid",
         "setgrent",
         "sethostent",
         "setitimer",
         "setjmp",
         "setkey",
         "setlocale",
         "setlogmask",
         "setnetent",
         "setpgid",
         "setpgrp",
         "setpriority",
         "setprotoent",
         "setpwent",
         "setregid",
         "setreuid",
         "setrlimit",
         "setservent",
         "setsid",
         "setsockopt",
         "setstate",
         "setuid",
         "setutxent",
         "setvbuf",
         "shmat",
         "shmctl",
         "shmdt",
         "shmget",
         "shm_open",
         "shm_unlink",
         "shutdown",
         "sigaction",
         "sigaddset",
         "sigaltstack",
         "sigdelset",
         "sigemptyset",
         "sigfillset",
         "sighold",
         "sigignore",
         "siginterrupt",
         "sigismember",
         "siglongjmp",
         "signal",
         "signbit",
         "sigpause",
         "sigpending",
         "sigprocmask",
         "sigqueue",
         "sigrelse",
         "sigset",
         "sigsetjmp",
         "sigsuspend",
         "sigtimedwait",
         "sigwait",
         "sigwaitinfo",
         "sinf",
         "sinhf",
         "sinh",
         "sinhl",
         "sin",
         "sinl",
         "sleep",
         "snprintf",
         "sockatmark",
         "socket",
         "socketpair",
         "sprintf",
         "sqrtf",
         "sqrt",
         "sqrtl",
         "srand48",
         "srand",
         "srandom",
         "sscanf",
         "stat",
         "statvfs",
         "stpcpy",
         "stpncpy",
         "strcasecmp",
         "strcasecmp_l",
         "strcat",
         "strchr",
         "strcmp",
         "strcoll",
         "strcoll_l",
         "strcpy",
         "strcspn",
         "strdup",
         "strerror",
         "strerror_l",
         "strerror_r",
         "strfmon",
         "strfmon_l",
         "strftime",
         "strftime_l",
         "strlen",
         "strncasecmp",
         "strncasecmp_l",
         "strncat",
         "strncmp",
         "strncpy",
         "strndup",
         "strnlen",
         "strpbrk",
         "strptime",
         "strrchr",
         "strsignal",
         "strspn",
         "strstr",
         "strtod",
         "strtof",
         "strtoimax",
         "strtok",
         "strtok_r",
         "strtold",
         "strtol",
         "strtoll",
         "strtoul",
         "strtoull",
         "strtoumax",
         "strxfrm",
         "strxfrm_l",
         "swab",
         "swprintf",
         "swscanf",
         "symlinkat",
         "symlink",
         "sync",
         "sysconf",
         "syslog",
         "system",
         "tanf",
         "tanhf",
         "tanh",
         "tanhl",
         "tan",
         "tanl",
         "tcdrain",
         "tcflow",
         "tcflush",
         "tcgetattr",
         "tcgetpgrp",
         "tcgetsid",
         "tcsendbreak",
         "tcsetattr",
         "tcsetpgrp",
         "tdelete",
         "telldir",
         "tempnam",
         "tfind",
         "tgammaf",
         "tgamma",
         "tgammal",
         "time",
         "timer_create",
         "timer_delete",
         "timer_getoverrun",
         "timer_gettime",
         "timer_settime",
         "times",
         "tmpfile",
         "tmpnam",
         "toascii",
         "tolower",
         "tolower_l",
         "toupper",
         "toupper_l",
         "towctrans",
         "towctrans_l",
         "towlower",
         "towlower_l",
         "towupper",
         "towupper_l",
         "truncate",
         "truncf",
         "trunc",
         "truncl",
         "tsearch",
         "ttyname",
         "ttyname_r",
         "twalk",
         "tzset",
         "ulimit",
         "umask",
         "uname",
         "ungetc",
         "ungetwc",
         "unlinkat",
         "unlink",
         "unlockpt",
         "unsetenv",
         "uselocale",
         "utime",
         "utimensat",
         "utimes",
         "va_arg",
         "va_copy",
         "va_end",
         "va_start",
         "vdprintf",
         "vfprintf",
         "vfscanf",
         "vfwprintf",
         "vfwscanf",
         "vprintf",
         "vscanf",
         "vsnprintf",
         "vsprintf",
         "vsscanf",
         "vswprintf",
         "vswscanf",
         "vwprintf",
         "vwscanf",
         "wait",
         "waitid",
         "waitpid",
         "wcpcpy",
         "wcpncpy",
         "wcrtomb",
         "wcscasecmp",
         "wcscasecmp_l",
         "wcscat",
         "wcschr",
         "wcscmp",
         "wcscoll",
         "wcscoll_l",
         "wcscpy",
         "wcscspn",
         "wcsdup",
         "wcsftime",
         "wcslen",
         "wcsncasecmp",
         "wcsncasecmp_l",
         "wcsncat",
         "wcsncmp",
         "wcsncpy",
         "wcsnlen",
         "wcsnrtombs",
         "wcspbrk",
         "wcsrchr",
         "wcsrtombs",
         "wcsspn",
         "wcsstr",
         "wcstod",
         "wcstof",
         "wcstoimax",
         "wcstok",
         "wcstold",
         "wcstol",
         "wcstoll",
         "wcstombs",
         "wcstoul",
         "wcstoull",
         "wcstoumax",
         "wcswidth",
         "wcsxfrm",
         "wcsxfrm_l",
         "wctob",
         "wctomb",
         "wctrans",
         "wctrans_l",
         "wctype",
         "wctype_l",
         "wcwidth",
         "wmemchr",
         "wmemcmp",
         "wmemcpy",
         "wmemmove",
         "wmemset",
         "wordexp",
         "wordfree",
         "wprintf",
         "write",
         "writev",
         "wscanf",
         "y0",
         "y1",
         "yn",
         "usleep", ## removed in POSIX.1-2008
         "gethostbyname",
         "gethostbyaddr"
         ]

gnuextensionsfunctions = ["gethostent_r",
                          "gethostbyaddr_r",
                          "gethostbyname_r",
                          "gethostbyname2_r",
                          "gethostbyname2",
                          "getmntent_r",
                          "getopt_long",
                          "getopt_long_only",
                          "mempcpy",
                          "wmempcpy",
                          "strchrnul",
                          "asprintf",
                          "vasprintf"
                          ]

bsdfunctions = ["daemon",
                "initgroups",
                "chroot",
                "setgroups",
                "on_exit",
                "getmntent",
                "setmntent",
                "addmntent",
                "endmntent",
                "hasmntopt",
                "ether_aton",
                "sethostname",
                "vfork",
                "strsep",
                "settimeofday",
                "wait3",
                "wait4",
                "syscall",
               ]

linuxfunctions = ["sysinfo",
                  "ptsname_r",
                  "clone",
                  "adjtimex",
                  "reboot",
                  "syslog",
                  "klogctl",
                  "statfs",
                  "fstatfs",
                  "mount",
                  "umount",
                  "umount2",
                 ]

susfunctions = ["getpagesize"]

glibcfunctions = ["getpt"]

## inserted by GCC
gccfunctions = ["__deregister_frame_info",
                "__register_frame_info",
               ]

#http://refspecs.linuxfoundation.org/LSB_3.2.0/LSB-Core-generic/LSB-Core-generic/libcman.html
lsbfunctions = ["__cxa_finalize",
                "__cxa_atexit",
                "__errno_location",
                "__h_errno_location",
                "__sigsetjmp",
               ]

sysvfunctions = ["getutent", "getutid", "getutline", "pututline", "setutent", "endutent", "utmpname", "stime"]

#XDR: External Data Representation Standard, RFC 1014
xdrfunctions = []

miscfunctions = ["inet_aton",
                 "vsyslog",
                 "setbuffer",
                 "setlinebuf",
                 "updwtmp",
                 "getdomainname",
                 "setdomainname",
                 "herror",
                 "hstrerror",
                 "clearenv"
                 "bindresvport"
                ]

allfunctions = posixfunctions + gnuextensionsfunctions + bsdfunctions + linuxfunctions + sysvfunctions + glibcfunctions + gccfunctions + lsbfunctions + susfunctions + xdrfunctions + miscfunctions

posixvars = ["daylight",
    "environ",
    "errno",
    "getdate_err",
    "optarg",
    "opterr",
    "optind",
    "optopt",
    "signgam",
    "stderr",
    "stdin",
    "stdout",
    "timezone",
    "tzname"]

lsbvars = ["__environ"]

allvars = posixvars + lsbvars
