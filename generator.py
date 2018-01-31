import os
from staticjinja import make_site


if __name__ == "__main__":
    outpath = "./site"
    site = make_site(outpath=outpath)
    site.render()
    os.remove(outpath+'/base.html')
