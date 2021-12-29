def getMissingArgs(requestBody, requiredArguments):
    missingArgs = []
    for arg in requiredArguments:
        if arg not in requestBody:
            missingArgs.append(arg)
    return missingArgs