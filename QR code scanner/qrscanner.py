import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("https://www.youtube.com/watch?v=oB6TC529Oc0")
myqr1= qrcode.make("https://www.google.co.in/search?q=algoprep&sca_esv=596388893&source=hp&ei=G-CaZdHTMu-mhbIPkuqU-As&iflsig=ANes7DEAAAAAZZruK2YcdlbHxlYacgIEsvfyZNN9isbK&gs_ssp=eJzj4tVP1zc0zDHMKkwpL8kyYLRSNagwtjRITksxMktKNkk2TUlJszKoMLFMNLE0MEs1MEw0M0k0NfDiSMxJzy8oSi0AAGLGEx4&oq=algoprep&gs_lp=Egdnd3Mtd2l6IghhbGdvcHJlcCoCCAAyERAuGIMBGK8BGMcBGLEDGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESLo4UJ4XWPIscAF4AJABAZgBuQ2gAYcyqgEJNS01LjEuMS4xuAEByAEA-AEBqAIKwgIKEAAYAxiPARjqAsICChAuGAMYjwEY6gLCAhEQLhiABBixAxiDARjHARjRA8ICCBAAGIAEGLEDwgILEC4YgAQYsQMYgwHCAg4QLhiABBiKBRixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgIFEC4YgATCAhQQLhiABBiKBRixAxiDARjHARjRA8ICCxAAGIAEGLEDGIMBwgIIEC4YgAQYsQPCAgsQLhiABBjHARivAcICERAuGIAEGLEDGIMBGMcBGK8BwgILEC4YrwEYxwEYgAQ&sclient=gws-wiz")
myqr2= qrcode.make("https://www.youtube.com/watch?v=n2M9OXvnPnQ")
myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)
myqr2.save("myqr2.png",scale=6)

b = decode(Image.com("myqr.png"))
print(b[0].data.decode("ascii"))