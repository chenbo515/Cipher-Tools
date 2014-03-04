





class matrix:
    def __init__(self):
        self.array=[[0 for col in range(5)] for row in range(5)]
        self.newkey=''
    def add(self,ch):
        self.array[self.index/5][self.index%5]=ch
        self.index+=1
    def fill(self,key):
        self.index=0
        key=key.upper().replace(' ','')
        for ch in key:
            if ch.isalpha() and self.newkey.count(ch)==0 :
                self.newkey+=ch
        for ch in range(26):
            ch=chr(ch+ord('A'))
            if self.newkey.count(ch)==0 :
                self.newkey+=ch
        self.newkey=self.newkey.replace('J','')
        #print 'newkey is '+self.newkey
        for ch in self.newkey:
            self.add(ch)
    def printmatrix(self):
        for x in self.array:
            line=''
            for y in x:
                 line+=y+' '
            print line
    def decodechars(self,ch1,ch2):
        ch1_index={'x':self.newkey.find(ch1)/5,'y':self.newkey.find(ch1)%5}
        ch2_index={'x':self.newkey.find(ch2)/5,'y':self.newkey.find(ch2)%5}
        #print 'index of '+ch1+' is '+str(ch1_index)+' , index of '+ch2+' is '+str(ch2_index)
        if ch1_index['x']==ch2_index['x']:
            return (self.array[ch1_index['x']][(ch1_index['y']+4)%5],self.array[ch2_index['x']][(ch2_index['y']+4)%5])
        if ch1_index['y']==ch2_index['y']:
            return (self.array[(ch1_index['x']+4)%5][ch1_index['y']],self.array[(ch2_index['x']+4)%5][ch2_index['y']])
        else:
            return (self.array[ch1_index[
                'x']][ch2_index['y']],self.array[ch2_index['x']][ch1_index['y']])
    def encodechars(self,ch1,ch2):
        ch1_index={'x':self.newkey.find(ch1)/5,'y':self.newkey.find(ch1)%5}
        ch2_index={'x':self.newkey.find(ch2)/5,'y':self.newkey.find(ch2)%5}
        #print 'index of '+ch1+' is '+str(ch1_index)+' , index of '+ch2+' is '+str(ch2_index)
        if ch1_index['x']==ch2_index['x']:
            return (self.array[ch1_index['x']][(ch1_index['y']+1)%5],self.array[ch2_index['x']][(ch2_index['y']+1)%5])
        if ch1_index['y']==ch2_index['y']:
            return (self.array[(ch1_index['x']+1)%5][ch1_index['y']],self.array[(ch2_index['x']+1)%5][ch2_index['y']])
        else:
            return (self.array[ch1_index[
                'x']][ch2_index['y']],self.array[ch2_index['x']][ch1_index['y']])
class playfair:
    def __init__(self,key):
        self.m=matrix()
        self.m.fill(key)
        self.m.printmatrix()
    def encrypt(self,plaintext):
        ciphertext=''
        plaintext=plaintext.replace('J','I').replace(' ','').upper()
        for x in range(len(plaintext)-1):
            if plaintext[x]==plaintext[x+1]:
                plaintext=plaintext[:x+1]+'X'+plaintext[x+1:]
        if len(plaintext)%2==0:
            pad=''
        else:
            pad='Z'
        plaintext+=pad
        print 'plaintext is '+plaintext
        for index in range(len(plaintext))[::2]:
            chars=self.m.encodechars(plaintext[index],plaintext[index+1])
            print plaintext[index]+' and '+plaintext[index+1]+' are switched to '+str(chars)
            ciphertext+=chars[0]+chars[1]
        return ciphertext

    def decrypt(self,ciphertext):
        plaintext=''
        plaintext=plaintext.upper().replace(' ','')
        for index in range(len(ciphertext))[::2]:
            chars=self.m.decodechars(ciphertext[index],ciphertext[index+1])
            print ciphertext[index]+' and '+ciphertext[index+1]+' are switched to '+str(chars)
            plaintext+=chars[0]+chars[1]     
        return plaintext
s=raw_input('enter a text to encrypt\n')
k=raw_input('enter a password\n')
p=playfair(k)
e=p.encrypt(s)
print 'ciphertext is '+e
print 'plaintext is '+p.decrypt(e)
