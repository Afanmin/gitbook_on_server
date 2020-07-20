import os
import sys
def generateIndex(dir,root=False,filename = 'SUMMARY.md'):
    def myWalkThrough(dir,depth,fp,filename,root=False):
        #print(filename)
        ls = os.listdir(dir)
        ls.sort()
        readme = 'README.md'
        if not root:
            if readme in ls:
                fp.write(depth+' '+'['+dir.split('/')[-1]+']'+'('+ dir+'/'+ readme +')\n')
                print(depth,'['+dir.split('/')[-1]+']'+'('+ dir+'/'+ readme +')')
            depth = '   ' + depth
        for item in ls:
            if os.path.isfile(dir+'/'+item):
                if os.path.splitext(item)[-1] == '.md':
                    if item == readme and not root:
                        continue
                    if root and item == filename:
                        continue
                    fp.write(depth+' '+'['+ os.path.splitext(item)[0] +']'+'('+dir+'/'+item+')\n')
                    print(depth,'['+ os.path.splitext(item)[0] +']'+'('+dir+'/'+item+')')

        for item in ls:
            if not item.startswith('.') and not item.startswith('_'):
                if os.path.isdir(dir+'/'+item):
                    myWalkThrough(dir+'/'+item,depth,fp,filename)
    with open(dir+'/'+filename,'w') as fp:
        depth = '*'
        fp.write('# '+filename.split('.')[0]+'\n')
        myWalkThrough(dir,depth,fp,filename,root=root)

def main(args):
    try:
        path = args[1]
        filename = args[2]
    except:
        filename = 'SUMMARY.md'
    os.chdir(path)
    print(filename)
    generateIndex('.',root=True,filename=filename)

if __name__ == '__main__':
    main(sys.argv)
