from datetime import datetime


def generate_log_file_name(prefix=""):
    return prefix + datetime.now().strftime("%d-%m-%Y_%H.%M.%S") + ".json"
