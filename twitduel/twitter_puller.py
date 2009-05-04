'''
Created on May 3, 2009

@author: darkxanthos
'''
from twitter import Twitter

test = Twitter()
test.username = "darkxanthos"
test.password = "mypw"

print test.statuses.friends_timeline()[0]