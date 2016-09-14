# URL
# https://www.hackerrank.com/challenges/two-two

# target: less than 10s for a file
import regex as re
import math
import unittest

def main():
    # read input
    n = int(input().strip())
    cases = []
    for _ in range(n):
        cases.append(input().strip())
        
    pow2 = prepPow2(800)
        
    for case in cases:
        print(calcPow2s(case, pow2))


def prepPow2(p):
    ret = []
    for x in range(p):
        ret.append(int(math.pow(2,x)))
    #ret.append(1)
    return ret


def calcPow2s(data, pow2):
    total = 0
    
    for p in pow2:
        if len(str(p)) > len(data):
            break
        total += len(re.findall('(%s)' % p, data))
        #print(p, total)
    return total

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
def readFromFile(fname):
    data = []
    lnr = -1
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if lnr < 0:
            n = line
            lnr = 0
            continue
        data.append( line.strip() )
    return data
    
class Test(unittest.TestCase):
    
    def setUp(self):
        self.p = prepPow2(800)
        
    def txestCalc7x2(self):
        self.assertEquals(7, calcPow2s('2222222s', self.p))
        
    def xtestCalc1x2_4_256(self):
        self.assertEquals(4, calcPow2s('24256', self.p))

    def xtestCalc1x65536(self):
        self.assertEquals(1, calcPow2s('65536', self.p))        
        
    def xtestCalc2x32(self):
        self.assertEquals(4, calcPow2s('023223', self.p))   
                
    def xtestCalc0(self):
        self.assertEquals(0, calcPow2s('33579', self.p))  
    
    def txestCalcLong1(self):
        self.assertEquals(455, calcPow2s('2394524282602951341184917229922358099404279878411878431217485503159922313815972297931663057485981426649711508591569596253717388197656201203061030634919711598269311214066228954479756792882853062901769007199254740992118571099379011784113736688648896417641748464297615937576404566024103044751294464501645651011311865543459881103527895503076534540479074430301752383111205510814745150915769222029538271616265187852689524938529229181652437508374669137180409427187316048473796672026038921768447615746808217618268770466636286477546060408953537745699156787257089907708238395242331438777979805455309864961749800579826409539498001781694097092282535544714569949140616485127962399359500738578810541618443059271288134650346800291268306339067051951456695425758748915299883092176174487635584164154887676833928121541286087087412614229511011271491218722697833120659596691437416786879139845044909253853184300613450595050653169853516389035139504087366260264943450533244356122755214669880763353471793250393988087676928321',
            self.p))                      
    def xtestCalcLong2(self):
        self.assertEquals(476, calcPow2s('1897137590064188545819787018382342682267975428761855001222473056385648716020711424615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544331961245510479436680992629095292892080995698579394951999652586375252224913032651711976563915768303543055830928904063134591612086032942024630949986729117094964894544272120761894830081834798892792057209288656716241669552637251991334624898990071071509538300870787846456014842488100549243699210474849945267653984042207029848317287093254547337807326346532377907628148494958575626464295442893302882837389208192227229495220946833257770651288286003214805966303832139350404543766617799332207546397368398772612114315281400229324120391186508262907471446518781001063643199979511070672176498331492302656566440002483892212112902694227841240230545471432332984864391982563904255426568958978968711216842229769122273777112486581988938598139599956403855167484720643781523509973086428463104274877906944429496729612811310728', 
            self.p))
    def xtestCalcLong3(self):
        self.assertEquals(459, calcPow2s('1042962419883256876169444192465601618458351817556959360325703910069443225478828393565899456512321387608851798055108392418468232520504440598756558567060275241094811730846668025320233460001005199612029709556045777330319555224469955445943922763019814668659775210804444188892325882964314454560967680686052895717819140275184930690973423372373108471271228681978529185792148213874223764730142170860811120522052185580372019921970505707530128805939118083564406732517340014563415316953352597572834771287937445764994154608808724381779208207744383841696406077064304354370630711475550563574560936134891656032979834571870839343956992252245462692659218170968107390172263733095197200113358841034017182951507037254979515982202834948083154776267844089139019063040156654448338365040715366427194265232218475452906916175486393719275167627624034467811539875860662264875634828245120115979739426247133669695820851985744862087818610657767422912849272419524161066772132814424480153627222589353675077077069968594541456916486414',
            self.p))
        
    def testFile(self):
        fname = 'two-two-08.input.txt'
        data = readFromFile(fname)
        for d in data:
            print( calcPow2s(d, self.p) )
        