from pals import read_csv_and_count_rating

def test_count_rating():
    # Test the count_rating function
    csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
    rating_count = read_csv_and_count_rating(csv_url)
    assert rating_count == 32780