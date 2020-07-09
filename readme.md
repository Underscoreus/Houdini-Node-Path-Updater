# Houdini Path Updater

A quick tool I wrote at the beginning of lockdown that would easily allow me to update all the paths in my houdini scenes from using the old paths from a different network to my own personal home network.

The tool simply gathers a list of all nodes in the scene, checks them agains a list of certain node types and if it finds a match, it will do a string replacement based on user input to update the paths.

## Instalation:

I've included two main ways of installing this utility, my .shelf file with the tool, name and icon in it aswell as the raw python code.

### Method 1:

After downloading, copy the .shelf file to this folder on your machine:

Windows: C:\Program Files\Side Effects Software\Houdini xx.x.xxx\houdini\toolbar

Mac: Libary/Frameworks/Houdini Framework/Versions/xx.x.xxx/Resources/hodini/toolbar (Note that I am unfamiliar with Mac and don't know if this path is correct)

Linux: /opt/hfs xx.x.xxx/houdini/toolbar

After restarting houdini the "MB_Shelf" should be avalible to add to your shelf tray by clicking the "+" button next to your shelves titles, hovering over the "Shelves" option and scrolling down to "MB_Shelf".

### Method 2:

After downloading, open houdini, either create a new shelf and add a new tool to this shelf or create a new tool in an existing shelf.
Right click the new tool and select "Edit Tool", click on the "Script" tab in the new window, then copy the contents of the "Path_Updater.py" file and paste it into the text field in the "Script" tab. Click "Apply" and "Accept" and the tool is ready too use!

(Note that to use the "Print Node Name" tool mentioned in the usage section you will need to repeat this process for that tool as well)

## Usage:

After instalation, to use the tool simply press the button in the shelf, a new window will appear where you can enter what part of the path you want to replace/update. Simply enter the part you wish to replace in the "Old" field and what you want it changed too in the "New" field.
These "Old" and "New" fields are split into four categories, "Cache", "Render", "Texture" and "Lights".
These categories determine which type of node gets certain changes. The "Cache" input fields will only update cache related nodes such as filecache, file, rop geometry, redshift proxy output and rop alembic output.

The nodes that are recognized by this tool can easily be edited/expanded by right clicking the tool in the shelf, selecting "edit tool", going to the "Script" tab and scrolling down to the "### THIS IS WHERE ONE CAN ADD ADDITIONAL NODES TOO THE TOOL###" comment.
To add a new node simply copy the last line of the "nodedict" variable and paste it on a new line right below it inside the curly brackets {}, remember to add a comma "," after the last line, then filling in the details for the node you want.
The format is as follows, first string is the name of the node type (not the name of the node it self but the type of node, this can be found by running the other tool included in the shelf called "Print Node Name" and looking in the terminal Window), the second string is the parameter name you want to affect inside the node, this can be found by hovering over the parameter name inside the node, the third string is the category this node falls into, this will control what text field will change the nodes path. The different categories are "cache", "render", "light", "texture".

### Here is an example:

#### Before:
```python
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
"Redshift_Proxy_Output":[["RS_archive_file"], "cache"]
}
```
#### After:
```python
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
"Redshift_Proxy_Output":[["RS_archive_file"], "cache"]__,
"rop_alembic":[["filename"], "cache"]__
}
```
