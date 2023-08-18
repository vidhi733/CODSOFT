from tkinter import *
from typing import ValuesView

class toDoList(Frame):
     
    toDoDict = {0: None}
    def __init__(self, master = None):
        super().__init__(master, width = 500, height = 350)
        self.master = master
        self.pack(fill = BOTH)
        self.createWidgets()
        
    def createWidgets(self):
        
        self.title = Label(self, text = 'To Do List')
        self.label1 = Label(self, text = 'Enter your to do')
        self.label2 = Label(self, text = 'Enter a number to delete')
        self.toDoTextBox = Entry(self)
        self.toRemoveTextBox = Entry(self)
        self.submitToDo = Button(self, text = 'Submit', command = self.addItem)
        self.eraseToDo = Button(self, text = 'Delete', command = self.eraseItem)
        self.title.place(relx = .4, y = 5, width = 100, height = 20)
        self.label1.place(relx = .2, y = 25, width = 100, height = 20)
        self.toDoTextBox.place(relx = .2, y = 45, width = 100, height = 20)
        self.submitToDo.place(relx = .2, y = 85, width = 100, height = 20)
        self.label2.place(relx = .15, y = 125, width = 150, height = 20)
        self.toRemoveTextBox.place(relx = .2, y = 150, width = 100, height = 20)
        self.eraseToDo.place(relx = .2, y = 180, width = 100, height = 20)
    
    def addItem(self, toDoDict = toDoDict):
        
        text = self.toDoTextBox.get()
        errorMessage = Label(self, text = '', fg = 'red')
        errorMessage.place(relx = .2, y = 110, width = 100, height = 20)
        if len(text) > 0:
            errorMessage.config(text = '')
            toDoKeys = list(toDoDict.keys())
            toDoDict[toDoKeys[-1]+1] = text
            toDoKeys = list(toDoDict.keys())
            toDoArr = []
            for i in toDoKeys:
                toDoArr.append(f'{i}.- {toDoDict[i]}')
            
            toDoArr.pop(0)
            self.showToDo = Label(self, text = '\n'.join(toDoArr), anchor = 'nw', justify = 'left')
            self.showToDo.place(relx = .5, y = 25, width = 200, relheight = 1)
            self.toDoTextBox.delete(0, 'end')
        else:
            errorMessage.config(text = 'Input something')
    def eraseItem(self, toDoDict = toDoDict):
        
        errorIndex = Label(self, text = '', fg = 'red')
        errorIndex.place(relx = .2, y = 200, width = 100, height = 20)
        
        toDoKeys = toDoDict.keys()
        try:
            rindex = int(self.toRemoveTextBox.get())
            errorIndex.config(text = '')
            if rindex == 0 or len(toDoKeys) == 1 or len(toDoKeys)-1 < rindex: raise ValueError
            for i in range(rindex, len(toDoKeys)-1):
                
                toDoDict[i] = toDoDict[i+1]
            toDoDict.pop(len(toDoKeys)-1)
            toDoKeys = toDoDict.keys()
            
            toDoArr = []
            for i in toDoKeys:
                toDoArr.append(f'{i}.- {toDoDict[i]}')
            toDoArr.pop(0)
            self.showToDo.config(text = '\n'.join(toDoArr))
            self.toRemoveTextBox.delete(0, 'end')
        except:
            errorIndex.config(text = 'Invalid Number')
    
root = Tk()
root.wm_title('To Do List')

app = toDoList(root)
app.mainloop()
app.mainloop()