result = []
def backtrack(path, options):
    if (ending_condition):
        result.add(path)
        return
    
    for choice in options:
        make(choice)
        backtrack(path, options)
        redo(option)