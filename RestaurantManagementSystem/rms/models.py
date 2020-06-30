from django.db import models
from django.http import HttpResponse

class Manager(models.Model):
    managerID = models.IntegerField(primary_key=True)
    managerName = models.CharField(max_length=30)

    def __str__(self):
        return str(self.managerID) + "\t\t" + self.managerName


class Chef(models.Model):
    chefID = models.IntegerField(primary_key=True)
    chefName = models.CharField(max_length=30)
    managerID = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.chefID) + "\t\t" + self.chefName + "\t\t" + str(self.managerID)


class Waiter(models.Model):
    waiterID = models.IntegerField(primary_key=True)
    waiterName = models.CharField(max_length=30)
    managerID = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.waiterID) + "\t\t" + self.waiterName + "\t\t" + str(self.managerID)


class Cashier(models.Model):
    cashierID = models.IntegerField(primary_key=True)
    cashierName = models.CharField(max_length=30)
    managerID = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.cashierID) + "\t\t" + self.cashierName + "\t\t" + str(self.managerID)


class Item(models.Model):
    itemNo = models.IntegerField(primary_key=True)
    itemName = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.itemNo) + "\t\t" + self.itemName + "\t\t" + str(self.price)


class Customer(models.Model):
    customerID = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=30)
    phoneNo = models.IntegerField()

    def __str__(self):
        return str(self.customerID) + "\t\t" + self.customerName + "\t\t" + str(self.phoneNo)


class Bill(models.Model):
    billNo = models.IntegerField()
    itemNo = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    qty = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    cashierID = models.ForeignKey(Cashier, on_delete=models.DO_NOTHING)
    customerID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('billNo', 'itemNo')

    def __str__(self):
        return str(self.billNo) + "\t|\t" + str(self.itemNo) + "\t|\t" + str(self.qty) + "\t|\t" + str(self.amount) + "\t|\t" + str(self.cashierID) + "\t|\t" + str(self.customerID)