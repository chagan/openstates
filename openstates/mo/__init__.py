import datetime

metadata = dict(
    name='Missouri',
    abbreviation='mo',
    legislature_name='Missouri General Assembly',
    lower_chamber_name='House of Representatives',
    upper_chamber_name='Senate',
    lower_chamber_title='Representative',
    upper_chamber_title='Senator',
    lower_chamber_term=2,
    upper_chamber_term=4,
    terms=[
        {'name': '2011-2012',
         'sessions': ['2011', '2012'],
         'start_year': 2011, 'end_year': 2012},
        ],
    session_details={
        '2012': {'start_date': datetime.date(2012,1,26), 'type': 'primary',
                 'display_name': '2012 Regular Session'},
        '2011': {'start_date': datetime.date(2011,1,26), 'type': 'primary',
                 'display_name': '2011 Regular Session'},
    },
    feature_flags=[],
    _ignored_scraped_sessions = [
        '2011 - 96th General Assembly - 1st Regular Session',
        '2010 - 95th General Assembly - 2nd Regular Session',
        '2009 - 95th General Assembly - 1st Regular Session',
        '2008 - 94th General Assembly - 2nd Regular Session',
        '2007 - 94th General Assembly - 1st Regular Session',
        '2006 - 93rd General Assembly - 2nd Regular Session',
        '2005 - 93rd General Assembly - 1st Regular Session',
        '2004 - 92nd General Assembly - 2nd Regular Session',
        '2003 - 92nd General Assembly - 1st Regular Session',
        '2002 - 91st General Assembly - 2nd Regular Session',
        '2001 - 91st General Assembly - 1st Regular Session',
        '2000 - 90th General Assembly - 2nd Regular Session',
        '1999 - 90th General Assembly - 1st Regular Session',
        '1998 - 89th General Assembly - 2nd Regular Session',
        '1997 - 89th General Assembly - 1st Regular Session',
        '1996 - 88th General Assembly - 2nd Regular Session',
        '1995 - 88th General Assembly - 1st Regular Session'
    ]
)

def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://www.senate.mo.gov/pastsessions.htm',
        "//div[@id='list']/li/a/text()")

