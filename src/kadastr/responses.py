ext_api_resp = {
    200: {
        "description": "External server is working",
        "content": {"application/json": {"example": {'server_status': 'ok'}}},
    },
    504: {
        "description": "External server is not reachable",
        "content": {
            "application/json": {"example": {'server_status': 'disabled'}}
        },
    },
}
query_resp = {
    504: {
        "description": "External server is not reachable",
        "content": {
            "application/json": {"example": {'query_id': 'try later, please'}}
        },
    },
}

result_resp = {
    406: {
        "description": "Query id given doesn't exist",
        "content": {
            "application/json": {
                "example": {"result": "this query_id doesn't exist"}
            }
        },
    },
    504: {
        "description": "External server is not reachable",
        "content": {
            "application/json": {"example": {'query_id': 'try later, please'}}
        },
    },
}
