from implementation.dominant import dominant
from implementation.median import median

first_dominant_array = [1, 2, 2, 3, 6, 3, 1, 2, 8, 2, 4, 2, 9, 2]

first_median_array = [1, 4, 8, 6, 3, 1, 9]
second_median_array = [2, 3, 8, 4]


class TestDominant:

    def test_empty_array(self):
        result, count, index = dominant([])
        assert result == 0

    def test_first_array(self):
        result, count, index = dominant(first_dominant_array)
        assert result == 2


class TestMedian:

    def test_empty_array(self):
        assert median([]) is None

    def test_median_even_elements_array(self):
        result = median(first_median_array)
        assert result == [4]

    def test_median_odd_elements_array(self):
        result = median(second_median_array)
        assert result == [3, 4]
