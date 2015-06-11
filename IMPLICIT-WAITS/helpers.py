from datetime import datetime

def generate_date_stamp():
    ''' generates a unique datestamp of the form yyyymmdd-hhmmss '''
    now = datetime.now()
    return(now.strftime('%Y%m%d-%H%M%S-%f'))

def generate_email(date_stamp,prefix='saucelabs.automation',suffix='@gmail.com'):
    ''' given a unique date stamp, generates a unique email address for automated registering
        of SauceLabs accounts '''
    return(prefix + '+' + date_stamp + suffix)
