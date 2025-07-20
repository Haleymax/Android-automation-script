import os



base_path = os.path.dirname(os.path.dirname(__file__))

package_path = os.path.join(base_path, 'package')

file_path = os.path.join(package_path, 'app-release.apk')

screen_path = os.path.join(base_path, 'picture')

config_path = os.path.join(base_path, 'config')

config_file = os.path.join(config_path, 'config.yaml')