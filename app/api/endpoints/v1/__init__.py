from app.api.endpoints.v1 import root, white_blood_cells_endpoint

v1_api_routers_dict: dict = {
    "prefix": "/v1",
    "routers_list": [
        root.router,
        white_blood_cells_endpoint.router
    ]
}
