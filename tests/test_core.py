import unittest

from duration_humanizer_utils import humanize_duration, format_duration


class HumanizeDurationTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(humanize_duration(0), "0s")

    def test_seconds_only(self):
        self.assertEqual(humanize_duration(45), "45s")

    def test_minutes_and_seconds(self):
        self.assertEqual(humanize_duration(75), "1m15s")

    def test_hours_minutes_seconds(self):
        self.assertEqual(humanize_duration(11765), "3h16m5s")

    def test_negative(self):
        self.assertEqual(humanize_duration(-75), "-1m15s")

    def test_negative_zero_not_produced(self):
        self.assertEqual(humanize_duration(-0.0), "0s")

    def test_subsecond_remainder(self):
        self.assertEqual(humanize_duration(0.5), ".5s")

    def test_full_with_subsecond_remainder(self):
        self.assertEqual(humanize_duration(75.5), "1m15s.5s")

    def test_truncates_fractional_seconds(self):
        result = humanize_duration(59.9)
        self.assertEqual(result, "59s.9s")
        self.assertFalse(result.startswith("1m"))

    def test_format_duration_alias(self):
        self.assertEqual(format_duration(3600), humanize_duration(3600))

    def test_hours_only(self):
        self.assertEqual(humanize_duration(3600), "1h")

    def test_minutes_only(self):
        self.assertEqual(humanize_duration(120), "2m")


if __name__ == "__main__":
    unittest.main()
