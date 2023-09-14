from main import read_csv_and_count_rating

def test_count_rating():
    # Test the count_rating function
    rating_count = read_csv_and_count_rating()
    assert rating_count == 32780