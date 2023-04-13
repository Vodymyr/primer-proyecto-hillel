

# def parse(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

from urllib.parse import parse_qs, urlparse


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_string = parsed_url.query
    parsed_params = parse_qs(query_string)
    return {key: value[0] for key, value in parsed_params.items()}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Dima&age=28&city=NY') == {'name': 'Dima', 'age': '28', 'city': 'NY'}
    assert parse('http://example.com/?name=Dima%20User&age=28&city=N.Y.') == {'name': 'Dima User', 'age': '28',
                                                                              'city': 'N.Y.'}
    assert parse('http://example.com/?name=&age=&city=') == {'name': '', 'age': '', 'city': ''}
    assert parse('http://example.com/?name=John&name=Doe') == {'name': 'John'}
    assert parse('https://example.com/path/to/page?name=&color=') == {'name': '', 'color': ''}