"""
Functions for task 2 of the 2017 - Kont exam from NTNU
"""

def file_to_list(filename: str) -> list:
    """
    Task 2a (5%)

    Takes a filename, opens the file and splits it by lines then splits the lines by tabs.
    Then it returns the 2-dimentional list.
    """
    try:
        text_file = open(filename)
        line_list = text_file.read().split("\n")
        text_file.close()
        list_list = list(map(lambda line: line.split("\t"), line_list))
        return list_list
    except IOError:
        print("Error: File does not appear to exist.")
        return 0

def list_stores(data_list: list) -> list:
    """
    Task 2b (4%)
    """
    stores = map(lambda line: line[0], data_list)
    filtered_stores = list(set(stores))
    return filtered_stores

def sum_prices_stores(data_list: list, store_list: list) -> list:
    """
    Task 2c (5%)
    """
    return_list = []
    for store in store_list:
        store_lines = filter(lambda line: line[0] == store, data_list)
        store_prices = map(lambda line: float(line[2]), store_lines)
        price = sum(store_prices)
        return_list.append(price)
    return return_list

def rank_stores(store_list: list, sum_stores: list) -> list:
    """
    Task 2d (6%)
    """
    store_sums = []
    for i in range(0, len(store_list), 1):
        store_sums.append([store_list[i], sum_stores[i]])
    store_sums.sort(key=lambda element: element[1])
    ranked_stores = list(map(lambda element: element[0], store_sums))
    return ranked_stores

def store_analysis(filename):
    """
    Task 2e (5%)
    """
    data_list = file_to_list(filename)
    store_list = list_stores(data_list)
    sum_stores = sum_prices_stores(data_list, store_list)
    ranked_store_list = rank_stores(store_list, sum_stores)

    print("The total price for shopping per store is:")
    for i in range(0, len(store_list), 1):
        print("{} : {} kr".format(store_list[i], sum_stores[i]))

    print("The ranking of stores according to prices is:")
    for i in range(0, len(ranked_store_list), 1):
        print("{} {}".format(i+1, ranked_store_list[i]))

def main():
    """
    Main method for Task 2.
    """
    print(
        """
        Task 2 (25%)
        """
    )
    store_analysis("pricewar.txt")

if __name__ == "__main__":
    main()
