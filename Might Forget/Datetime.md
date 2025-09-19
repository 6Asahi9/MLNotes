Got it 🌙 I’ll polish this up into a **clear, neat reference sheet** so it’s easier to read and use when working with Python datetimes.

---

# 🕒 Manipulating Datetime Strings in Python

To work with dates and times in Python, you’ll need the `datetime` module:

```python
from datetime import datetime
```

---

## 📅 Common `strftime` / `strptime` Format Codes

| Code | Format                          | Example                               |
| ---- | ------------------------------- | ------------------------------------- |
| `%a` | Abbreviated weekday             | `Sun`                                 |
| `%A` | Full weekday                    | `Sunday`                              |
| `%b` | Abbreviated month               | `Jan`                                 |
| `%B` | Full month name                 | `January`                             |
| `%c` | Locale’s date & time            | `Sun Jan 1 00:00:00 2021`             |
| `%d` | Day (01–31)                     | `01` → `31`                           |
| `%H` | Hour (24h clock)                | `00` → `23`                           |
| `%I` | Hour (12h clock)                | `01` → `12`                           |
| `%j` | Day of year                     | `001` → `366`                         |
| `%m` | Month (01–12)                   | `01` → `12`                           |
| `%M` | Minute                          | `00` → `59`                           |
| `%p` | AM/PM                           | `AM` / `PM`                           |
| `%S` | Seconds                         | `00` → `61`                           |
| `%U` | Week number (Sunday as 1st day) | `00` → `53`                           |
| `%W` | Week number (Monday as 1st day) | `00` → `53`                           |
| `%w` | Weekday (0=Sunday)              | `0` → `6`                             |
| `%x` | Locale’s date                   | `08/16/1988` (US) / `16.08.1988` (DE) |
| `%X` | Locale’s time                   | `21:30:00`                            |
| `%y` | Year (2-digit)                  | `88`                                  |
| `%Y` | Year (4-digit)                  | `2022`                                |
| `%z` | UTC offset                      | `+0900`                               |
| `%Z` | Time zone                       | `JST`, `GMT`, `EDT`                   |

---

## 🔧 Useful Datetime Functions

| Code / Function                                                                                                                                               | Input Type         | Input Example                | Output Type                 | Output Example                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------------------- | --------------------------- | ------------------------------ |
| `datetime.strptime("25/11/2022", "%d/%m/%Y")`                                                                                                                 | String             | `"25/11/2022"`               | `datetime`                  | `2022-11-25 00:00:00`          |
| `datetime.strftime(dt, "%d/%m/%Y")`                                                                                                                           | Datetime           | `2022-11-25 00:00:00`        | String                      | `"25/11/2022"`                 |
| `dt = datetime.strptime("25/11/2022", "%d/%m/%Y")`<br>`datetime.timestamp(dt)`                                                                                | String             | `"25/11/2022"`               | Float (seconds since epoch) | `1669334400.0`                 |
| `datetime.strptime("25/11/2022", "%d/%m/%Y").strftime("%Y-%m-%d")`                                                                                            | String             | `"25/11/2022"`               | String                      | `"2022-11-25"`                 |
| `datetime.fromtimestamp(1669334400.0)`                                                                                                                        | Float (timestamp)  | `1669334400.0`               | Datetime                    | `2022-11-25 00:00:00`          |
| `datetime.fromtimestamp(1669334400.0).strftime("%d/%m/%Y")`                                                                                                   | Float (timestamp)  | `1669334400.0`               | String                      | `"25/11/2022"`                 |
| `datetime.strptime("20:00", "%H:%M").strftime("%I:%M %p")`                                                                                                    | String             | `"20:00"`                    | String                      | `"08:00 PM"`                   |
| `datetime.strptime("08:00 PM", "%I:%M %p").strftime("%H:%M")`                                                                                                 | String             | `"08:00 PM"`                 | String                      | `"20:00"`                      |
| `from pytz import timezone`<br>`ny = datetime.strptime("25-11-2022 09:34:00-0700", "%d-%m-%Y %H:%M:%S%z")`<br>`tokyo = ny.astimezone(timezone("Asia/Tokyo"))` | String w/ timezone | `"25-11-2022 09:34:00-0700"` | Datetime (converted)        | `2022-11-26 01:34:00 JST+0900` |

---

✨ In short:

* **`strptime`** → parse string → datetime
* **`strftime`** → format datetime → string
* **timestamp/fromtimestamp** → convert between datetime ↔ seconds since epoch
* **timezone conversion** lets you easily flip between time zones.

---

Do you want me to also make you a **super short “cheat card” version** (like 5 most useful codes + 3 most common functions) for quick recall, instead of the big table?
