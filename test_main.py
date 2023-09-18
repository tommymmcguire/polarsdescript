from main import read_csv_and_count_rating

def test_count_rating():
    # Test the count_rating function
    rating_count, rating_avg, median_rating, stddev_rating = read_csv_and_count_rating()
    assert int(rating_count) == 32780
    assert int(rating_avg) == 91
    assert int(median_rating) == 91
    assert int(stddev_rating) == 2
