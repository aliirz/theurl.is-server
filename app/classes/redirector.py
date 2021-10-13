from starlette.responses import RedirectResponse


class Redirector:
    def redirect(self, url):
        return RedirectResponse(url=url)
