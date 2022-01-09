import os

from imageTransformer.app import mongo

def getMissingArgs(requestBody, requiredArguments):
    missingArgs = []
    for arg in requiredArguments:
        if arg not in requestBody:
            missingArgs.append(arg)
    return missingArgs

def saveTempFileAndCleanup(temp_filepath, db_filename):
    mongo.save_file(db_filename, open(temp_filepath, 'rb'))
    os.remove(temp_filepath)

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else None
