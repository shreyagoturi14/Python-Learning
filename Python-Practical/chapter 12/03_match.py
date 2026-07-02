def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknow status"
            
print(http_status(533))
print(http_status(200))