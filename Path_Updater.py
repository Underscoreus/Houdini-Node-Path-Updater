import hou

categories = ['Old Cache Path', 'New Cache Path', 'Old Render Path', 'New Render Path', 'Old Light Path', 'New Light Path', 'Old Texture Path', 'New Texture Path']

message = 'Define the base folder for the old and new folder structure. Like /LOSTBOYS/FX/RENDER   /mynewfolder/fx/newrenders'

cc = 1

usrreturn = hou.ui.readMultiInput(message,categories, buttons=('Update All Nodes', 'Update Selected Nodes', 'Cancel'), close_choice=cc)

paths = usrreturn[1]

clicked = usrreturn[0]

#Format: Old var, New var
pathvars = {
"cache":[paths[0], paths[1]],
"render":[paths[2], paths[3]],
"light":[paths[4], paths[5]],
"texture":[paths[6], paths[7]]
}

#Format: Node name, parameter name, category
### THIS IS WHERE ONE CAN ADD ADDITIONAL NODES TOO THE TOOL###
nodedict = {
"file":[["file"], "cache"],
"filecache":[["file"], "cache"],
"rop_geometry":[["sopoutput"], "cache"],
"ifd":[["vm_picture"], "render"],
"flipbook":[["output"], "render"],
"texture::2.0":[["map"], "texture"],
"principledshader::2.0":[["basecolor_texture","ior_texture","rough_texture",
"aniso_texture","anisodir_texture","metallic_texture","reflect_texture",
"reflecttint_texture","coat_texture","coatrough_texture","transparency_texture",
"transcolor_texture", "transdist_texture","dispersion_texture",
"sss_texture","sssdist_texture","ssscolor_texture","sheen_texture",
"sheentint_texture","emitcolor_texture","opaccolor_texture","baseNormal_texture",
"coatNormal_texture","dispTex_texture"], "texture"],
"envlight":[["env_map"], "light"],
"Redshift_ROP":[["RS_outputFileNamePrefix"], "render"],
"rslightdome::2.0":[["env_map"], "light"],
"redshift::TextureSampler":[["tex0"], "texture"],
"Redshift_Proxy_Output":[["RS_archive_file"], "cache"],
"rop_alembic":[["filename"], "cache"]
}


if clicked == 0:
    allnodes = hou.node('/').allSubChildren()
elif clicked == 1:
    allnodes = hou.selectedNodes()


nodesaffected = 0



def updatePath(innode):
    ntype = innode.type().name()
    
    #Checking that the value to replace is not empty, if it is, don't execute the code.
    if pathvars[nodedict[ntype][1]][0] != "":
        if innode.isInsideLockedHDA() == False:
            for x in nodedict[ntype][0]:
                val = innode.parm(x).rawValue()
                oldval = val
                
                val = val.replace(pathvars[nodedict[ntype][1]][0], pathvars[nodedict[ntype][1]][1])
                
                innode.parm(x).set(val)
            
            if val != oldval:
                global nodesaffected
                nodesaffected += 1
        

if clicked != 2:
    for child in allnodes:
        try:
            updatePath(child)
        except:
            pass
            
    hou.ui.displayMessage(('Path changed on ' + str(nodesaffected) + ' nodes'))