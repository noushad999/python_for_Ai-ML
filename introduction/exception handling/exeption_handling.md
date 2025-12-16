## 1) Error, Bug, Exception — difference ta exactly ki?

### ✅ Error (general meaning)

- “Error” মানে code/logic/inputs/environment এ এমন একটা সমস্যা যেটা program কে
  expected behavior দিতে দেয় না। [web:21]
- Error শব্দটা broad: syntax error থেকে শুরু করে runtime failure, wrong
  output—সবই daily কথায় “error” বলা হয়। [web:21]

### ✅ Bug (software engineering term)

- Bug মানে software defect: code run হলেও wrong result, crash, security
  issue—যেকোন defect। [web:21]
- Bug fix করার process = debugging (reproduce → isolate → fix → test). [web:21]

### ✅ Exception (Python specific)

- Python এ exception হচ্ছে runtime এ ওঠা একটা event যা normal control flow
  থামায়, আর handle না করলে program error দেখিয়ে terminate করতে পারে।
  [web:21][web:23]
- Exception হলো Python-এর structured way to signal runtime problems (file
  missing, invalid int conversion, network failure, etc.). [web:23]

---

## 2) Error types — 3 category (exam + interview + real life)

### 2.1 Syntax / Parse-time error (compile-time type)

- Code run হওয়ার আগেই Python parser ধরে ফেলে। [web:21]
- Example: missing parenthesis.
  ```
  print("hello"
  ```
- কেন `try/except` দিয়ে ধরা যায় না?
  - কারণ program execute শুরুই হয় না, তাই `try` block এ ঢোকার সুযোগ নেই।
    [web:21]

### 2.2 Runtime errors (exceptions)

- Program চলাকালে কোনো invalid condition হলে Python exception তোলে।
  [web:21][web:23]
- Example: division by zero.
  ```
  a = 10
  b = 0
  a / b   # ZeroDivisionError
  ```
- এগুলা `try/except` দিয়ে handle করা যায়, তাই production code এ এটা সবচেয়ে
  গুরুত্বপূর্ণ। [web:21]

### 2.3 Logical errors

- Program crash করে না, কিন্তু output wrong. [web:21]
- Example: wrong formula/assumption.
  ```
  def area(r):
      return 3.14 * r * r   # maybe should be math.pi
  ```
- Logical error fix করতে exception handling না—debugging, tests, code review
  লাগে। [web:21]

---

## 3) Python exception system — essential mental model

### 3.1 “Raise” vs “Catch”

- **Raise**: problem detect করলে exception তোলা (signal). [web:21]
- **Catch**: `except` দিয়ে handle করা (recover / fallback / message / cleanup).
  [web:21]

### 3.2 Propagation (bubble up)

- Function A তে exception হলে A handle না করলে caller (Function B) এর দিকে
  propagate হয়। [web:21]
- এটাই reason: low-level function এ সব exception swallow করা dangerous, কারণ
  real bug hide হয়ে যায়। [web:27]

### 3.3 Traceback (why it’s valuable)

- Traceback দেখায় কোন line → কোন function call chain দিয়ে error এসেছে। [web:21]
- Traceback এর bottom line সাধারণত final exception type/message দেয়; উপরের দিক
  call history। [web:21]

---

## 4) try/except/else/finally — deep explanation

### 4.1 `try` block (small রাখার rule)

- `try` এর ভিতরে শুধু সেই statement গুলো রাখুন যেগুলো “risky”। [web:27]
- Small try block মানে: unexpected line থেকে exception উঠলে accidental handling
  কম হয়। [web:27]

### 4.2 `except` blocks (order matters)

- Python প্রথম matching `except` এ ঢুকে যায়। [web:21]
- Specific exceptions আগে, broad exceptions পরে।
  - Good:
    ```
    try:
        ...
    except FileNotFoundError:
        ...
    except OSError:
        ...
    ```
- Bad: আগে broad ধরলে later specific unreachable হতে পারে (maintainability
  issue). [web:27]

### 4.3 `else` block (clean success path)

- `else` runs only if `try` এর ভিতরে কোনো exception হয়নি। [web:21]
- কেন useful?
  - Success-path logic `try` থেকে আলাদা থাকে → readability improves. [web:21]

### 4.4 `finally` block (guaranteed cleanup)

- `finally` runs no matter what: exception হোক বা না হোক। [web:21]
- Use cases:
  - file close
  - lock release
  - temp cleanup
  - “finish message”
- But: modern Python এ resource management এ `with`/context manager বেশি clean
  (still `finally` knowledge mandatory). [web:21]

---

## 5) Built-in exceptions — meaning বুঝলে debugging speed 2x

### 5.1 Very common ones

- `ValueError`: type ঠিক, কিন্তু value invalid (e.g., `"abc"` to `int`).
  [web:23]
- `TypeError`: wrong type operation (e.g., `"10" + 5`). [web:23]
- `KeyError`: dict key missing. [web:23]
- `IndexError`: list index invalid. [web:23]
- `FileNotFoundError`: file missing. [web:23]
- `OSError`: OS-level errors (permissions, IO issues); many file-related issues
  come from here. [web:23]
- `ZeroDivisionError`: division by 0. [web:23]

### 5.2 Exception hierarchy idea (why it matters)

- Built-in exceptions are structured; catching the right level prevents
  over-catching and hiding bugs। [web:23][web:27]
- PEP 8 advises avoiding bare `except:` and being careful with broad catches.
  [web:27]

---

## 6) Best practices (PEP 8 aligned) — “production rules”

### 6.1 Avoid `except:`

- Bare `except:` catches too much (including exit/interrupt signals) and can
  make program behavior weird. [web:27]
- Better: `except Exception:` (still broad) or specific exceptions. [web:27]

### 6.2 Don’t swallow exceptions silently

- “pass” করে ignore করলে debugging nightmare হয়। [web:27]
- If ignoring intentionally, make it explicit (see `contextlib.suppress`).
  [web:19][web:27]

### 6.3 Make error messages actionable

- Message should say:
  - what went wrong
  - which input/value caused it
  - how to fix (if user-facing)
- For libraries, prefer precise exception type + concise message. [web:27]

---

## 7) Raising exceptions — clean validation & fail-fast

### 7.1 Use `raise` for invalid state/input

```
def set_age(age: int) -> None:
    if age < 0:
        raise ValueError("age must be non-negative")
```

- This is better than returning special values everywhere because caller can
  handle it centrally. [web:21][web:23]

### 7.2 Re-raise after logging (don’t hide bugs)

```
import logging
log = logging.getLogger(__name__)

def run():
    try:
        risky()
    except Exception:
        log.exception("Unexpected failure")
        raise
```

- Logging + re-raise keeps the failure visible while preserving traceback.
  [web:27][web:21]

---

## 8) Custom exceptions — clean architecture pattern

### 8.1 Why custom exceptions help

- App/domain level এ “what went wrong” clearly communicate করে। [web:27]
- UI/API boundary তে domain exceptions catch করে user-friendly response দেওয়া
  যায়। [web:27]

### 8.2 Pattern

```
class AppError(Exception):
    pass

class ConfigError(AppError):
    pass
```

- Now calling code can do:
  - `except AppError:` for all domain errors
  - or `except ConfigError:` for config-specific recovery. [web:27]

---

## 9) Exception chaining — root cause হারাবেন না

### 9.1 `raise NewError(...) from e` (recommended)

- PEP 3134 defines explicit chaining: original exception preserved as cause.
  [web:9]

```
class DataError(Exception): ...

def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise DataError(f"Expected int, got {s!r}") from e
```

- Benefit: user sees high-level meaning + dev sees original traceback.
  [web:9][web:21]

### 9.2 `raise ... from None` (context suppression)

- PEP 409: old context hide করার standard way. [web:1]

```
class ConfigError(Exception): ...

def require(cfg: dict, key: str):
    try:
        return cfg[key]
    except KeyError:
        raise ConfigError(f"Missing required key: {key!r}") from None
```

- Use when you intentionally want clean UX and previous traceback would confuse
  users. [web:1][web:27]

---

## 10) `contextlib.suppress` — intentional ignore (clean style)

- `contextlib` provides utilities for “with-statement contexts”. [web:19]
- `suppress(SomeError)` means: only that error ignore হবে, others will still
  raise. [web:19]

```
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("temp.txt")
```

- This is safer than broad `try/except: pass`. [web:19][web:27]

---

## 11) Cleanup best practice — `with` vs `finally`

- `finally` guarantees cleanup, but `with open(...)` (context manager) is
  usually cleaner for resource management. [web:21]
- Still, `finally` remains essential when cleanup is not tied to a single
  context manager. [web:21]

---

## 12) Python 3.11+ (advanced): Exception Groups & `except*` (reference)

- Python 3.11 adds Exception Groups and `except*` to handle multiple exceptions
  (often concurrency/async contexts). [web:42][web:44]
- Use this when multiple tasks fail and you want to handle subsets of failures
  by type. [web:44]

---

## 13) Practice tasks (concept lock-in)

1. Input parser: string → int; on failure raise `DataError` with chaining.
   [web:9][web:23]
2. File reader: first line read; handle `FileNotFoundError`, cleanup guaranteed.
   [web:21][web:23]
3. Config getter: missing key → `ConfigError` with `from None`. [web:1]
4. Cleaner tool: delete file if exists with `contextlib.suppress`. [web:19]

---

## 14) Projects (GitHub-ready)

### Project A: Robust CLI Calculator

- Handles `ValueError` and `ZeroDivisionError`, loop continues until exit.
  [web:21][web:23]

### Project B: Config Loader + Validator

- Validates required keys; missing keys show clean error messages using
  `raise ... from None`. [web:1][web:27]

### Project C: File Cleanup Utility

- Deletes temp files; ignores only `FileNotFoundError` via `suppress`.
  [web:19][web:23]

### Project D: Safe Runner (wrapper)

- Runs any job, logs exception with traceback, then re-raises to avoid silent
  failures. [web:21][web:27]
