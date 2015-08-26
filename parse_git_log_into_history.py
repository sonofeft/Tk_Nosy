"""
After running ``git log > git_log.txt``, parse the file ``git_log.txt`` and create
the file HISTORY.rst from it.
"""
# To use a consistent encoding
from codecs import open

from os import path

here = path.abspath(path.dirname(__file__))

# Get a list of lines from log info file
with open(path.join(here, 'git_log.txt'), encoding='utf-8') as f:
    log_infoL = f.read().strip().splitlines()

# make a list of starting lines
startL = []
for i in xrange( len(log_infoL) ):
    if log_infoL[i].startswith('commit '):
        startL.append( i )

startL.append( len(log_infoL) )

class Entry( object ):
    def __init__(self, ibeg, iend):
        self.msgL = []
        self.author = ''
        self.date = ''
        for i in xrange(ibeg, iend):
            s = log_infoL[i]
            if s.startswith('Author:'):
                self.author = s.split()[1]
            elif s.startswith('Date:'):
                sL = s.split()
                self.date =  sL[2] + ' ' + sL[3] + ', ' + sL[5]
            elif s.strip():
                self.msgL.append( s.strip() )
    def __str__(self):
        return self.date +' by:'+ self.author + '\n' + '\n'.join(self.msgL)
                
eL = []
for istart in xrange(len(startL) - 1):
    eL.append( Entry( startL[istart]+1, startL[istart+1] ) )
    

# Get a list of lines from log info file
fOut = open(path.join(here, 'HISTORY.rst'), 'w')

fOut.write(""".. :changelog:

History
=======

GitHub Log
----------

""")


for i,e in enumerate( eL ):
    if i==0 or (e.date != eL[i-1].date):
        fOut.write( '* ' + e.date + '\n' )
    if i==0 or (e.date != eL[i-1].date) or (e.author != eL[i-1].author):
        fOut.write( '    '  +'- (by: %s) '%e.author + '\n' )
    for msg in e.msgL:
        fOut.write('        '  +'- %s'%msg + '\n' )
        
fOut.close()    