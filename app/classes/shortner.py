import random
import string


class Shortener:
    def generate_short_url(self, size=4, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
