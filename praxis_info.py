import urllib
import re

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

head_sep = "----+----1----+----2----+----3----+----4----+----5----+----6"
int_attrs = ["number", "pubmon", "pubday", "pubyear"]

def parse_chrono(infos = None):
    """Parse the chronological listing of exercises and add/update the infos"""
    page = urllib.urlopen("http://programmingpraxis.com/contents/chron/")
    contents = page.read()
    page.close()

    pattern = r"""
              <tr>\n
              <td>(\d+?)</td>\n
              <td>(\d\d?)\s([A-Z][a-z][a-z])\s(\d\d\d\d)</td>\n
              <td>(.*?)</td>\n.*?</tr>
              """

    exercises = re.findall(pattern, contents, re.DOTALL | re.VERBOSE)

    print exercises[0]
    print "*"*20
    print exercises[-1]
    print len(exercises)
    return infos

def parse_theme(infos = None):
    """Parse the thematic listing of exercises and add/update the infos"""
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
