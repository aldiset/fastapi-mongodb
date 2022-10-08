from starlette.config import Config

config = Config('.env')

MONGOHOST = config('HOST', default='localhost')
MONGOPORT = config('MONGOPORT', default=27017)
MONGONAME = config('MONGONAME', default='books')