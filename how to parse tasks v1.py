# figuring out how to parse tasks

'''
format:

{{
[[id=#]]
[[title=some text]]
[[parents = #s for parents]]
[[daughters = #s for daughters]]
[[inherettags = bool]]
}}

if inherettags = True, then self will inheret tags from parent

'''

class currenttask:
    def __init__(self, id, title, parents, daughters, tags, inherettags):
        self.id = id # int
        self.title = title # str
        self.parents = parents # list
        self.daughters = daughters # list
        self.inherettags = inherettags # list
    def read():
        
        taskstring = # put all the factors into a string
        # return that string
    
    def edit(parameter, modification, value="nothing"):
        if parameter == "title":
            if value != "nothing":
                currenttask.title = value

    def edittitle(newtitle): # edits the title of the task
        currenttask.title = newtitle
    def append(variable, content)
    def addparent(newparent): # adds a new parent task
        currenttask.parents.append(newparent)
    def removeparent(parent):
        currenttask.parents.remove(parent)


would like:

currenttask.edit.title(newtitle)
currenttask.add.tags(new tag, optional new tags)
currenttask.inherettags = True/False
currenttask.add.parents(new parent, optional new parents)
currenttask.add.daughters(new daughter, optional new daughters)
currenttask.remove.parents(parent, optional additional parents)
currenttask.remove.daughters(daughter, optional additional daughters)
currenttask.save # essentially git.push, saves all the info
                 # in string form to the document in the right place



    




# creating a task:
# do the stuff to get the info for a task from the user
# save that into currenttask
# then, create a string that consists of the info gained from currenttask
# include line breaks and formatting
# append that text to the document
        
# reading a task:
# find id=#
# 