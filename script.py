import pygame as pg
import sys
pg.init()
#Initial Setup
win_width,win_height = [1200,600]
reflektor=[]
vertices=[]
c="01"
occluded=[]
jars=[]
mode="vertices"
splits=[]
pg.display.set_caption("Luxor 3 Map Editor by Mima Explorer")
icon=pg.image.load("icon.ico")
pg.display.set_icon(icon)
creators=pg.image.load("credits.png")
muted=False
targets=[]
editorOpen=False
vertnum=0
creditsOpen=False
visible=True
sh=[]
printed=[]
pg.display.init()
win=pg.display.set_mode([win_width,win_height])
#Your Level
BG=pg.image.load("background.png")
editordisplay=pg.image.load("spriteeditor.png")
menu=pg.image.load("menu.png")
#Buttons
hiden=pg.image.load("hidden.png")
reload=pg.image.load("reloadmap.png")
save=pg.image.load("savemap.png")
muste=pg.image.load("mute.png")
editor=pg.image.load("objecteditor.png")
printvis=[]
m=1
#Music
l3ctn=pg.mixer_music.load("ctn.mp3")
pg.mixer.music.play()
pg.mixer.music.play()
pg.mixer.music.play()
pg.mixer.music.play()
pg.mixer.music.play()
pg.mixer.music.play()
#Editor Buttons
zones=pg.image.load("zoning.png")
reflektormod=pg.image.load("reflekTour.png")
jarmod=pg.image.load("jar.png")
splittermod=pg.image.load("splitter.png")
vertices=[]
d=1
m=1
vis=0.02
#Loads in the user interface and the map
win.blit(BG, (0,0))
win.blit(menu, (800,0))
win.blit(BG, (0,0))
win.blit(hiden, (800,525))
win.blit(reload, (875,525))
win.blit(save, (950,525))
win.blit(muste, (1025,525))
win.blit(editor, (1100,525))
pg.display.update()
target=0,0
#The "Forever" Loop
active=True
while active:
    pg.mixer.init()
    pg.mixer.music.set_volume(1)
    #On click adds the vertices
    for event in pg.event.get():
        mouseup=pg.MOUSEBUTTONUP
        if event.type==mouseup:
            if mode=="vertices":
                vertice=pg.mouse.get_pos()
                iks=pg.mouse.get_pos()
                if visible:
                    pg.draw.line(BG,(255,0,255),iks,vertice,width=10)
                    pg.display.update()
                else:
                    pg.draw.line(BG,(0,255,255),iks,vertice,width=10)
                pg.display.update()
                vertnum+=1
                vertis=*vertice,vis
                vertices.append(vertis)
                iks=vertice
            elif mode=="reflektor":
                ref=pg.mouse.get_pos()
                reflektor.append(ref)
                target=tuple(input("Input Target").split())
                targets.append(target)
            elif mode=="split":
                splitter=pg.mouse.get_pos()
                splits.append(splitter)
            elif mode=="jars":
                jar=pg.mouse.get_pos()
                jars.append(jar)
        if event.type==pg.QUIT:
            actve=False
            pg.quit()
#Hotkeys
        if event.type == pg.KEYDOWN:
                #Vertice Visiblity(H)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h and visible and mode=="vertices":
                    visible=False
                    vis=0.01
                elif event.key == pg.K_h and not visible and mode=="vertices":
                    visible=True
                    vis=0.02
            #(S)s
        if event.type==pg.KEYUP:
            if event.key == pg.K_s and not editorOpen:
                print("//Luxor 3 Track Files")
                print("")
                print("Verts:")
                print("{")
                for i in vertices:
                     print("Vert ",*i)
                print("")
                print("}")
                print("")
                print("Sections:")
                print('"initial"',"{"," 0 1 2"," }")
                #Occluded Printing:
                for k in range(3,len(vertices)):
                    occluded.append(k)
                print('"occlude1"'"{ ",*occluded[3:-4]," }")
                occluded=occluded[: :-1]
                print('"pyramid_gate"',"{ ",occluded[3],"",occluded[2]," }")
                print('"pyramid"',"{ ",occluded[1],"",occluded[0], "}")
                print("")
                print("}")
                print("")
                print("Reflectors")
                print("{")
                for l in reflektor:  
                    for p in targets:
                        if m<10:
                            c='"'+"0"+str(m)+'"'
                        else:
                            c=str(m)
                            m+=1 
                    print("reflect",c,""," { ",l," to ",p," }")
                print("")
                print("}")
                print("")
                print("NamedPoints")#canopic jar spawn
                print("{")
                for n in jars:
                    b=""
                    if d<10:
                        b="0"+str(d)
                    else:
                        b=str(d)
                    print("pointspawn"+b," ",n)
                    d+=1
                print("}")
                print("Split Coordinates. DO NOT COPY THIS INTO PATH.LX3TRX!")
                for w in splits:
                    pos=splits.index(w)+1
                    sp="Split #"+str(pos)
                    print(sp,"",*w)
                #(R)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                win.blit(BG, (0,0))
                BG=pg.image.load("background.png")
                pg.display.update()
                #(M)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_m and muted==False :
                pg.mixer.music.set_volume(0)
            elif event.key == pg.K_m and muted==True:
                pg.mixer.music.set_volume(100)
            #(E)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e and not editorOpen:
                editorOpen=True
                win.blit(editordisplay, (0,0))
                win.blit(zones, (665,255))
                win.blit(splittermod, (665,55))
                win.blit(reflektormod, (125,55))
                win.blit (jarmod, (125,255))
                pg.display.update()
            elif event.key == pg.K_e and editorOpen:
                editorOpen=False
                win.blit(BG, (0,0))
                pg.display.update() #closes editor
        #Adding Reflektors (F)
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_f and mode!="reflektor" and editorOpen:
                mode="reflektor"
                editorOpen=False
                win.blit(BG, (0,0))
                pg.display.update() #closes editor
            elif event.key==pg.K_f and mode=="reflektor" and not editorOpen:
                mode="vertices"
                pg.display.update()                                                                                                                                                                                                                   
        #Adding Splits (P)
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_p and mode!="split" and editorOpen:
                    mode="split"
                    editorOpen=False
                    win.blit(BG, (0,0))
                    pg.display.update()
        #AltF4
                elif event.key==pg.K_p and mode=="split" and not editorOpen:
                    mode="vertices"
                    editorOpen=False
                    win.blit(BG, (0,0))
                    pg.display.update()
        #Adding Canopic Jars (J):
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_j and mode!="jars" and editorOpen:
                    mode="jars"
                    editorOpen=False
                    win.blit(BG,(0,0))
                    pg.display.update()
                elif event.key==pg.K_j and mode=="jars" and editorOpen:
                    mode="vertices"
                    editorOpen=False
                    win.blit(BG, (0,0))
                    pg.display.update()
            #Zoning Laws (Z/Y)
            if event.type==pg.KEYDOWN:
                if (event.key==pg.K_z or event.key==pg.K_y) and mode!="zone" and editorOpen:
                    mode="zone"
                    zone1=[vertices[0],vertices[1],vertices[2]]
                    zone2=[vertices[3],vertices[-5]]
                    dzone=[vertices[-5],vertices[-4],vertices[-3]]
                    pyr=[vertices[-2],vertices[-1]]
                    print("Zoning Complete!")
                    win.blit(BG,(0,0))
                    editorOpen=False
                    mode="vertices"
                    pg.display.update()
        #Vertice Input(I)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_i:
                x=int(input("Input X coordinate"))
                y=int(input("Input Y coordinate"))
                coord= x,y
                vertices.append(coord)
            #Vertice Deletion (D)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                vertices.pop()
            #Credits (C)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c and not creditsOpen:
                    win.blit(creators,(0,0))
                    creditsOpen=True
                    pg.display.update()
                elif event.key == pg.K_c and  creditsOpen:
                    win.blit(BG,(0,0))
                    creditsOpen=False
                    pg.display.update()