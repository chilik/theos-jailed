#!/usr/bin/python

import io, sys
name=sys.argv[1]
orig=file(name,'rd')
data=orig.read()
orig.close()
out=data.replace(b'/usr/lib/libsubstrate.dylib',b'@executable_path/CSubstrate')
fout=file(name,'wb')
fout.write(out)
fout.close()
