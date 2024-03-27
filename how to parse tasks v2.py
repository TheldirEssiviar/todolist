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

# refer to the document, and then pull data from it in some form, then save
# that data as the info in a new instance of currenttask

taskparameterlist = ("id", "title", "parents", "daughters", "tags", "inherittags")
idcounter = 0

class currenttask:
    global taskparameterlist
    '''def __init__(self, id, title, parents, daughters, tags, inherittags):
        self.id = id # int
        self.title = title # str
        self.parents = parents # list
        self.daughters = daughters # list
        self.tags = tags # list
        self.inherettags = inherittags # bool'''
    def __init__(self, taskparameterlist):
        ownparameters = {}
        for i in taskparameterlist:
        
        for each type of parameter (each parameter in taskparameterlist):


        for i in taskparameterlist:
            # set the stuff up
            i += 1

    '''for each parameter passed, create a dictionary entry for it
        dont need to mess with setting default parameter values or
        any of that bs. allows dynamically changing the list of parameter
        types. allows omitting or including whichever parameters desired'''
    
    def __init__(self):
        # idk, do we even need stuff? probably yes
    
    def getparameters()

    
    def edit():
        # dynamically create subfunctions for each parameter to edit each
        edit.[parameter name]

    def read(id):
        # finds the task with the specified id
        # saves that section as a string
        # parses the string to set all the class variables correctly

    def create(title, tempparents = "null", tempdaughters = "null", temptags = "null", tempinhirettags = False):
