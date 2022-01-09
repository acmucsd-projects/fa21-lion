class SESSION_KEYS:
    CURRENT_USERNAME = 'currentUsername'

class USER_DOCUMENT_KEYS:
    USERNAME = 'username'
    PASSWORD_HASH = 'passwordHash'
    IMAGES = 'images'
    VIDEOS = 'videos'
    FILENAME = 'filename'
    TRANSFORMED_FILENAME = 'transformed'

class REQUEST_KEYS:
    USERNAME = 'username'
    PASSWORD = 'password'
    VIDEO = 'video'
    IMAGE = 'image'

TRANSFORMED_FILE_PREFIX = 'transformed-'
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_VIDEO_EXTENSIONS = ['mp4', 'mov']