#!/usr/bin/env python
# checks options
import sys
from stickystuff import LANGS
class Bough(object):
    def __init__(self, url, names, boughs):
        # files contained in boughs
        self.url=url
        self.names={}
        for i, l in enumerate(LANGS): self.names[l]=names[i]
        self.boughs=boughs

    def urls(self):
        us=[self.url]
        [us.extend(b.urls()) for b in self.boughs]
        return us

    def level(self, name, start=0):
        if name in self.urls()[1]: return start
        else:
            for b in self.boughs:
                result=b.level(name, start+1)
                if result is not None:return result

def standard_tree():
    tree=Bough(None, (None,None),[])
    # First bough!
    home=Bough("index.html", ("Home", "Home"), [])
    tree.boughs.append(home)
    # science
    s=Bough("science/index.html", ("Science", "Scienza"), [])
    s.boughs.append(Bough("science/lauelens.html", ("Laue lens", "Lenti di Laue!"), []))
    s.boughs.append(Bough("science/ga.html", ("Genetic Algorythms", "Algoritmi genetici!"), []))
    s.boughs.append(Bough("science/publications.html", ("Publications", "Pubblicazioni"), []))
    tree.boughs.append(s)

    # code
    pyxcom=(Bough("code/pyxcom/mission.html", ("Mission", "A cosa serve"), []),
            Bough("code/pyxcom/download.html", ("Download &amp; Install", "Scarica e installa"), []),
            Bough("code/pyxcom/manual.html", ("User guide", "Manuale"), []),
            Bough("code/pyxcom/screenshots.html", ("Screenshots", "Screenshots"), []),
        )

    qombinatorics=(Bough("code/qombinatorics/mission.html", ("Mission", "A cosa serve"), []),
                Bough("code/qombinatorics/download.html", ("Download &amp; Install", "Scarica e installa"), []),
                Bough("code/qombinatorics/manual.html", ("User guide", "Manuale"), []),
                Bough("code/qombinatorics/screenshots.html", ("Screenshots", "Screenshots"), []),
                )

    code=Bough("code/index.html", ("Software", "Software"), [])

    code.boughs.extend((Bough("code/hwads.html", ("Hardware&nbsp;ads", "Consigli&nbsp;hardware"), []),
                Bough("code/swads.html", ("Software&nbsp;ads", "Consigli&nbsp;software"), []),
                Bough("code/ap2html.html", ("ap2html", "ap2html"), []),
                Bough("code/pyxcom.html", ("pyxcom",  "pyxcom"),pyxcom),
                Bough("code/qombinatorics.html", ("qombinatorics",  "qombinatorics"),qombinatorics),
                #Bough("code/mandriva.html", ("Mandriva",  "Mandriva"),mandriva),
                ))
    tree.boughs.append(code)

    # freetime
    freetime=Bough("freetime/index.html", ("Free Time", "Tempo Libero"), [])
    freetime.boughs.append(Bough("freetime/trionfo/index.html", ("Trionfo!", "Trionfo!"), []))
    tree.boughs.append(freetime)
    # gallery
    gallery=Bough("gallery/index.html", ("Photo Gallery", "Galleria Fotografica"), [])
    gallery.boughs.append(Bough("gallery/test.html", ("Preview!", "Anticipo!"), []),)
    tree.boughs.append(gallery)
    #info
    info=Bough("info/index.html", ("Links &amp; Info", "Links &amp; Info"), [])
    info.boughs.extend((Bough("info/bio.html", ("Biography", "Biografia"), []),
                Bough("info/cv.html", ("Curriculum&nbsp;Vitae", "Curriculum&nbsp;Vitae"), []),
                Bough("info/publications.html", ("Publications", "Pubblicazioni"), []),
                ))
    tree.boughs.append(info)
    return tree

tree=standard_tree()

if __name__=="__main__":
    print tree.level('code/qombinatorics/mission.html')