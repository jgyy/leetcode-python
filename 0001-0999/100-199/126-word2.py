from typing import List
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def hashword(word):
            h=0
            c=1
            for i in word:
                h+=c*(ord(i)-97)
                c=c*26
            return h

        def unhash(value,length):
            c=1
            word=[]
            for i in range(length):
                cr=chr(((value%(c*26))//c)+97)
                word.append(cr)
                c=c*26
            return "".join(word)

        d={}
        for i in range(len(wordList)):
            d[hashword(wordList[i])]=0
        h=hashword(beginWord)
        q=deque()
        q.append(h)
        f=hashword(endWord)
        q=deque()
        q.append([h,1])
        d[h]=1
        main_ans=[]
        s=1
        while q:
            x=q.popleft()
            h=x[0]
            if h==f:
                s=x[1]
                break
            else:
                c=1
                for i in range(len(beginWord)):
                    for j in range(26):
                        y=h-(((h%(c*26))//c)*c)+(c*j)
                        if y in d:
                            if d[y]==0:
                                d[y]=x[1]+1
                                q.append([y,x[1]+1])
                    c=c*26
        ans=deque()
        if f in d:
            if d[f]==s:
                ans.append([f])
                while len(ans[0])<s:
                    x=ans.popleft()
                    h=x[-1]
                    c=1
                    for i in range(len(beginWord)):
                            for j in range(26):
                                y=h-(((h%(c*26))//c)*c)+(c*j)
                                if y in d:
                                    if d[y]==s-len(x):
                                        x.append(y)
                                        ans.append(x[::])
                                        x.pop()
                            c=c*26
        a=[]
        while ans:
            x=ans.popleft()
            ab=[]
            while x:
                k=unhash(x.pop(),len(beginWord))
                ab.append(k)
            a.append(ab)
        return a

if __name__ == "__main__":
    s = Solution()
    print(s.findLadders("a", "c", ["a","b","c"]))
    print(s.findLadders("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
    print(s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print(s.findLadders("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog", "cog"]))
    print(s.findLadders("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog", "cog", "cog"]))
    print(s.findLadders("red", "tax", [
          "ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
    print(s.findLadders("aaaaa", "ggggg", [
        "aaaaa", "caaaa", "cbaaa", "daaaa", "dbaaa", "eaaaa", "ebaaa", "faaaa", "fbaaa", "gaaaa", "gbaaa", "haaaa", "hbaaa", "iaaaa", "ibaaa", "jaaaa",
        "jbaaa", "kaaaa", "kbaaa", "laaaa", "lbaaa", "maaaa", "mbaaa", "naaaa", "nbaaa", "oaaaa", "obaaa", "paaaa", "pbaaa", "bbaaa", "bbcaa", "bbcba",
        "bbdaa", "bbdba", "bbeaa", "bbeba", "bbfaa", "bbfba", "bbgaa", "bbgba", "bbhaa", "bbhba", "bbiaa", "bbiba", "bbjaa", "bbjba", "bbkaa", "bbkba",
        "bblaa", "bblba", "bbmaa", "bbmba", "bbnaa", "bbnba", "bboaa", "bboba", "bbpaa", "bbpba", "bbbba", "abbba", "acbba", "dbbba", "dcbba", "ebbba",
        "ecbba", "fbbba", "fcbba", "gbbba", "gcbba", "hbbba", "hcbba", "ibbba", "icbba", "jbbba", "jcbba", "kbbba", "kcbba", "lbbba", "lcbba", "mbbba",
        "mcbba", "nbbba", "ncbba", "obbba", "ocbba", "pbbba", "pcbba", "ccbba", "ccaba", "ccaca", "ccdba", "ccdca", "cceba", "cceca", "ccfba", "ccfca",
        "ccgba", "ccgca", "cchba", "cchca", "cciba", "ccica", "ccjba", "ccjca", "cckba", "cckca", "cclba", "cclca", "ccmba", "ccmca", "ccnba", "ccnca",
        "ccoba", "ccoca", "ccpba", "ccpca", "cccca", "accca", "adcca", "bccca", "bdcca", "eccca", "edcca", "fccca", "fdcca", "gccca", "gdcca", "hccca",
        "hdcca", "iccca", "idcca", "jccca", "jdcca", "kccca", "kdcca", "lccca", "ldcca", "mccca", "mdcca", "nccca", "ndcca", "occca", "odcca", "pccca",
        "pdcca", "ddcca", "ddaca", "ddada", "ddbca", "ddbda", "ddeca", "ddeda", "ddfca", "ddfda", "ddgca", "ddgda", "ddhca", "ddhda", "ddica", "ddida",
        "ddjca", "ddjda", "ddkca", "ddkda", "ddlca", "ddlda", "ddmca", "ddmda", "ddnca", "ddnda", "ddoca", "ddoda", "ddpca", "ddpda", "dddda", "addda",
        "aedda", "bddda", "bedda", "cddda", "cedda", "fddda", "fedda", "gddda", "gedda", "hddda", "hedda", "iddda", "iedda", "jddda", "jedda", "kddda",
        "kedda", "lddda", "ledda", "mddda", "medda", "nddda", "nedda", "oddda", "oedda", "pddda", "pedda", "eedda", "eeada", "eeaea", "eebda", "eebea",
        "eecda", "eecea", "eefda", "eefea", "eegda", "eegea", "eehda", "eehea", "eeida", "eeiea", "eejda", "eejea", "eekda", "eekea", "eelda", "eelea",
        "eemda", "eemea", "eenda", "eenea", "eeoda", "eeoea", "eepda", "eepea", "eeeea", "ggggg", "agggg", "ahggg", "bgggg", "bhggg", "cgggg", "chggg",
        "dgggg", "dhggg", "egggg", "ehggg", "fgggg", "fhggg", "igggg", "ihggg", "jgggg", "jhggg", "kgggg", "khggg", "lgggg", "lhggg", "mgggg", "mhggg",
        "ngggg", "nhggg", "ogggg", "ohggg", "pgggg", "phggg", "hhggg", "hhagg", "hhahg", "hhbgg", "hhbhg", "hhcgg", "hhchg", "hhdgg", "hhdhg", "hhegg",
        "hhehg", "hhfgg", "hhfhg", "hhigg", "hhihg", "hhjgg", "hhjhg", "hhkgg", "hhkhg", "hhlgg", "hhlhg", "hhmgg", "hhmhg", "hhngg", "hhnhg", "hhogg",
        "hhohg", "hhpgg", "hhphg", "hhhhg", "ahhhg", "aihhg", "bhhhg", "bihhg", "chhhg", "cihhg", "dhhhg", "dihhg", "ehhhg", "eihhg", "fhhhg", "fihhg",
        "ghhhg", "gihhg", "jhhhg", "jihhg", "khhhg", "kihhg", "lhhhg", "lihhg", "mhhhg", "mihhg", "nhhhg", "nihhg", "ohhhg", "oihhg", "phhhg", "pihhg",
        "iihhg", "iiahg", "iiaig", "iibhg", "iibig", "iichg", "iicig", "iidhg", "iidig", "iiehg", "iieig", "iifhg", "iifig", "iighg", "iigig", "iijhg",
        "iijig", "iikhg", "iikig", "iilhg", "iilig", "iimhg", "iimig", "iinhg", "iinig", "iiohg", "iioig", "iiphg", "iipig", "iiiig", "aiiig", "ajiig",
        "biiig", "bjiig", "ciiig", "cjiig", "diiig", "djiig", "eiiig", "ejiig", "fiiig", "fjiig", "giiig", "gjiig", "hiiig", "hjiig", "kiiig", "kjiig",
        "liiig", "ljiig", "miiig", "mjiig", "niiig", "njiig", "oiiig", "ojiig", "piiig", "pjiig", "jjiig", "jjaig", "jjajg", "jjbig", "jjbjg", "jjcig",
        "jjcjg", "jjdig", "jjdjg", "jjeig", "jjejg", "jjfig", "jjfjg", "jjgig", "jjgjg", "jjhig", "jjhjg", "jjkig", "jjkjg", "jjlig", "jjljg", "jjmig",
        "jjmjg", "jjnig", "jjnjg", "jjoig", "jjojg", "jjpig", "jjpjg", "jjjjg", "ajjjg", "akjjg", "bjjjg", "bkjjg", "cjjjg", "ckjjg", "djjjg", "dkjjg",
        "ejjjg", "ekjjg", "fjjjg", "fkjjg", "gjjjg", "gkjjg", "hjjjg", "hkjjg", "ijjjg", "ikjjg", "ljjjg", "lkjjg", "mjjjg", "mkjjg", "njjjg", "nkjjg",
        "ojjjg", "okjjg", "pjjjg", "pkjjg", "kkjjg", "kkajg", "kkakg", "kkbjg", "kkbkg", "kkcjg", "kkckg", "kkdjg", "kkdkg", "kkejg", "kkekg", "kkfjg",
        "kkfkg", "kkgjg", "kkgkg", "kkhjg", "kkhkg", "kkijg", "kkikg", "kkljg", "kklkg", "kkmjg", "kkmkg", "kknjg", "kknkg", "kkojg", "kkokg", "kkpjg",
        "kkpkg", "kkkkg", "ggggx", "gggxx", "ggxxx", "gxxxx", "xxxxx", "xxxxy", "xxxyy", "xxyyy", "xyyyy", "yyyyy", "yyyyw", "yyyww", "yywww", "ywwww",
        "wwwww", "wwvww", "wvvww", "vvvww", "vvvwz", "avvwz", "aavwz", "aaawz", "aaaaz"
    ]))
    print(s.findLadders("aaaaa", "uuuuu", [
        "aaaaa", "waaaa", "wbaaa", "xaaaa", "xbaaa", "bbaaa", "bbwaa", "bbwba", "bbxaa", "bbxba", "bbbba", "wbbba", "wbbbb", "xbbba", "xbbbb", "cbbbb",
        "cwbbb", "cwcbb", "cxbbb", "cxcbb", "cccbb", "cccwb", "cccwc", "cccxb", "cccxc", "ccccc", "wcccc", "wdccc", "xcccc", "xdccc", "ddccc", "ddwcc",
        "ddwdc", "ddxcc", "ddxdc", "ddddc", "wdddc", "wdddd", "xdddc", "xdddd", "edddd", "ewddd", "ewedd", "exddd", "exedd", "eeedd", "eeewd", "eeewe",
        "eeexd", "eeexe", "eeeee", "weeee", "wfeee", "xeeee", "xfeee", "ffeee", "ffwee", "ffwfe", "ffxee", "ffxfe", "ffffe", "wfffe", "wffff", "xfffe",
        "xffff", "gffff", "gwfff", "gwgff", "gxfff", "gxgff", "gggff", "gggwf", "gggwg", "gggxf", "gggxg", "ggggg", "wgggg", "whggg", "xgggg", "xhggg",
        "hhggg", "hhwgg", "hhwhg", "hhxgg", "hhxhg", "hhhhg", "whhhg", "whhhh", "xhhhg", "xhhhh", "ihhhh", "iwhhh", "iwihh", "ixhhh", "ixihh", "iiihh",
        "iiiwh", "iiiwi", "iiixh", "iiixi", "iiiii", "wiiii", "wjiii", "xiiii", "xjiii", "jjiii", "jjwii", "jjwji", "jjxii", "jjxji", "jjjji", "wjjji",
        "wjjjj", "xjjji", "xjjjj", "kjjjj", "kwjjj", "kwkjj", "kxjjj", "kxkjj", "kkkjj", "kkkwj", "kkkwk", "kkkxj", "kkkxk", "kkkkk", "wkkkk", "wlkkk",
        "xkkkk", "xlkkk", "llkkk", "llwkk", "llwlk", "llxkk", "llxlk", "llllk", "wlllk", "wllll", "xlllk", "xllll", "mllll", "mwlll", "mwmll", "mxlll",
        "mxmll", "mmmll", "mmmwl", "mmmwm", "mmmxl", "mmmxm", "mmmmm", "wmmmm", "wnmmm", "xmmmm", "xnmmm", "nnmmm", "nnwmm", "nnwnm", "nnxmm", "nnxnm",
        "nnnnm", "wnnnm", "wnnnn", "xnnnm", "xnnnn", "onnnn", "ownnn", "owonn", "oxnnn", "oxonn", "ooonn", "ooown", "ooowo", "oooxn", "oooxo", "ooooo",
        "woooo", "wpooo", "xoooo", "xpooo", "ppooo", "ppwoo", "ppwpo", "ppxoo", "ppxpo", "ppppo", "wpppo", "wpppp", "xpppo", "xpppp", "qpppp", "qwppp",
        "qwqpp", "qxppp", "qxqpp", "qqqpp", "qqqwp", "qqqwq", "qqqxp", "qqqxq", "qqqqq", "wqqqq", "wrqqq", "xqqqq", "xrqqq", "rrqqq", "rrwqq", "rrwrq",
        "rrxqq", "rrxrq", "rrrrq", "wrrrq", "wrrrr", "xrrrq", "xrrrr", "srrrr", "swrrr", "swsrr", "sxrrr", "sxsrr", "sssrr", "ssswr", "sssws", "sssxr",
        "sssxs", "sssss", "wssss", "wtsss", "xssss", "xtsss", "ttsss", "ttwss", "ttwts", "ttxss", "ttxts", "tttts", "wttts", "wtttt", "xttts", "xtttt",
        "utttt", "uwttt", "uwutt", "uxttt", "uxutt", "uuutt", "uuuwt", "uuuwu", "uuuxt", "uuuxu", "uuuuu", "zzzzz", "zzzzy", "zzzyy", "zzyyy", "zzyyx",
        "zzyxx", "zzxxx", "zzxxw", "zzxww", "zzwww", "zzwwv", "zzwvv", "zzvvv", "zzvvu", "zzvuu", "zzuuu", "zzuut", "zzutt", "zzttt", "zztts", "zztss",
        "zzsss", "zzssr", "zzsrr", "zzrrr", "zzrrq", "zzrqq", "zzqqq", "zzqqp", "zzqpp", "zzppp", "zzppo", "zzpoo", "zzooo", "zzoon", "zzonn", "zznnn",
        "zznnm", "zznmm", "zzmmm", "zzmml", "zzmll", "zzlll", "zzllk", "zzlkk", "zzkkk", "zzkkj", "zzkjj", "zzjjj", "zzjji", "zzjii", "zziii", "zziih",
        "zzihh", "zzhhh", "zzhhg", "zzhgg", "zzggg", "zzggf", "zzgff", "zzfff", "zzffe", "zzfee", "zzeee", "zzeed", "zzedd", "zzddd", "zzddc", "zzdcc",
        "zzccc", "zzccz", "azccz", "aaccz", "aaacz", "aaaaz", "uuuzu", "uuzzu", "uzzzu", "zzzzu"
    ]))
