import urllib
import re
import os, os.path
from BeautifulSoup import BeautifulSoup

class PraxisInfo:
    __slots__ = ["number",
                 "file",
                 "pubmon",
                 "pubday",
                 "pubyear",
                 "title",
                 "ptitle",
                 "blurb",
                 "pblurb",
                 "exer",
                 "soln",
                 "extra",
                 "codepad",
                 "theme"]

    def __str__(self):
        ret = ""
        for slot in self.__slots__:
            if hasattr(self, slot):
                ret += slot + "\t" + str(getattr(self, slot)) + "\n"
        return ret

    def __lt__(self, other):
            comps = ["number", "pubyear", "pubmon", "pubday"]
            for c in comps:
                if getattr(self, c) < getattr(other, c):
                    return True
                if getattr(self, c) > getattr(other, c):
                    return False
            return NotImplemented

    def __le__(self, other):
        if self < other:
            return True
        if self == other:
            return True
        return False

    def __eq__(self, other):
        for slot in self.__slots__:
            if slot == "theme":
                continue
            if hasattr(self, slot) and hasattr(other, slot):
                if getattr(self, slot) != getattr(other, slot):
                    return False
        return True

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def add_info(self, other):
        for slot in self.__slots__:
            if slot == "theme":
                themes = []
                if hasattr(self, "theme"):
                    for th in self.theme.split("|"):
                        themes.append(th)
                if hasattr(other, "theme"):
                    for th in other.theme.split("|"):
                        themes.append(th)
                self.theme = "|".join(themes)
            elif hasattr(other, slot):
                if hasattr(self, slot):
                    if getattr(self, slot) != getattr(other, slot):
                        print self
                        print ""
                        print other
                        print ""
                        print slot
                        assert False
                else:
                    setattr(self, slot, getattr(other, slot))

head_sep = "----+----1----+----2----+----3----+----4----+----5----+----6"
int_attrs = ["number", "pubmon", "pubday", "pubyear"]
mon_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
            "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

def tidy_string(string):
    reps = [("&#8217;", "'"),
            ("&amp", "&"),
            ("&egrave;", "e"),
            ("&#039;", "'"),
            ("&minus;", "-"), ("&;minus", "-"),
            ("&pi;", "pi"),
            ("<em>", ""),
            ("</em>", ""),
            ("&times;", "."),
            ("&#8216;", "'"),
            ("&#8220;", "\""),
            ("&#8221;", "\""),
            ("&quot;", "\""),
            ("&le;", "<"),
            ("&gt;", ">"),
            ("&#8230;", "...")]

    for r in reps:
        string = string.replace(*r)

    return string

def parse_chrono(infos = None):
    """Parse the chronological listing of exercises and add/update the infos"""
    page = urllib.urlopen("http://programmingpraxis.com/contents/chron/")
    contents = page.read()
    page.close()

    pattern = r"""
              <tr>\n
              <td>(\d+?)</td>\n
              <td>(\d\d?)\s([A-Z][a-z][a-z])\s(\d\d\d\d)</td>\n
              <td><a\shref="(.*?)">(.*?)</a>:\s(.*?)</td>\n
              <td><a.*?</a>\s<a\shref="(.*?)">solution</a>\s<a\shref="http://programmingpraxis.codepad.org/(.*?)">codepad</a></td>\n
              </tr>
              """

    exercises = re.findall(pattern, contents, re.DOTALL | re.VERBOSE)

    if infos == None:
        infos = []

    for ex in exercises:
        info = PraxisInfo()
        info.number = int(ex[0])
        info.pubday = int(ex[1])
        info.pubmon = mon_dict[ex[2]]
        info.pubyear = int(ex[3])
        info.file = ex[4].split("/")[4]
        if len(ex[4].split("/")) == 7:
            info.exer = ex[4].split("/")[5]
        else:
            info.exer = "1"
        info.title = tidy_string(ex[5])
        info.blurb = tidy_string(ex[6])
        info.soln = ex[7].split("/")[-2]
        info.codepad = ex[8]

        found = -1
        for i, inf in enumerate(infos):
            if info == inf:
                found = i
                break
        if found == -1:
            infos.append(info)
        else:
            print found
            infos[found].add_info(info)

    return infos

def parse_theme(infos = None):
    """Parse the thematic listing of exercises and add/update the infos"""
    page = urllib.urlopen("http://programmingpraxis.com/contents/themes/")
    contents = page.read()
    page.close()

    soup = BeautifulSoup(contents)
    table = str(soup.find("table"))

    table = table.split("<tr>")

    curr_theme = None
    for t in table:
        theme_pattern = r'\s*<td\scolspan="6"><a\sname="(?P<theme>.*?)">.*'
        
        theme_match = re.match(theme_pattern, t, re.DOTALL | re.X)
        if theme_match:
            curr_theme = theme_match.group("theme")
            continue
        
        info_pattern = """\s*
                       <td>&nbsp;</td>\s
                       <td>(?P<number>\d+)</td>\s
                       <td>(?P<pubday>\d\d?)\s
                       (?P<pubmon>[A-Z][a-z][a-z])\s
                       (?P<pubyear>\d\d\d\d)</td>\s
                       <td><a\shref="(?P<addr>.*?)">
                       (?P<title>.*?)</a>:\s(?P<blurb>.*?)</td>\s
                       <td><a.*?</a>\s<a\shref="(?P<soln_addr>.*?)">solution</a>\s<a\shref="http://programmingpraxis.codepad.org/(?P<codepad>.*?)">codepad</a></td>\n
                       (.*?)</tr>
                       """

        info_match = re.match(info_pattern, t, re.DOTALL | re.X)

        fields = ["number", "pubday", "pubmon", "pubyear",
                  "title", "blurb", "codepad"]
        if info_match:
            info = PraxisInfo()
            for field in fields:
                if field == "pubmon":
                    info.pubmon = mon_dict[info_match.group("pubmon")]
                elif field in int_attrs:
                    setattr(info, field, int(info_match.group(field)))
                else:
                    setattr(info, field, tidy_string(info_match.group(field)))
            assert curr_theme
            info.theme = curr_theme

            addr = info_match.group("addr")
            info.file = addr.split("/")[4]
            if len(addr.split("/")) == 7:
                info.exer = addr.split("/")[5]
            else:
                info.exer = "1"
            soln = info_match.group("soln_addr")
            info.soln = soln.split("/")[-2]

            #Fix up a broken one
            if info.file == "rpn-calculator":
                info.number = 1

            found = -1
            for i,inf in enumerate(infos):
                if info == inf:
                    found = i
                    break
            if found == -1:
                infos.append(info)
            else:
                infos[i].add_info(info)

    return infos

def parse_praxis_info():
    """Read a set of PraxisInfos from the praxis.info file"""
    infos = []
    with open("praxis.info") as fin:
        line = ""
        while line != head_sep:
            line = fin.readline().strip()
        line = fin.readline()

        while line:
            info = PraxisInfo()
            line = fin.readline()
            while line and line != "\n":
                line = line.strip().split("\t")
                if line[0] in int_attrs:
                    setattr(info, line[0], int(line[1]))
                else:
                    setattr(info, line[0], line[1])
                line = fin.readline()
            infos.append(info)
    return infos

def write_praxis_info(infos):
    """Write out the praxis.info file from a set of infos"""
    with open("praxis.info", "w") as fout:
        fout.write("praxis.info\n")
        fout.write("\n")
        fout.write("number  exercise number\n")
        fout.write("file    base name of files\n")
        fout.write("pubmon  month of publication\n")
        fout.write("pubday  day of publication\n")
        fout.write("pubyear year of publication\n")
        fout.write("title   formatted title\n")
        fout.write("ptitle  plain title\n")
        fout.write("blurb   formatted blurb\n")
        fout.write("pblurb  plain blurb\n")
        fout.write("exer    exercise sub-page number\n")
        fout.write("soln    solution sub-page number\n")
        fout.write("extra   extra info sub-page number\n")
        fout.write("codepad eight-character codepad index\n")
        fout.write("theme   category in which exercise appears\n")
        fout.write("\n")
        fout.write("name/value pairs on a line separated by tabs,\n")
        fout.write("with records separated by blank lines\n")
        fout.write("\n")
        fout.write("the \"number\" field must appear first, others\n")
        fout.write("may be in any order, and are optional\n")
        fout.write("\n")
        fout.write("----+----1----+----2----+----3----+----4----+----5----+----6\n")
        fout.write("\n")

        for info in infos:
            fout.write("%s" % str(info))
            fout.write("\n")


def update_praxis_info():
    infos = parse_praxis_info()
    infos = parse_chrono(infos)
    infos = parse_theme(infos)
    write_praxis_info(infos)

def strip_exercise(contents):
    soup = BeautifulSoup(contents)

    title = soup.find('title')
    entry_title = soup.find('div', {"class": "entrytitle"})
    entry =  soup.find('div', {"class": "entrybody"})
    entry = str(entry).split("<div class=\"wpadvert\"")[0]
    entry = entry.split("<div id=\"wpcom_below_post\"")[0] + "</div>"

    page = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
    page += '<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en">\n'
    page += '<head>\n'
    page += str(title) + '\n'
    page += '</head>\n'
    page += '<body>\n'
    page += str(entry_title) + '\n'
    page += entry + '\n'
    page += '</body>\n'
    page += '</html>\n'

    return page

def download_exercises(infos, force=False):
    for i, info in enumerate(infos):
        print "Downloading", i+1, "/", len(infos), ":", info.file
        outpath = os.path.join("exercises", info.file + ".html")

        if os.path.exists(outpath) and not force:
            continue

        url = "http://programmingpraxis.com/"
        url += str(info.pubyear) + "/"
        url += str(info.pubmon) + "/"
        url += str(info.pubday) + "/"
        url += info.file + "/"

        page = urllib.urlopen(url)
        contents = page.read()
        page.close()

        contents = strip_exercise(contents)
        
        with open(outpath, "w") as fout:
            fout.write(contents)

def download_solutions(infos, force=False):
    for i, info in enumerate(infos):
        print "Downloading", i+1, "/", len(infos), ":", info.file

        outpath = os.path.join("solutions", info.file + ".html")

        if os.path.exists(outpath) and not force:
            continue
        
        url = "http://programmingpraxis.com/"
        url += str(info.pubyear) + "/"
        url += str(info.pubmon) + "/"
        url += str(info.pubday) + "/"
        url += info.file + "/"
        url += info.soln + "/"

        page = urllib.urlopen(url)
        contents = page.read()
        page.close()

        contents = strip_exercise(contents)

        with open(outpath, "w") as fout:
            fout.write(contents)

def chrono_page(infos):
    with open("chrono.html", "w") as fout:
        fout.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
        fout.write('<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en">\n')
        fout.write('<head>\n')
        fout.write('<title>Exercises by time</title>\n')
        fout.write('</head>\n')
        fout.write('<body>\n')

        for info in infos:
            fout.write(info.title + '\n')

        fout.write('</body>\n')
        fout.write('</html>\n')
