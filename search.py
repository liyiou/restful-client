import requests
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)

class ArcSightLogger(object):

    def __init__(self, logger, username, password):
        self.logger = logger
        self.username = username
        self.password = password

    def _login(self):
        url = self.logger + '/core-service/rest/LoginService/login?login=admin&password=password'
        r = requests.get(url, verify=False)
        return r

    def _logout(self, auth_token):
        url = self.logger + '/core-service/rest/LoginService/logout?authToken=' + auth_token
        r = requests.get(url, verify=False)
        return r

    def _startSearch(self, search_id, query, start, end, auth_token):
        url = self.logger + '/server/search'
        r = requests.post(url, json = {'search_session_id' : search_id, 'user_session_id' : auth_token}, verify=False)
        return r

    def _getEvents(self, search_id, auth_token):
        url = self.logger + '/server/search/events'
        r = requests.post(url, json={'search_session_id': search_id, 'user_session_id': auth_token, 'length': 10000}, verify=False)
        return r

if __name__ == '__main__':

    arcsight_search = ArcSightLogger(logger='https://15.214.133.151', username='admin', password="password")
    search_query = ''
    search_id = 1
    start_time = '2017-09-01T22:08:44.000-07:00'
    end_time = '2017-09-30T22:08:44.000-07:00'
    local_search = True

    r = requests.get(loginurl, params=login_values, headers=headers_init, verify=False)
    if r.status_code == 200:
        print("Login completed successfully.")
    if debug:
        print(r.raise_for_status)
        print(r.url)
        print(r.status_code)  # 200=Request completed successfully, 500=Request error or authentication failure
        print(r.encoding)
        # print(r.json)
        print(r.text)
    # print(r.headers)
    # print(r.headers['Content-Type'])
    # print(r.headers.get('content-type'))
    for cookie in r.cookies:
        if cookie.name == "session_string":
            session_cookie = cookie.value
    print(session_cookie)

    #auth_token = arcsight_search._login()  # For this to work, the session_string needs to be extract from the response
    auth_token = 'j4GoUEBxUNd5p_ToXs7-sjDrFZJtUp1QYk2tgtDVEKw.'

    r = arcsight_search._startSearch(search_id, search_query, start_time, end_time, auth_token)

    counter = 0
    numEvents = 0
    start = datetime.utcnow()
    while(counter < 10):
        r = arcsight_search._getEvents(search_id, auth_token)
        counter += 1
        numEvents += len(r.json()['results'])
        if r.json() == None:
            break
    time = datetime.utcnow() - start

    print numEvents, time, numEvents/time.seconds



