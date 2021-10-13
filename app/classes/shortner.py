import random
import string


class Shortener:
    def generate_the_url(self, size=4, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
