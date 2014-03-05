import Image
import os
import sys
#magic number to tell weather a image file contains message
MAGIC_NUMBER='571532745'

def openfile(fn):
    try:
        m=Image.open(fn)
    except:
        print 'AN ERROR OCUURED,ILLEGAL FILE NAME'
    return m

def encode_image(fn):
    raw_msg=raw_input('enter a message to encrypt\n')
    #ensure the message length and be divied by 3
    msg=raw_msg+' '*(len(raw_msg)%3)
    msg=MAGIC_NUMBER+' '*(10-len(str(len(msg))))+str(len(msg))+msg
    print msg
    #ensure the image is able to hold the message
    if len(msg)>(im.size[0]*im.size[1]*3//8-8):
        print 'message is too long'
        os.system('PAUSE')
        sys.exit(1)

     # data_len=len(data)
    for x in range(len(msg)):
        for n in range(8):
            if ord(msg[x])&(1<<n):
                data[(x//3)*8+n][x%3]|=0x01
            else:
                data[(x//3)*8+n][x%3]&=0xfe
    for x in range(len(data)):
        data[x]=tuple(data[x])
    im.putdata(tuple(data))
    im.save(filename.split('.')[0]+'___encrypted.'+filename.split('.')[1]);
    print 'message was encoded to the image'

def read_byte(n):
    b=0
    for x in range(8):
        b|=(data[(n//3)*8+x][n%3]&0x01)<<x
    return chr(b)

def decode_image(fn):
    magic_num=''
    final_msg=''
    for x in range(len(MAGIC_NUMBER)):
        num=read_byte(x)
        magic_num+=num
    if magic_num!=MAGIC_NUMBER:
        print "this image doesn't contains any message"
        #os.system('PAUSE')
        sys.exit(1)
    msg_len=''
    for x in range(len(MAGIC_NUMBER),len(MAGIC_NUMBER)+10):
        msg_len+=read_byte(x)
    msg_len=int(msg_len)
    for x in range(len(MAGIC_NUMBER)+10,len(MAGIC_NUMBER)+10+msg_len):
        final_msg+=read_byte(x)
    print 'the message in the image is'
    print final_msg

filename=raw_input('enter the image filename\n')
im=openfile(filename)
data=list(im.getdata())
for x in range(len(data)):
    data[x]=list(data[x])
choice=raw_input("enter 'e' to encode a message\n enter 'd' to decode the message in current file.\n")
if choice=='e':
    encode_image(filename)
elif choice=='d':
    decode_image(filename)
else:
    print 'illegal user input'


