import os

os.system('git bisect start a0b82d138e1c89c38d13e48a68f74c2eb4bbb0e9 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')