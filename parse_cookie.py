








# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

def parse_cookie(query: str) -> dict:
    cookies = query.split(";")
    parsed_cookies = {}

    for cookie in cookies:
        cookie_parts = cookie.split("=")
        if len(cookie_parts) >= 2:
            cookie_name = cookie_parts[0].strip()
            cookie_value = cookie_parts[1].strip()
            parsed_cookies[cookie_name] = cookie_value

    return parsed_cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name1=;age1=;') == {'name1': '', 'age1': ''}
    assert parse_cookie('name2=Dima,age2=28,city2=NY,') == {'name2': 'Dima', 'age2': '28', 'city2': 'NY'}
    assert parse_cookie('name3=Dima;age3=28;city3=NY;') == {'name3': 'Dima', 'age3': '28', 'city3': 'NY'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=3&size=small') == {'name': 'ferret', 'color': 'purple', 'age': '3', 'size': 'small'}
    assert parse('https://example.com/?name=ferret&color=purple&age=3&size=small') == {'name': 'ferret', 'color': 'purple', 'age': '3', 'size': 'small'}
