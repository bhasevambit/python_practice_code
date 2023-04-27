import unittest
from practice_list_and_dictionary import extract_list


class ExtractListTest(unittest.TestCase):
    # -----------------------
    # --- Unit TEST Class ---
    # -----------------------
    def setUp(self) -> None:
        self.test_dict_list = [
            {"name": "Taro", "age": 37},
            {"name": "Hanako", "age": 37},
            {"name": "Ken", "age": 9},
            {"name": "Dai", "age": 20},
        ]

    def test_extract_list1(self):
        expected_results = [
            {"name": "Taro", "age": 37},
            {"name": "Hanako", "age": 37}
        ]
        actual_results = extract_list(self.test_dict_list, 37)

        self.assertEqual(expected_results, actual_results)

    def test_extract_list2(self):
        expected_results = [
            {"name": "Ken", "age": 9}
        ]
        actual_results = extract_list(self.test_dict_list, 9)

        self.assertEqual(expected_results, actual_results)

    def test_extract_list3(self):
        expected_results = [
            {"name": "Dai", "age": 20}
        ]
        actual_results = extract_list(self.test_dict_list, 20)

        self.assertEqual(expected_results, actual_results)

    def test_extract_list4(self):
        expected_results = []
        actual_results = extract_list(self.test_dict_list, 1)

        self.assertEqual(expected_results, actual_results)


if __name__ == "__main__":
    unittest.main()
