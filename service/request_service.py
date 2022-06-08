
from repository.request_dao import insert_request_info



def create_request(input):
    #login_dto = select_user_by_id(emp_id)
    req_id = insert_request_info(input.get("emp_id"), input.get("description"), input.get("amount"), input.get("status"), input.get("comments"))

    if req_id is not None:
        return req_id
