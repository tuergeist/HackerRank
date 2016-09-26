'''
valid string = same number of chars
'''
import unittest

def main():
    # read input
    S = input().strip()
    if check(S):
        print("YES")
    else:
        print("NO")


def check(S):
    c = {}
    for s in S:
        try:
            c[s] += 1
        except:
            c[s] = 1
    ma = c[max(c, key = lambda x: c.get(x) )]
    mi = c[min(c, key = lambda x: c.get(x) )]
    #print(c, ma, mi)
    if ma == mi:
        return True
    
    if (ma - mi) == 1 :
        # check how many have min/max
        # exact one shall be max or min
        minc = 0
        maxc = 0
        other = 0
        for e in c.keys():
            if c[e] == ma: maxc+=1
            else: minc+=1
            if maxc > 1 and minc >1:
                return False
            #print(minc, maxc, other)
        return True
    
    if mi == 1:
        minc = 0
        maxc = 0
        other = 0
        for e in c.keys():
            if c[e] == ma: maxc+=1
            elif c[e] == mi: minc+=1
            else: 
                other+=1
            if maxc > 0 and minc > 0 and other >0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()        
        
    
class Test(unittest.TestCase):
    def testYes(self):
        self.assertTrue(check('aabbcc'))
        self.assertTrue(check('aabcc'))
        self.assertTrue(check('aabcc'))
        self.assertTrue(check('abcc'))
        self.assertTrue(check('abc'))
        
    def testNo(self):
        self.assertFalse(check('aaaabbcc'))   
        
    def testNo2(self):     
        self.assertFalse(check('aabbcd'))
        
    def testNo3(self):     
        self.assertFalse(check('tfgyrknpgngtqgjccbyctwdcymwrcjtpoaflkeoxfxijxkngpjoofggsozftkpgxakptmzjxugavazwllxdtrjrrbjmrqwfxaby'))
        
    def testLongYes(self):
        s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
        self.assertTrue(check(s))
        