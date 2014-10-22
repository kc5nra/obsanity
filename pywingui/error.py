# error.py
# Copyright (c) 2012 Maxim Kolosov

NO_ERROR = 0
ERROR_INVALID_FUNCTION = 1
ERROR_FILE_NOT_FOUND = 2
ERROR_PATH_NOT_FOUND = 3
ERROR_TOO_MANY_OPEN_FILES = 4
ERROR_ACCESS_DENIED = 5
ERROR_INVALID_HANDLE = 6
ERROR_ARENA_TRASHED = 7
ERROR_NOT_ENOUGH_MEMORY = 8
ERROR_INVALID_BLOCK = 9
ERROR_BAD_ENVIRONMENT = 10
ERROR_BAD_FORMAT = 11
ERROR_INVALID_ACCESS = 12
ERROR_INVALID_DATA = 13
ERROR_INVALID_DRIVE = 15
ERROR_CURRENT_DIRECTORY = 16
ERROR_NOT_SAME_DEVICE = 17
ERROR_NO_MORE_FILES = 18
ERROR_WRITE_PROTECT = 19
ERROR_BAD_UNIT = 20
ERROR_NOT_READY = 21
ERROR_BAD_COMMAND = 22
ERROR_CRC = 23
ERROR_BAD_LENGTH = 24
ERROR_SEEK = 25
ERROR_NOT_DOS_DISK = 26
ERROR_SECTOR_NOT_FOUND = 27
ERROR_OUT_OF_PAPER = 28
ERROR_WRITE_FAULT = 29
ERROR_READ_FAULT = 30
ERROR_GEN_FAILURE = 31
ERROR_SHARING_VIOLATION = 32
ERROR_LOCK_VIOLATION = 33
ERROR_WRONG_DISK = 34
ERROR_FCB_UNAVAILABLE = 35
ERROR_SHARING_BUFFER_EXCEEDED = 36
ERROR_NOT_SUPPORTED = 50
ERROR_REM_NOT_LIST = 51
ERROR_DUP_NAME = 52
ERROR_BAD_NETPATH = 53
ERROR_NETWORK_BUSY = 54
ERROR_DEV_NOT_EXIST = 55
ERROR_TOO_MANY_CMDS = 56
ERROR_ADAP_HDW_ERR = 57
ERROR_BAD_NET_RESP = 58
ERROR_UNEXP_NET_ERR = 59
ERROR_BAD_REM_ADAP = 60
ERROR_PRINTQ_FULL = 61
ERROR_NO_SPOOL_SPACE = 62
ERROR_PRINT_CANCELLED = 63
ERROR_NETNAME_DELETED = 64
ERROR_NETWORK_ACCESS_DENIED = 65
ERROR_BAD_DEV_TYPE = 66
ERROR_BAD_NET_NAME = 67
ERROR_TOO_MANY_NAMES = 68
ERROR_TOO_MANY_SESS = 69
ERROR_SHARING_PAUSED = 70
ERROR_REQ_NOT_ACCEP = 71
ERROR_REDIR_PAUSED = 72
ERROR_FILE_EXISTS = 80
ERROR_DUP_FCB = 81
ERROR_CANNOT_MAKE = 82
ERROR_FAIL_I24 = 83
ERROR_OUT_OF_STRUCTURES = 84
ERROR_ALREADY_ASSIGNED = 85
ERROR_INVALID_PASSWORD = 86
ERROR_INVALID_PARAMETER = 87
ERROR_NET_WRITE_FAULT = 88
ERROR_NO_PROC_SLOTS = 89
ERROR_NOT_FROZEN = 90
ERR_TSTOVFL = 91
ERR_TSTDUP = 92
ERROR_NO_ITEMS = 93
ERROR_INTERRUPT = 95
ERROR_TOO_MANY_SEMAPHORES = 100
ERROR_EXCL_SEM_ALREADY_OWNED = 101
ERROR_SEM_IS_SET = 102
ERROR_TOO_MANY_SEM_REQUESTS = 103
ERROR_INVALID_AT_INTERRUPT_TIME = 104
ERROR_SEM_OWNER_DIED = 105
ERROR_SEM_USER_LIMIT = 106
ERROR_DISK_CHANGE = 107
ERROR_DRIVE_LOCKED = 108
ERROR_BROKEN_PIPE = 109
ERROR_OPEN_FAILED = 110
ERROR_BUFFER_OVERFLOW = 111
ERROR_DISK_FULL = 112
ERROR_NO_MORE_SEARCH_HANDLES = 113
ERROR_INVALID_TARGET_HANDLE = 114
ERROR_PROTECTION_VIOLATION = 115
ERROR_VIOKBD_REQUEST = 116
ERROR_INVALID_CATEGORY = 117
ERROR_INVALID_VERIFY_SWITCH = 118
ERROR_BAD_DRIVER_LEVEL = 119
ERROR_CALL_NOT_IMPLEMENTED = 120
ERROR_SEM_TIMEOUT = 121
ERROR_INSUFFICIENT_BUFFER = 122
ERROR_INVALID_NAME = 123
ERROR_INVALID_LEVEL = 124
ERROR_NO_VOLUME_LABEL = 125
ERROR_MOD_NOT_FOUND = 126
ERROR_PROC_NOT_FOUND = 127
ERROR_WAIT_NO_CHILDREN = 128
ERROR_CHILD_NOT_COMPLETE = 129
ERROR_DIRECT_ACCESS_HANDLE = 130
ERROR_NEGATIVE_SEEK = 131
ERROR_SEEK_ON_DEVICE = 132
ERROR_IS_JOIN_TARGET = 133
ERROR_IS_JOINED = 134
ERROR_IS_SUBSTED = 135
ERROR_NOT_JOINED = 136
ERROR_NOT_SUBSTED = 137
ERROR_JOIN_TO_JOIN = 138
ERROR_SUBST_TO_SUBST = 139
ERROR_JOIN_TO_SUBST = 140
ERROR_SUBST_TO_JOIN = 141
ERROR_BUSY_DRIVE = 142
ERROR_SAME_DRIVE = 143
ERROR_DIR_NOT_ROOT = 144
ERROR_DIR_NOT_EMPTY = 145
ERROR_IS_SUBST_PATH = 146
ERROR_IS_JOIN_PATH = 147
ERROR_PATH_BUSY = 148
ERROR_IS_SUBST_TARGET = 149
ERROR_SYSTEM_TRACE = 150
ERROR_INVALID_EVENT_COUNT = 151
ERROR_TOO_MANY_MUXWAITERS = 152
ERROR_INVALID_LIST_FORMAT = 153
ERROR_LABEL_TOO_LONG = 154
ERROR_TOO_MANY_TCBS = 155
ERROR_SIGNAL_REFUSED = 156
ERROR_DISCARDED = 157
ERROR_NOT_LOCKED = 158
ERROR_BAD_THREADID_ADDR = 159
ERROR_BAD_ARGUMENTS = 160
ERROR_BAD_PATHNAME = 161
ERROR_SIGNAL_PENDING = 162
ERROR_UNCERTAIN_MEDIA = 163
ERROR_MAX_THRDS_REACHED = 164
ERROR_MONITORS_NOT_SUPPORTED = 165
ERROR_LOCK_FAILED = 167
ERROR_BUSY = 170
ERROR_DEVICE_SUPPORT_IN_PROGRESS = 171
ERROR_CANCEL_VIOLATION = 173
ERROR_ATOMIC_LOCKS_NOT_SUPPORTED = 174
ERROR_INVALID_SEGMENT_NUMBER = 180
ERROR_INVALID_CALLGATE = 181
ERROR_INVALID_ORDINAL = 182
ERROR_ALREADY_EXISTS = 183
ERROR_NO_CHILD_PROCESS = 184
ERROR_CHILD_ALIVE_NOWAIT = 185
ERROR_INVALID_FLAG_NUMBER = 186
ERROR_SEM_NOT_FOUND = 187
ERROR_INVALID_STARTING_CODESEG = 188
ERROR_INVALID_STACKSEG = 189
ERROR_INVALID_MODULETYPE = 190
ERROR_INVALID_EXE_SIGNATURE = 191
ERROR_EXE_MARKED_INVALID = 192
ERROR_BAD_EXE_FORMAT = 193
ERROR_ITERATED_DATA_EXCEEDS_64k = 194
ERROR_INVALID_MINALLOCSIZE = 195
ERROR_DYNLINK_FROM_INVALID_RING = 196
ERROR_IOPL_NOT_ENABLED = 197
ERROR_INVALID_SEGDPL = 198
ERROR_AUTODATASEG_EXCEEDS_64k = 199
ERROR_RING2SEG_MUST_BE_MOVABLE = 200
ERROR_RELOC_CHAIN_XEEDS_SEGLIM = 201
ERROR_INFLOOP_IN_RELOC_CHAIN = 202
ERROR_ENVVAR_NOT_FOUND = 203
ERROR_NOT_CURRENT_CTRY = 204
ERROR_NO_SIGNAL_SENT = 205
ERROR_FILENAME_EXCED_RANGE = 206
ERROR_RING2_STACK_IN_USE = 207
ERROR_META_EXPANSION_TOO_LONG = 208
ERROR_INVALID_SIGNAL_NUMBER = 209
ERROR_THREAD_1_INACTIVE = 210
ERROR_INFO_NOT_AVAIL = 211
ERROR_LOCKED = 212
ERROR_BAD_DYNALINK = 213
ERROR_TOO_MANY_MODULES = 214
ERROR_NESTING_NOT_ALLOWED = 215
ERROR_NO_DATA = 232
ERROR_PIPE_NOT_CONNECTED = 233
ERROR_MORE_DATA = 234
ERROR_VC_DISCONNECTED = 240
ERROR_INVALID_EA_NAME = 254
ERROR_EA_LIST_INCONSISTENT = 255
WAIT_TIMEOUT = 258
ERROR_NO_MORE_ITEMS = 259

ERROR_INVALID_ADDRESS = 487

ERROR_BAD_DEVICE = 1200
ERROR_CONNECTION_UNAVAIL = 1201
ERROR_DEVICE_ALREADY_REMEMBERED = 1202
ERROR_NO_NET_OR_BAD_PATH = 1203
ERROR_BAD_PROVIDER = 1204
ERROR_CANNOT_OPEN_PROFILE = 1205
ERROR_BAD_PROFILE = 1206
ERROR_NOT_CONTAINER = 1207
ERROR_EXTENDED_ERROR = 1208
ERROR_INVALID_GROUPNAME = 1209
ERROR_INVALID_COMPUTERNAME = 1210
ERROR_INVALID_EVENTNAME = 1211
ERROR_INVALID_DOMAINNAME = 1212
ERROR_INVALID_SERVICENAME = 1213
ERROR_INVALID_NETNAME = 1214
ERROR_INVALID_SHARENAME = 1215
ERROR_INVALID_PASSWORDNAME = 1216
ERROR_INVALID_MESSAGENAME = 1217
ERROR_INVALID_MESSAGEDEST = 1218
ERROR_SESSION_CREDENTIAL_CONFLICT = 1219
ERROR_REMOTE_SESSION_LIMIT_EXCEEDED = 1220
ERROR_DUP_DOMAINNAME = 1221
ERROR_NO_NETWORK = 1222
ERROR_CANCELLED = 1223
ERROR_USER_MAPPED_FILE = 1224
ERROR_CONNECTION_REFUSED = 1225
ERROR_GRACEFUL_DISCONNECT = 1226
ERROR_ADDRESS_ALREADY_ASSOCIATED = 1227
ERROR_ADDRESS_NOT_ASSOCIATED = 1228
ERROR_CONNECTION_INVALID = 1229
ERROR_CONNECTION_ACTIVE = 1230
ERROR_NETWORK_UNREACHABLE = 1231
ERROR_HOST_UNREACHABLE = 1232
ERROR_PROTOCOL_UNREACHABLE = 1233
ERROR_PORT_UNREACHABLE = 1234
ERROR_REQUEST_ABORTED = 1235
ERROR_CONNECTION_ABORTED = 1236
ERROR_RETRY = 1237
ERROR_CONNECTION_COUNT_LIMIT = 1238
ERROR_LOGIN_TIME_RESTRICTION = 1239
ERROR_LOGIN_WKSTA_RESTRICTION = 1240
ERROR_INCORRECT_ADDRESS = 1241
ERROR_ALREADY_REGISTERED = 1242
ERROR_SERVICE_NOT_FOUND = 1243
ERROR_NOT_AUTHENTICATED = 1244
ERROR_NOT_LOGGED_ON = 1245
ERROR_CONTINUE = 1246
ERROR_ALREADY_INITIALIZED = 1247
ERROR_NO_MORE_DEVICES = 1248
ERROR_NO_SUCH_SITE = 1249
ERROR_DOMAIN_CONTROLLER_EXISTS = 1250
ERROR_ONLY_IF_CONNECTED = 1251
ERROR_OVERRIDE_NOCHANGES = 1252
ERROR_BAD_USER_PROFILE = 1253
ERROR_NOT_SUPPORTED_ON_SBS = 1254
ERROR_SERVER_SHUTDOWN_IN_PROGRESS = 1255
ERROR_HOST_DOWN = 1256
ERROR_NON_ACCOUNT_SID = 1257
ERROR_NON_DOMAIN_SID = 1258
ERROR_APPHELP_BLOCK = 1259
ERROR_ACCESS_DISABLED_BY_POLICY = 1260
ERROR_REG_NAT_CONSUMPTION = 1261
ERROR_CSCSHARE_OFFLINE = 1262
ERROR_PKINIT_FAILURE = 1263
ERROR_SMARTCARD_SUBSYSTEM_FAILURE = 1264
ERROR_DOWNGRADE_DETECTED = 1265
ERROR_MACHINE_LOCKED = 1271
ERROR_CALLBACK_SUPPLIED_INVALID_DATA = 1273
ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED = 1274
ERROR_DRIVER_BLOCKED = 1275
ERROR_INVALID_IMPORT_OF_NON_DLL = 1276
ERROR_ACCESS_DISABLED_WEBBLADE = 1277
ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER = 1278
ERROR_RECOVERY_FAILURE = 1279
ERROR_ALREADY_FIBER = 1280
ERROR_ALREADY_THREAD = 1281
ERROR_STACK_BUFFER_OVERRUN = 1282
ERROR_PARAMETER_QUOTA_EXCEEDED = 1283
ERROR_DEBUGGER_INACTIVE = 1284
ERROR_DELAY_LOAD_FAILED = 1285
ERROR_VDM_DISALLOWED = 1286
ERROR_UNIDENTIFIED_ERROR = 1287
ERROR_INVALID_CRUNTIME_PARAMETER = 1288
ERROR_BEYOND_VDL = 1289
ERROR_INCOMPATIBLE_SERVICE_SID_TYPE = 1290
ERROR_DRIVER_PROCESS_TERMINATED = 1291
ERROR_IMPLEMENTATION_LIMIT = 1292
ERROR_PROCESS_IS_PROTECTED = 1293
ERROR_SERVICE_NOTIFY_CLIENT_LAGGING = 1294
ERROR_DISK_QUOTA_EXCEEDED = 1295
ERROR_CONTENT_BLOCKED = 1296
ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE = 1297
ERROR_APP_HANG = 1298
ERROR_INVALID_LABEL = 1299
ERROR_NOT_ALL_ASSIGNED = 1300
ERROR_SOME_NOT_MAPPED = 1301
ERROR_NO_QUOTAS_FOR_ACCOUNT = 1302
ERROR_LOCAL_USER_SESSION_KEY = 1303
ERROR_NULL_LM_PASSWORD = 1304
ERROR_UNKNOWN_REVISION = 1305
ERROR_REVISION_MISMATCH = 1306
ERROR_INVALID_OWNER = 1307
ERROR_INVALID_PRIMARY_GROUP = 1308
ERROR_NO_IMPERSONATION_TOKEN = 1309
ERROR_CANT_DISABLE_MANDATORY = 1310
ERROR_NO_LOGON_SERVERS = 1311
ERROR_NO_SUCH_LOGON_SESSION = 1312
ERROR_NO_SUCH_PRIVILEGE = 1313
ERROR_PRIVILEGE_NOT_HELD = 1314
ERROR_INVALID_ACCOUNT_NAME = 1315
ERROR_USER_EXISTS = 1316
ERROR_NO_SUCH_USER = 1317
ERROR_GROUP_EXISTS = 1318
ERROR_NO_SUCH_GROUP = 1319
ERROR_MEMBER_IN_GROUP = 1320

ERROR_INVALID_TRANSFORM = 2020
ERROR_COLORSPACE_MISMATCH = 2021
ERROR_INVALID_COLORINDEX = 2022
ERROR_PROFILE_DOES_NOT_MATCH_DEVICE = 2023
ERROR_CONNECTED_OTHER_PASSWORD = 2108
ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT = 2109
ERROR_BAD_USERNAME = 2202
ERROR_NOT_CONNECTED = 2250
ERROR_OPEN_FILES = 2401
ERROR_ACTIVE_CONNECTIONS = 2402
ERROR_DEVICE_IN_USE = 2404

ERROR_USER_DEFINED_BASE = 0xF000

ERROR_I24_WRITE_PROTECT = 0
ERROR_I24_BAD_UNIT = 1
ERROR_I24_NOT_READY = 2
ERROR_I24_BAD_COMMAND = 3
ERROR_I24_CRC = 4
ERROR_I24_BAD_LENGTH = 5
ERROR_I24_SEEK = 6
ERROR_I24_NOT_DOS_DISK = 7
ERROR_I24_SECTOR_NOT_FOUND = 8
ERROR_I24_OUT_OF_PAPER = 9
ERROR_I24_WRITE_FAULT = 0x0A
ERROR_I24_READ_FAULT = 0x0B
ERROR_I24_GEN_FAILURE = 0x0C
ERROR_I24_DISK_CHANGE = 0x0D
ERROR_I24_WRONG_DISK = 0x0F
ERROR_I24_UNCERTAIN_MEDIA = 0x10
ERROR_I24_CHAR_CALL_INTERRUPTED = 0x11
ERROR_I24_NO_MONITOR_SUPPORT = 0x12
ERROR_I24_INVALID_PARAMETER = 0x13
ALLOWED_FAIL = 0x0001
ALLOWED_ABORT = 0x0002
ALLOWED_RETRY = 0x0004
ALLOWED_IGNORE = 0x0008
I24_OPERATION = 0x1
I24_AREA = 0x6
I24_CLASS = 0x80
ERRCLASS_OUTRES = 1
ERRCLASS_TEMPSIT = 2
ERRCLASS_AUTH = 3
ERRCLASS_INTRN = 4
ERRCLASS_HRDFAIL = 5
ERRCLASS_SYSFAIL = 6
ERRCLASS_APPERR = 7
ERRCLASS_NOTFND = 8
ERRCLASS_BADFMT = 9
ERRCLASS_LOCKED = 10
ERRCLASS_MEDIA = 11
ERRCLASS_ALREADY = 12
ERRCLASS_UNK = 13
ERRCLASS_CANT = 14
ERRCLASS_TIME = 15
ERRACT_RETRY = 1
ERRACT_DLYRET = 2
ERRACT_USER = 3
ERRACT_ABORT = 4
ERRACT_PANIC = 5
ERRACT_IGNORE = 6
ERRACT_INTRET = 7
ERRLOC_UNK = 1
ERRLOC_DISK = 2
ERRLOC_NET = 3
ERRLOC_SERDEV = 4
ERRLOC_MEM = 5
TC_NORMAL = 0
TC_HARDERR = 1
TC_GP_TRAP = 2
TC_SIGNAL = 3
