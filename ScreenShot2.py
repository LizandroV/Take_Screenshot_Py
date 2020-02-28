import wx
wx.App()  # Need to create an App instance before doing anything
screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.EmptyBitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem  # Release bitmap
bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)

print("Test")

1.- cd "ruta de la carpeta"
2.- git init
3.- git status
4.- git add -A
5.- git status
6.- git commit -m "Version#"
7.- git remote add origin %link_git%
8.- git push origin mater

--------------------------------

1.- git add -A
2.- git status
3.- git commit -m "Version#"
4.- git push origin master
