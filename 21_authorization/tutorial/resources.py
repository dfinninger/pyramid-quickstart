from pyramid.security import Allow, Everyone


class Root:
    __acl__ = [(Allow, Everyone, "view"), (Allow, "group:editors", "edit")]

    def __init__(self, request):
        pass
