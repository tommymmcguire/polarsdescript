from pals import data_desc

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"

def test_fxn():
    assert data_desc(csv_url) == 32780