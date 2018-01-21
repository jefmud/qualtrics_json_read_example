import urllib
import urllib2
import json


# you could possibly put these in the settings file, these are app-secrets, but could possibly be encoded into a database table
qualtrics_url = 'https:// ------' # an institutional or individual URL
qualtrics_user = 'user#organization' # an institutional or individual user id
qualtrics_token = '--secret token---' # you may have to activate/generate this in your account

def qualtrics_parameters(user, token, survey_id, version='2.4', format='JSON'):
    """returns qualtrics paramers dictionary"""
    return {'User': user, 'Token': token, 'SurveyID': survey_id, 'Version': version, 'Format': format}

def get_qualtrics_JSON(url, params):
    """get_qualtrics_JSON(url, params) - gets the JSON data from a particular Qualtrics survey
    url = The Qualtrics API base URL
    params = Dictionary of User, Token, and SurveyID, Version, Format
    returns JSON array data
    """
    data = None
    encoded_params = urllib.urlencode(params)
    try:
        request = urllib2.urlopen(url, encoded_params).read()
        data = json.loads(request)
    except:
        pass
    return data

if __name__ == '__main__':
    survey_id = ' ---- some id ---- ' # this is a survey identifier, comes from user profile and survey
    survey_params = qualtrics_parameters(user=qualtrics_user, token=qualtrics_token, survey_id=survey_id)
    data = get_qualtrics_JSON(url=qualtrics_url, params=survey_params)

    with open('data.json', 'w') as fp:
        json.dump(data, fp)
