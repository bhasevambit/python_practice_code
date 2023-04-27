import unittest


def extract_list(test_dict_list, search_age):
    # ----------------------------
    # --- TEST Target Function ---
    # ----------------------------
    extract_list = list(
        filter(
            lambda item: item['age'] == search_age,
            test_dict_list))
    return extract_list


class ExtractListTest(unittest.TestCase):
    # -----------------------
    # --- Unit TEST Class ---
    # -----------------------
    def test_extract_list(self):

        test_dict_list = [
            {"name": "Taro", "age": 37},
            {"name": "Hanako", "age": 37},
            {"name": "Ken", "age": 9},
            {"name": "Dai", "age": 20},
        ]

        expected_results1 = [
            {"name": "Taro", "age": 37},
            {"name": "Hanako", "age": 37}
        ]
        expected_results2 = [
            {"name": "Ken", "age": 9}
        ]
        expected_results3 = [
            {"name": "Dai", "age": 20}
        ]
        expected_results4 = []

        actual_results1 = extract_list(test_dict_list, 37)
        actual_results2 = extract_list(test_dict_list, 9)
        actual_results3 = extract_list(test_dict_list, 20)
        actual_results4 = extract_list(test_dict_list, 1)

        self.assertEqual(expected_results1, actual_results1)
        self.assertEqual(expected_results2, actual_results2)
        self.assertEqual(expected_results3, actual_results3)
        self.assertEqual(expected_results4, actual_results4)


if __name__ == "__main__":
    unittest.main()
