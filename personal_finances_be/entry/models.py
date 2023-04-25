from django.db import models

class AccountBalance(models.Model):
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    balance = models.DecimalField("account balance", decimal_places=2, max_digits=30)
    date_effective = models.DateField("date effective")


class Account(models.Model):
    name = models.CharField("account name", max_length=100)


class Paycheck(models.Model):
    account = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField("amount on paycheck", decimal_places=2, max_digits=50)
    is_paid = models.BooleanField(default=False)


class IndependentIncome(models.Model):
    name = models.CharField("independent income name", max_length=100)
    amount = models.DecimalField("independent income amount", decimal_places=2, max_digits=50)
    date = models.DateField("independent income date")

class WageJob(models.Model):
    name = models.CharField("wage job name", max_length=100)
    wage = models.DecimalField("hourly rate", decimal_places=2, max_digits=50)
    pay_interval = models.IntegerField("weeks between paydays")
    pay_weekday = models.IntegerField("weekday of payday", choices=
    (
        (0, "Monday"),
        (1, "Tuesday"), 
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday")
        )
    )


class WageTimesheet(models.Model):
    wage_job = models.ForeignKey("WageJob", on_delete=models.CASCADE)
    date = models.DateField("date worked")
    hours = models.DecimalField("hours worked", decimal_places=2, max_digits=5)


class Expense(models.Model):
    account = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField("expense amount", decimal_places=2, max_digits=50)
    description = models.CharField("expense description", max_length=255)
