# duration_humanizer_utils

Converts a float of seconds into a compact human-readable string like `3h12m45s`, omitting units that are zero.

```python
from duration_humanizer_utils import humanize_duration

print(humanize_duration(11765))  # '3h16m5s'
print(humanize_duration(0))      # '0s'
print(humanize_duration(-75))    # '-1m15s'
```

## Why

Log lines and dashboards often need a duration in a fixed, compact form. The standard `datetime` and `timedelta` formatters produce verbose or locale-dependent output. This library gives a single, deterministic representation with no decisions left to the caller at format time.

The trade-off: sub-second remainders are appended verbatim after the whole-seconds component (e.g. `1m15s.5s`), rather than being rounded. Rounding could push seconds to 60, creating a phantom minute and an inconsistent output. Truncation keeps each component within its base unit.

## Edge cases

- `0` renders as `0s` (never an empty string).
- Negative durations render with a leading `-`, e.g. `-1m15s`.
- Fractional seconds are truncated, not rounded, so `59.9` renders as `59s.9s`, not `1m`.

Exported names: `humanize_duration`, `format_duration` (alias).
