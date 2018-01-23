class PenguinError(Exception):
    """docstring for PenguinError"""
    pass


class RespWithFailedCodeError(PenguinError):
    def __init__(self, code, resp_json, resp):
        super(RespWithFailedCodeError, self).__init__(
            'penguin resp with error content, code: {}'.format(code))
        self.code = code
        self.resp_json = resp_json
        self.resp = resp


class RespContentValueError(PenguinError):
    def __init__(self, msg=None):
        super(RespContentValueError, self).__init__(
            msg or 'resp content value error')


class CredentialError(PenguinError):
    def __init__(self, msg=None):
        super(CredentialError, self).__init__(
            msg or 'credential error')
