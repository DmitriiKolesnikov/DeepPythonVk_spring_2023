import unittets
from Client import *

class TestClient(unittest.TestCase):
  def test_process_url():
    url = 'https://ru.wikipedia.org/wiki/Baba_Yaga'
    process_url(url)

def test_main():
    with mock.patch('builtins.open', mock.mock_open(read_data='https://ru.wikipedia.org/wiki/Baba_Yaga' * 10)):
        with mock.patch('client.process_url') as mock_process_url:
            main(['urls.txt', '-m', '5'])
            assert mock_process_url.call_count == 10



if __name__ == "__main__":
  unittset.main()
