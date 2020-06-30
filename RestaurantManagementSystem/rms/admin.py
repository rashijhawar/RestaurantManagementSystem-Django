from django.contrib import admin

from .models import Manager
from .models import Chef
from .models import Waiter
from .models import Cashier
from .models import Item
from .models import Customer
from .models import Bill


admin.site.register(Manager)
admin.site.register(Chef)
admin.site.register(Waiter)
admin.site.register(Cashier)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Bill)