from rest_framework.exceptions import APIException

class QueryParamsIdDispensaNotFound(APIException):
    status_code = 400
    default_detail = 'query params "id_dispensa" non specificato, per altre informazioni consultare la documentazione'
    default_code = 'query_params_id_dispensa_not_found'

class UserHasNoPermission(APIException):
    status_code = 403
    default_detail = 'utente non ha i permessi per accedere a questa risorsa'
    default_code = 'user_has_no_permission'