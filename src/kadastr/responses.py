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
