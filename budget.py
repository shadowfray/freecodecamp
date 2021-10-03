#Shadowfray
#Budgets note program for freecodecamp.org
'''This program is designed to track a budget as long as its running.
The user can create different categories for their budget such as Food
or Transportation. They can deposit/alocate money to each category and
then withdraw that cash as needed, leaving little notes to remember what
each purchase was for.

transfer(amount, category-from, category-to)

create_spend_chart() is used to see how much of their money for each category
theyve used up / how much is left.'''


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = {}
        self.total = 0

    def __str__(self):
        
        selfkeys = self.ledger.keys()
        keys_23char = [] #for our display we only want 23 characters displayed here
        values_2decimals = [] #for our display we floats but with 2 decimals
        final_print = f'{self.name}'.center(30, '*')  + '\n' #the string we will return at the end
        
        for k in selfkeys:
            #shortens keys
            if len(k) > 23:
                keys_23char.append(k[:22])
            else:
                keys_23char.append(k)
                
            #makes sure every number is a float with 2 decimal points
            value_list = list(str(float(self.ledger[k])))
            addedZeroes = len(value_list[value_list.index('.'):]) -1 
            if addedZeroes == 1:
                value_list.append('0')
                values_2decimals.append(''.join(value_list))
            else:
                values_2decimals.append(''.join(value_list))

        for i in range(len(values_2decimals)):
            spaces_len = 23 - len(keys_23char[i]) #to create blank space for notes
            num_space = 7 - len(values_2decimals[i]) #to create blank spaces for numbers
            line = keys_23char[i] + ' '*(spaces_len + num_space) + values_2decimals[i] + '\n'
            final_print += line

        final_print += f'Total: {self.total}\n'

        return final_print
            
    def deposit(self, amount, description=''):
        self.ledger[description] = amount
        self.total += amount

    def withdraw(self, amount, category):
        if self.check_funds(amount):
            self.ledger[category] = (-1 * amount)
            self.total -= amount
        else:
            return 'Not enough funds!'

    def get_balance(self):
        return f'${self.total}'

    def transfer(self, amount, cat_from, cat_to):
        if cat_from.check_funds(amount):
            cat_from.ledger[f'transfer to {cat_to.name}'] = amount * -1
            cat_from.total -= amount
            cat_to.ledger[f'transfer from {cat_from.name}'] = amount
            cat_to.total += amount
            return f'${amount} transfered from {cat_from.name} to {cat_to.name}'
        else:
            return 'Not enough funds!'

    def check_funds(self, amount):
        if amount <= self.total:
            return True
        else:
            return False


def create_spend_chart(categList): #takes a list of all categories
    net_money = []
    final_print = 'AMOUNT SPEND'.center(30,'*') + '\n'
    for i in categList:
        spent_total, deposit_total = 0, 0
        for k in i.ledger.keys():
            if i.ledger[k] < 0:
                spent_total += i.ledger[k]
            if i.ledger[k] > 0:
                deposit_total += i.ledger[k]
                
        spent_total = spent_total * -1 #flips the value so its no longer negative
        percent_spent = spent_total / deposit_total
        percent_fin = round(percent_spent,4) * 100 #rounds to 2 decimals of %

        #prints the categories and percents
        final_print += f'{i.name}: {percent_fin}% spent \n'

    return final_print
