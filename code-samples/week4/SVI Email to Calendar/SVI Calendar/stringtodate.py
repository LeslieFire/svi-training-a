'''
Written by Antonio Carlos L. Ortiz. Updated: 03/18/2015
Input: the date returned by the database
Output: edits the date to the format that is required by
the google calendar api
'''

def string2date(s,startend='start'):
    month_dict = {"January":'01',
                  "February":'02',
                  "March":'03',
                  "April":'04',
                  "May":'05',
                  "June":'06',
                  "July":'07',
                  "August":'08',
                  "September":'09',
                  "October":'10',
                  "November":'11',
                  "December":'12',
                 }
                 
    s = s.replace("\n\r", " ")
    s = s.split()
    for n,i in enumerate(s):
      s[n] = i.strip(',')

    if startend == 'end':
        try:
            mm = month_dict[s[4]]
            dd = s[5]
            if len(dd) <= 1:
              dd = '0' + dd 
            yy = s[6]
            return '-'.join([yy,mm,dd])
        except:
          startend == 'start'

    elif startend == 'start':
        mm = month_dict[s[0]]
        dd = s[1]
        if len(dd) <= 1:
          dd = '0' + dd
        yy = s[2]
        return '-'.join([yy,mm,dd])
    
    else:
        return 'specify whether start or end'