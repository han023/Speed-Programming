# https://www.hackerrank.com/challenges/handshake/problem?isFullScreen=true

# At the annual meeting of Board of Directors of Acme Inc. If everyone attending 
# shakes hands exactly one time with every other attendee, how many handshakes are there?

def handshake(n):
    return n*(n-1)//2


