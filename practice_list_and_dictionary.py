
def extract_list(test_dict_list, search_age):
    # ----------------------------
    # --- TEST Target Function ---
    # ----------------------------
    extract_list = list(
        filter(
            lambda item: item['age'] == search_age,
            test_dict_list
        )
    )
    return extract_list
