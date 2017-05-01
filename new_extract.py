import requests
from lxml import html

USERNAME = "sk9727192@gmail.com"
PASSWORD = "8687917613"

LOGIN_URL = "https://bitbucket.org/account/signin/"
URL = "https://bitbucket.org/dashboard/overview"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    print authenticity_token

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print result.ok
    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    print result.ok
    tree = html.fromstring(result.content)
    bucket_elems = tree.findall(".//*[@id='repositories-pjax']/div/section/table/tbody/tr/td[1]/div/a")
    bucket_names = [bucket_elem.text_content().replace("\n", "").strip() for bucket_elem in bucket_elems]

    print bucket_names

if __name__ == '__main__':
    main()