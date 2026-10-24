"""Convert a float of seconds into a compact human-readable string."""


_UNITS = ("h", "m", "s")


def humanize_duration(seconds):
    """Convert ``seconds`` into a compact string like ``'3h12m45s'``.

    Units with a zero value are omitted, with one deliberate exception:
    a duration of exactly zero renders as ``'0s'`` so the output is never
    empty. Negative durations are formatted with a leading ``-`` and the
    same unit breakdown applied to the absolute value.
    """
    if seconds < 0:
        return "-" + humanize_duration(-seconds)
    if seconds == 0:
        return "0s"

    # Truncate rather than round the sub-second remainder. Rounding could
    # push the seconds component up to 60, introducing a phantom leading
    # minute and breaking the compact representation the caller expects.
    total_int = int(seconds)
    remainder = round(seconds - total_int, 3)

    hours = total_int // 3600
    minutes = (total_int % 3600) // 60
    whole_seconds = total_int % 60

    parts = []
    for count, suffix in (
        (hours, "h"),
        (minutes, "m"),
        (whole_seconds, "s"),
    ):
        if count:
            parts.append(f"{count}{suffix}")

    if not parts:
        if remainder:
            parts.append(str(remainder).lstrip("0") + "s")
        else:
            parts.append("0s")
    else:
        if remainder:
            parts.append(str(remainder).lstrip("0") + "s")

    return "".join(parts)


def format_duration(seconds):
    """Alias for :func:`humanize_duration`.

    Provided so callers who prefer a verb-noun naming convention can use
    ``format_duration(seconds)`` instead of ``humanize_duration(seconds)``.
    """
    return humanize_duration(seconds)
