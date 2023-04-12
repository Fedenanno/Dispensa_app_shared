from rest_framework.exceptions import APIException

class QueryParamsIdDispensaNotFound(APIException):
    status_code = 400
    default_detail = 'query params "id_dispensa" non specificato, per altre informazioni consultare la documentazione'
    default_code = 'query_params_id_dispensa_not_found'

class PayloadDataNotValid(APIException):
    status_code = 400
    default_detail = 'payload data non valido, per altre informazioni consultare la documentazione'
    default_code = 'payload_data_not_valid'

class DispensaNotFound(APIException):
    status_code = 404
    default_detail = 'dispensa non trovata'
    default_code = 'dispensa_not_found'

class DispensaAlreadyShared(APIException):
    status_code = 400
    default_detail = 'dispensa già condivisa con questo utente'
    default_code = 'dispensa_already_shared'


#---- USER ----
class UserHasNoPermission(APIException):
    status_code = 403
    default_detail = 'utente non ha i permessi per accedere a questa risorsa'
    default_code = 'user_has_no_permission'

class UserIsNotOwner(APIException):
    status_code = 403
    default_detail = 'utente non è il proprietario della dispensa'
    default_code = 'user_is_not_owner'

class UserNotFound(APIException):
    status_code = 404
    default_detail = 'utente non trovato'
    default_code = 'user_not_found'

class SameUser(APIException):
    status_code = 400
    default_detail = "Gli utenti non possono essere uguali"
    default_code = 'same_user'