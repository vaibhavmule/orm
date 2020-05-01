""" Web Routes """
from masonite.routes import Get

ROUTES = [
    Get('/', 'PackageController@show').name('welcome'),
]
