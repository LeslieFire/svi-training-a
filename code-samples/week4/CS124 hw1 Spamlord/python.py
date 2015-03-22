import sys
import os
import re
from pprint import pprint

email_patterns = ['([A-Za-z]+) {0,1}@ {0,1}([A-Za-z.]+).edu',
                  '([A-Za-z]+) at ([A-Za-z ]+)dot edu',
                  '([A-Za-z]+) at ([A-Za-z;]+);edu',
                  'obfuscate\((.*),(.*)\)',
                  '([A-Za-z]+) at ([A-Za-z.]+).edu',
                  '([A-Za-z]+) {0,1}&#x40; {0,1}([A-Za-z.]+).edu',
                  '>([A-Za-z.]+).*@(\w.+).edu',
                  '([A-Za-z]+) at ([A-Za-z ]+) edu']

num_patterns = ['[^0-9A-Za-z]{0,1}([0-9]{3})[^0-9A-Za-z]{0,1}-{0,1} {0,1}([0-9]{3})-{0,1}([0-9]{4})',
                ]
def process_file(name, f):
    # note that debug info should be printed to stderr
    # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
    res = []

    for line in f:
        line2 = line.replace('-', '')
        line_tuple = (line, line2)
        for line_ in line_tuple:
            for pattern in email_patterns:
                matches = re.findall(pattern, line_)
                for m in matches:
                    if 'tuple' in str(type(m)):
                            if 'edu' in m[0]:
                                domain = m[0].replace('.edu\'', '')
                                m = (m[1], domain)

                            email  = '%s@%s.edu' % m                
                            email = email.replace(' ', '')
                            email = email.replace('dot','.')
                            email = email.replace(';','.')
                            email = email.replace('\'', '')
                            res.append((name,'e',email))
                    else:
                        for i in m:
                            email  = '%s@%s.edu' % i
                            email = email.replace(' ', '')
                            email = email.replace('dot','.')
                            email = email.replace(';','.')
                            res.append((name,'e',email))

        for pattern in num_patterns:
            matches = re.findall(pattern, line)
            for m in matches:
                if 'tuple' in str(type(m)):
                    num = '%s-%s-%s' % m
                    res.append((name,'p',num))
                else:
                    for i in m:
                        num = '%s-%s-%s' % m
                        res.append((name,'p',num))
    res = set(res)
    return res

def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        with open(path,'r') as f:
            f_guesses = process_file(fname, f)
            guess_list.extend(f_guesses)
    return guess_list


if __name__ == "__main__":
#   with open('./test_folder/ashishg', 'r') as f:
#       pprint(process_file('ashishg',f))
    pprint(process_dir('./test_folder'))
