def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorised"
        case 403:
            return "Forbidden"
        case 404:
            return "Not found"
        case 408:
            return "Request Time-out"
        case 401|403|404:
            return "Client error"
        case 500:
            return "Internal server error"
        

value = int(input())
        
print(http_error(value))
        