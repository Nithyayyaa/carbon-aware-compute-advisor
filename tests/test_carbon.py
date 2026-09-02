import unittest

import pandas as pd

from cace.carbon import (
    compute_carbon_intensity,
    compute_carbon_intensity_series,
)


class CarbonIntensityTests(unittest.TestCase):
    def test_compute_carbon_intensity_uses_emissions_factors(self):
        intensity = compute_carbon_intensity(
            {"Solar": 100.0, "Fossil Gas": 100.0}
        )

        self.assertEqual(intensity, 265.5)

    def test_compute_carbon_intensity_returns_zero_for_no_generation(self):
        self.assertEqual(compute_carbon_intensity({"Solar": 0.0}), 0.0)

    def test_compute_carbon_intensity_series_preserves_index(self):
        index = pd.to_datetime(
            [
                "2026-01-01T00:00:00+01:00",
                "2026-01-01T00:15:00+01:00",
            ]
        )
        frame = pd.DataFrame(
            {
                "Solar - Actual Aggregated": [100.0, 0.0],
                "Fossil Gas - Actual Aggregated": [100.0, 0.0],
            },
            index=index,
        )

        result = compute_carbon_intensity_series(frame)

        self.assertTrue(result.index.equals(index))
        self.assertEqual(result.tolist(), [265.5, 0.0])


if __name__ == "__main__":
    unittest.main()
